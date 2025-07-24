import os
from datetime import datetime
from typing import Optional
from docx import Document


def _timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H-%M-%S")


def salvar_markdown(base_dir: str, nome_base: str, conteudo_md: str) -> str:
    os.makedirs(base_dir, exist_ok=True)
    caminho = os.path.join(base_dir, f"{_timestamp()}_{nome_base}.md")
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo_md)
    return caminho


def salvar_docx(base_dir: str, nome_base: str, conteudo_md: str) -> str:
    """Converte texto simples em parágrafos DOCX (sem render completo de Markdown)."""
    os.makedirs(base_dir, exist_ok=True)
    caminho = os.path.join(base_dir, f"{_timestamp()}_{nome_base}.docx")
    doc = Document()
    for linha in conteudo_md.splitlines():
        doc.add_paragraph(linha)
    doc.save(caminho)
    return caminho