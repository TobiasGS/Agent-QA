from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile", temperature=0)

complementador = Agent(
    model=llm,
    description=(
        "Você é um Especialista em Complementação de Testes. Recebe cenários BDD e os enriquece: "
        "adicione casos alternativos, fluxos negativos, dados inválidos, limites e cenários de erro de API. "
        "Inclua tags como @regressivo, @critico, @fumaca quando fizer sentido."
    ),
    markdown=True,
)