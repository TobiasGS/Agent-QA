import faiss
import numpy as np
import os
import pickle
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils.loader import carregar_arquivo_generico  # corrigido
from utils.groq_embeddings import GroqEmbeddings # sua importação customizada
from dotenv import load_dotenv

load_dotenv()  # garante que as variáveis do .env são carregadas


def indexar_base_conhecimento_faiss(diretorio_docs="docs/", caminho_faiss="faiss_index"):
    print("[LOG] Indexando base de conhecimento (FAISS)...")
    
    documentos = []
    # Carregar todos os documentos do diretório, suportando pdf, docx, txt
    for nome_arquivo in os.listdir(diretorio_docs):
        caminho_arquivo = os.path.join(diretorio_docs, nome_arquivo)
        if os.path.isfile(caminho_arquivo):
            try:
                docs = carregar_arquivo_generico(caminho_arquivo)
                documentos.extend(docs)
            except Exception as e:
                print(f"[AVISO] Falha ao carregar {caminho_arquivo}: {e}")

    if not documentos:
        print("[ERRO] Nenhum documento encontrado.")
        return

    # Quebra os documentos em chunks menores para melhor indexação
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    documentos_chunkados = splitter.split_documents(documentos)

    embeddings = GroqEmbeddings(
        model="nomic-embed-text",
        groq_api_key=os.getenv("GROQ_API_KEY")  # Certifique-se de ter essa variável no seu .env
    )

    # Cria o índice FAISS com os documentos chunkados e embeddings
    db = FAISS.from_documents(documentos_chunkados, embeddings)
    
    # Salva localmente o índice e os metadados
    db.save_local(caminho_faiss)
    
    print(f"[LOG] Base indexada com sucesso e salva em '{caminho_faiss}/' ✅")


def criar_indice_faiss(dimensao: int):
    return faiss.IndexFlatL2(dimensao)


def salvar_indice_faiss(indice, caminho: str):
    faiss.write_index(indice, caminho)


def carregar_indice_faiss(caminho: str):
    return faiss.read_index(caminho)


def adicionar_vetores(indice, vetores: np.ndarray):
    indice.add(vetores)


def salvar_metadados(metadados, caminho: str):
    with open(caminho, 'wb') as f:
        pickle.dump(metadados, f)


def carregar_metadados(caminho: str):
    with open(caminho, 'rb') as f:
        return pickle.load(f)
