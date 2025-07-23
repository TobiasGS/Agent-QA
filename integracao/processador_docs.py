import os
from typing import Dict
from agents.gerador_bdd import gerador_bdd
from agents.complementador import complementador
from agents.validador import validador
from utils.loader import carregar_arquivo_generico
from utils.kb_loader import carregar_base_conhecimento, concatenar_texto_docs
from utils.export import salvar_markdown, salvar_docx


# =============================
# PROMPTS BASE DO PIPELINE
# =============================
PROMPT_GERAR = """Gere cenários BDD usando Gherkin (Português). Use a história abaixo e considere o contexto de base de conhecimento, se fornecido.
História:
{historia}

Base de conhecimento (contexto):
{kb}
"""

PROMPT_COMPLEMENTAR = """A seguir estão cenários BDD gerados. Melhore-os: adicione casos alternativos, negativos, dados limite, status de API e tags.
Cenários:
{cenarios}
"""

PROMPT_VALIDAR = """Revise os cenários BDD abaixo. Diga se cobrem os critérios esperados. Liste gaps, riscos, testes não funcionais sugeridos e priorização.
Cenários complementados:
{cenarios}
"""


# =============================
# PIPELINE
# =============================

def processar_historia(
    caminho_historia: str,
    diretorio_kb: str = None,
    salvar_em: str = "output/resultados",
    nome_base: str = None,
    incluir_kb: bool = True,
    gerar_docx: bool = True,
) -> Dict[str, str]:
    print("[LOG] Iniciando processamento da história...")

    # --- Carregar história ---
    print("[LOG] Carregando história do arquivo:", caminho_historia)
    docs_hist = carregar_arquivo_generico(caminho_historia)
    historia_texto = "\n\n".join(d.page_content for d in docs_hist)

    # --- Carregar KB ---
    kb_texto = ""
    if incluir_kb and diretorio_kb and os.path.isdir(diretorio_kb):
        print("[LOG] Carregando base de conhecimento do diretório:", diretorio_kb)
        kb_docs = carregar_base_conhecimento(diretorio_kb)
        print("[LOG] Concatenando textos da base de conhecimento...")
        kb_texto = concatenar_texto_docs(kb_docs)

    # --- Rodar Gerador BDD ---
    print("[LOG] Gerando cenários BDD com agente...")
    prompt_gerar = PROMPT_GERAR.format(historia=historia_texto, kb=kb_texto)
    resp_bdd = gerador_bdd.run(prompt_gerar)
    cenarios_bdd = resp_bdd.content if hasattr(resp_bdd, "content") else str(resp_bdd)
    print("[LOG] Cenários BDD gerados com sucesso.")

    # --- Complementar ---
    print("[LOG] Complementando cenários...")
    prompt_compl = PROMPT_COMPLEMENTAR.format(cenarios=cenarios_bdd)
    resp_compl = complementador.run(prompt_compl)
    cenarios_complementados = resp_compl.content if hasattr(resp_compl, "content") else str(resp_compl)
    print("[LOG] Cenários complementados com sucesso.")

    # --- Validar ---
    print("[LOG] Validando cenários...")
    prompt_valid = PROMPT_VALIDAR.format(cenarios=cenarios_complementados)
    resp_valid = validador.run(prompt_valid)
    relatorio_validacao = resp_valid.content if hasattr(resp_valid, "content") else str(resp_valid)
    print("[LOG] Validação concluída.")

    # --- Conteúdo final Markdown ---
    print("[LOG] Gerando arquivos de saída (Markdown e DOCX)...")
    conteudo_final = (
        "# Cenários BDD Gerados\n\n" + cenarios_bdd + "\n\n" +
        "# Cenários Complementados\n\n" + cenarios_complementados + "\n\n" +
        "# Relatório de Validação\n\n" + relatorio_validacao
    )

    if nome_base is None:
        nome_base = os.path.splitext(os.path.basename(caminho_historia))[0]

    caminho_md = salvar_markdown(salvar_em, nome_base, conteudo_final)
    caminho_docx = None
    if gerar_docx:
        caminho_docx = salvar_docx(salvar_em, nome_base, conteudo_final)

    print("[LOG] Processamento finalizado.")
    return {
        "historia_texto": historia_texto,
        "kb_texto": kb_texto,
        "bdd": cenarios_bdd,
        "complementado": cenarios_complementados,
        "validacao": relatorio_validacao,
        "arquivo_md": caminho_md,
        "arquivo_docx": caminho_docx,
    }