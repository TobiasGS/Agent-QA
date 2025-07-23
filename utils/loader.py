import os
import glob
from typing import List
from langchain.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def _split_docs(documents, chunk_size=1000, chunk_overlap=100) -> List:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)


def carregar_pdf(caminho_pdf: str, chunk_size=1000, chunk_overlap=100) -> List:
    loader = PyPDFLoader(caminho_pdf)
    docs = loader.load()
    return _split_docs(docs, chunk_size, chunk_overlap)


def carregar_docx(caminho_docx: str, chunk_size=1000, chunk_overlap=100) -> List:
    loader = UnstructuredWordDocumentLoader(caminho_docx)
    docs = loader.load()
    return _split_docs(docs, chunk_size, chunk_overlap)


def carregar_txt(caminho_txt: str, chunk_size=1000, chunk_overlap=100) -> List:
    loader = TextLoader(caminho_txt, encoding="utf-8")
    docs = loader.load()
    return _split_docs(docs, chunk_size, chunk_overlap)


def carregar_arquivo_generico(caminho: str, chunk_size=1000, chunk_overlap=100) -> List:
    caminho_lower = caminho.lower()
    if caminho_lower.endswith(".pdf"):
        return carregar_pdf(caminho, chunk_size, chunk_overlap)
    elif caminho_lower.endswith(".docx"):
        return carregar_docx(caminho, chunk_size, chunk_overlap)
    elif caminho_lower.endswith(".txt"):
        return carregar_txt(caminho, chunk_size, chunk_overlap)
    else:
        raise ValueError(f"Formato não suportado: {caminho}")


def carregar_historia(caminho: str) -> str:
    docs = carregar_arquivo_generico(caminho)
    texto = "\n".join([doc.page_content for doc in docs])
    return texto


def carregar_textos_base_conhecimento(diretorio: str, chunk_size=1000, chunk_overlap=100) -> str:
    """
    Carrega e concatena o conteúdo de todos os arquivos .txt, .pdf e .docx
    do diretório informado, retornando uma única string.
    """
    textos = []
    for ext in ('*.txt', '*.pdf', '*.docx'):
        arquivos = glob.glob(os.path.join(diretorio, ext))
        for arquivo in arquivos:
            try:
                docs = carregar_arquivo_generico(arquivo, chunk_size, chunk_overlap)
                texto_arquivo = "\n".join([doc.page_content for doc in docs])
                textos.append(texto_arquivo)
            except Exception as e:
                print(f"[AVISO] Falha ao carregar {arquivo}: {e}")
    return "\n\n".join(textos)


def salvar_diretrizes(diretriz: str, caminho: str) -> None:
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(diretriz)


def carregar_diretrizes(caminho: str) -> str:
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()


def salvar_cenarios(cenarios: List[dict], caminho: str) -> None:
    with open(caminho, 'w', encoding='utf-8') as f:
        for c in cenarios:
            f.write(c.get("texto", "") + "\n\n")


def carregar_ultima_diretriz(diretorio: str) -> str:
    """Carrega a diretriz mais recente salva no diretório informado."""
    arquivos = glob.glob(os.path.join(diretorio, '*.txt'))
    if not arquivos:
        raise FileNotFoundError("Nenhuma diretriz encontrada no diretório.")

    arquivos.sort(key=os.path.getmtime, reverse=True)
    ultimo_arquivo = arquivos[0]

    with open(ultimo_arquivo, 'r', encoding='utf-8') as f:
        return f.read()
