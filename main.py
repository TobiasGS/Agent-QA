import os
import sys
import time
import glob
import numpy as np
from dotenv import load_dotenv
load_dotenv()

from agents.gerador_bdd import gerador_bdd, gerar_cenarios_bdd
from agents.complementador import complementador
from agents.validador import validador
from agents.bdd_knowledge_agent import gerar_diretrizes_bdd
from integracao.processador_docs import processar_historia
from utils.loader import (
    carregar_ultima_diretriz,
    carregar_textos_base_conhecimento,
    carregar_historia,
    salvar_diretrizes,
    carregar_diretrizes,
    salvar_cenarios,
    carregar_arquivo_generico
    
)
from utils.preenchimento_planilha import preencher_planilha_com_cenarios
from utils.faiss_utils import (
    criar_indice_faiss,
    salvar_indice_faiss,
    adicionar_vetores,
    salvar_metadados
)

from utils.groq_embeddings import GroqEmbeddings



# 🔑 Instancia os embeddings com a API Key do .env
embeddings = GroqEmbeddings(
    api_key=os.getenv("GROQ_API_KEY"),
    model="mixtral-8x7b-32768"
)

INPUT_DIR = os.getenv("INPUT_DIR", "input/historias")
KB_DIR = os.getenv("KB_DIR", "knowledge_base")


def listar_arquivos_historia():
    if not os.path.isdir(INPUT_DIR):
        print(f"Diretório não encontrado: {INPUT_DIR}")
        return []
    arquivos = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
    if not arquivos:
        print("Nenhum arquivo encontrado no diretório.")
        return []
    print("\nArquivos disponíveis:")
    for i, nome in enumerate(arquivos, start=1):
        print(f"{i} - {nome}")
    return arquivos


def menu_agentes_simples():
    print("\n=== Conversar Diretamente com um Agente ===")
    print("1 - Gerador BDD")
    print("2 - Complementador")
    print("3 - Validador")
    print("0 - Voltar")
    esc = input("Escolha: ").strip()
    if esc == "0":
        return
    prompt = input("Digite sua pergunta/prompt:\n> ").strip()
    if esc == "1":
        gerador_bdd.print_response(prompt)
    elif esc == "2":
        complementador.print_response(prompt)
    elif esc == "3":
        validador.print_response(prompt)
    else:
        print("Opção inválida.")


def mostrar_spinner(duracao=3):
    spinner = "|/-\\"
    end_time = time.time() + duracao
    idx = 0
    while time.time() < end_time:
        sys.stdout.write(f"\rProcessando... {spinner[idx % len(spinner)]}")
        sys.stdout.flush()
        time.sleep(0.1)
        idx += 1
    sys.stdout.write("\r" + " " * 20 + "\r")


def menu_pipeline_historia():
    print("\n=== Pipeline: História -> BDD -> Complementação -> Validação ===")
    arquivos = listar_arquivos_historia()
    if not arquivos:
        return
    try:
        idx = int(input("Escolha o número do arquivo: ").strip()) - 1
        if idx < 0 or idx >= len(arquivos):
            print("Número fora do intervalo.")
            return
        caminho = os.path.join(INPUT_DIR, arquivos[idx])
    except ValueError:
        print("Entrada inválida.")
        return

    incluir_kb = input("Incluir Base de Conhecimento? (s/n) [s]: ").strip().lower() or "s"
    incluir_kb = incluir_kb.startswith("s")

    print(f"[LOG] Processando história '{arquivos[idx]}' com KB: {'Sim' if incluir_kb else 'Não'}")
    mostrar_spinner(3)

    try:
        resultado = processar_historia(
            caminho_historia=caminho,
            diretorio_kb=KB_DIR,
            incluir_kb=incluir_kb,
            gerar_docx=True,
        )
    except Exception as e:
        print(f"[ERRO] {e}")
        return

    print("\n=== Resultados ===")
    print(f"Markdown: {resultado.get('arquivo_md', 'N/A')}")
    print(f"DOCX:     {resultado.get('arquivo_docx', 'N/A')}")

    cenarios = resultado.get("cenarios")
    if cenarios:
        try:
            preencher_planilha_com_cenarios(
                cenarios,
                "input/prompts_extras/Modelo Planilha Cenários de Teste - Cenários.csv",
                "output/Planilha_Cenarios_Gerados.csv"
            )
        except Exception as e:
            print(f"[ERRO] Falha ao gerar planilha: {e}")
    else:
        print("[AVISO] Nenhum cenário encontrado.")
    print("Concluído!")


def gerar_diretrizes_base_conhecimento():
    print("[LOG] Carregando base de conhecimento...")
    conhecimento = carregar_textos_base_conhecimento(KB_DIR)
    print("[LOG] Gerando diretrizes...")
    diretriz = gerar_diretrizes_bdd(conhecimento)
    salvar_diretrizes(diretriz, 'output/ultima_diretriz.txt')
    print("[SUCESSO] Diretrizes salvas em: output/ultima_diretriz.txt")


def gerar_cenarios_com_diretriz():
    arquivos = listar_arquivos_historia()
    if not arquivos:
        return
    try:
        idx = int(input("Escolha o número do arquivo: ").strip()) - 1
        if idx < 0 or idx >= len(arquivos):
            print("Número fora do intervalo.")
            return
        caminho = os.path.join(INPUT_DIR, arquivos[idx])
    except ValueError:
        print("Entrada inválida.")
        return

    historia = carregar_historia(caminho)
    diretriz = carregar_ultima_diretriz('diretrizes')

    print("[LOG] Gerando cenários com diretriz...")
    cenarios = gerar_cenarios_bdd(historia, diretriz)
    if cenarios:
        salvar_cenarios(cenarios, "output/cenarios_com_diretriz.feature")
        print("[SUCESSO] Cenários salvos em: output/cenarios_com_diretriz.feature")
    else:
        print("[AVISO] Nenhum cenário gerado.")


def indexar_base_conhecimento_faiss():
    print("[LOG] Indexando base de conhecimento (FAISS)...")
    arquivos = []
    for ext in ('*.txt', '*.pdf', '*.docx'):
        arquivos += glob.glob(os.path.join(KB_DIR, ext))
    if not arquivos:
        print("[ERRO] Nenhum arquivo encontrado em KB.")
        return

    all_chunks, metadados = [], []
    for caminho in arquivos:
        try:
            docs = carregar_arquivo_generico(caminho)
            all_chunks.extend(docs)
            metadados.extend([{"source": caminho}] * len(docs))
        except Exception as e:
            print(f"[AVISO] Erro ao carregar {caminho}: {e}")

    textos = [doc.page_content for doc in all_chunks]
    if not textos:
        print("[ERRO] Nenhum conteúdo para indexar.")
        return

    print("[LOG] Gerando embeddings com Groq...")
    vetores = embeddings.embed_documents(textos)

    vetor_dim = len(vetores[0])
    indice = criar_indice_faiss(vetor_dim)
    adicionar_vetores(indice, np.array(vetores))

    os.makedirs("vector_store", exist_ok=True)
    salvar_indice_faiss(indice, "vector_store/index.faiss")
    salvar_metadados(metadados, "vector_store/metadados.pkl")
    print("[SUCESSO] Índice salvo em vector_store/")


def main():
    while True:
        print("\n==============================")
        print("Menu Principal - Agentes QA")
        print("==============================")
        print("1 - Conversar com Agentes (manual)")
        print("2 - Rodar Pipeline em Arquivo de História")
        print("3 - Gerar diretrizes da Base de Conhecimento")
        print("4 - Gerar cenários com base em uma diretriz salva")
        print("5 - Indexar Base de Conhecimento (FAISS)")
        print("0 - Sair")

        esc = input("Escolha: ").strip()
        if esc == "1":
            menu_agentes_simples()
        elif esc == "2":
            menu_pipeline_historia()
        elif esc == "3":
            gerar_diretrizes_base_conhecimento()
        elif esc == "4":
            gerar_cenarios_com_diretriz()
        elif esc == "5":
            indexar_base_conhecimento_faiss()
        elif esc == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
