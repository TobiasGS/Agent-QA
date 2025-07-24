import os
from typing import List
from .loader import carregar_arquivo_generico


def carregar_base_conhecimento(diretorio_kb: str, chunk_size=1000, chunk_overlap=100):
    """Carrega todos os arquivos suportados na pasta de base de conhecimento."""
    todos_docs = []
    for nome in os.listdir(diretorio_kb):
        caminho = os.path.join(diretorio_kb, nome)
        if not os.path.isfile(caminho):
            continue
        try:
            print(f"[LOG] Carregando arquivo: {nome}", flush=True)  # <-- Exibe nome do arquivo carregado
            docs = carregar_arquivo_generico(caminho, chunk_size, chunk_overlap)
            todos_docs.extend(docs)
        except ValueError:
            # ignora formatos desconhecidos
            print(f"[AVISO] Formato desconhecido ou erro ao carregar: {nome}")  # <-- Log de erro
    return todos_docs


def concatenar_texto_docs(docs) -> str:
    return "\n\n".join(d.page_content for d in docs)
