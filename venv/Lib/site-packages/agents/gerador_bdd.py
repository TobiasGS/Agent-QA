from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

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
Você é um especialista em QA. Com base nas seguintes diretrizes e na história do usuário, gere cenários de teste no formato BDD (Given / When / Then):

Diretrizes:
{diretriz_texto}

História do usuário:
{historia_texto}

Por favor, escreva os cenários BDD completos agrupados por funcionalidade e com exemplos de tabelas quando necessário.
"""
    resposta = gerador_bdd.run(prompt)
    # Supondo que a resposta seja texto com cenários separados por duas quebras de linha
    cenarios = resposta.split("\n\n")
    return [{"texto": c.strip()} for c in cenarios if c.strip()]
