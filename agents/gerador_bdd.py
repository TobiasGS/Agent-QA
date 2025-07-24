from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os
import re

load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile", temperature=0)

gerador_bdd = Agent(
    model=llm,
    description=(
        "Você é um Especialista em QA focado em escrever cenários no formato BDD. "
        "Transforme histórias de usuário, critérios de aceite e regras de negócio em cenários Given / When / Then. "
        "Certifique-se de agrupar cenários por funcionalidade e incluir exemplos de tabelas quando apropriado."
    ),
    markdown=True,
)


def gerar_cenarios_bdd(historia_texto: str, diretriz_texto: str):
    prompt = f"""
Você é um especialista em QA. Com base nas diretrizes e na história do usuário abaixo, gere cenários de teste no formato BDD, usando a sintaxe Gherkin (pode usar Markdown para formatação):

Diretrizes:
{diretriz_texto}

História do usuário:
{historia_texto}

Por favor, escreva os cenários BDD completos agrupados por funcionalidade e com exemplos de tabelas quando necessário.
"""
    resposta = gerador_bdd.run(prompt)
    if hasattr(resposta, "content"):
        texto = resposta.content
    elif hasattr(resposta, "text"):
        texto = resposta.text
    else:
        texto = str(resposta)

    # (Opcional) Limpar markdown para Gherkin puro
    # texto = limpar_markdown(texto)

    # Salva no local e formato desejado
    with open("output/cenarios_com_diretriz.md", "w", encoding="utf-8") as f:
        f.write(texto)

    cenarios = texto.split("\n\n")
    return [{"texto": c.strip()} for c in cenarios if c.strip()]

