# agents/bdd_knowledge_agent.py
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile", temperature=0)

gerador_diretrizes = Agent(
    model=llm,
    description=(
        "Você é um Especialista em QA que gera diretrizes para criação de cenários BDD "
        "com base em uma base de conhecimento técnica. Forneça instruções claras e exemplos."
    ),
    markdown=True,
)

def gerar_diretrizes_bdd(textos_base_conhecimento):
    prompt = (
        "Com base na seguinte base de conhecimento, gere diretrizes para escrever cenários BDD:\n\n"
        + textos_base_conhecimento
    )
    resposta = gerador_diretrizes.run(prompt)
    return resposta["text"]
