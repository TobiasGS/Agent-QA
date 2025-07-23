from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile", temperature=0)

validador = Agent(
    model=llm,
    description=(
        "Você é um Especialista em Validação de Testes. Analisa cenários BDD (brutos ou complementados) e verifica: "
        "cobertura de critérios de aceite, variedade de dados, casos negativos, limites, integrações, mensagens de erro. "
        "Responda com um relatório Markdown: 'Cobertura', 'Gaps', 'Recomendações'."
    ),
    markdown=True,
)