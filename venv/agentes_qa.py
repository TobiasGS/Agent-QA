from agno.agent import Agent 
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv

load_dotenv()

llm = Groq(id="llama-3.3-70b-versatile", temperature=0)

# === Agente 1: Validador de Testes ===
validador_agent = Agent(
    model=llm,
    description=(
        "Você é um Especialista em Validação de Testes. Sua função é revisar os cenários gerados "
        "e verificar se eles estão adequados à história de usuário, apontando pontos de melhoria e gaps."
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=False,
    markdown=True,
)

# === Agente 2: Complementador de Testes ===
complementador_agent = Agent(
    model=llm,
    description=(
        "Você é um Especialista em Complementação de Testes. Sua função é transformar as sugestões fornecidas "
        "pelo Especialista em Validação em cenários de teste completos e detalhados, utilizando boas práticas."
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=False,
    markdown=True,
)

# === Agente 3: Gerador de Casos BDD ===
bdd_agent = Agent(
    model=llm,
    description=(
        "Você é um Especialista em QA focado em escrever cenários no formato BDD. "
        "Transforme histórias de usuário, critérios de aceite e regras de negócio em cenários Given / When / Then."
    ),
    tools=[DuckDuckGoTools()],
    show_tool_calls=False,
    markdown=True,
)

# === Menu interativo ===
def main():
    print("=== Bem-vindo ao Agente QA ===")
    print("Escolha o agente para conversar:")
    print("1 - Validador de Testes")
    print("2 - Complementador de Testes")
    print("3 - Gerador de Casos BDD")
    print("0 - Sair")

    while True:
        escolha = input("\nDigite sua escolha: ")

        if escolha == "1":
            prompt = input("Digite sua pergunta para o Validador de Testes:\n> ")
            validador_agent.print_response(prompt)
        elif escolha == "2":
            prompt = input("Digite sua pergunta para o Complementador de Testes:\n> ")
            complementador_agent.print_response(prompt)
        elif escolha == "3":
            prompt = input("Digite sua pergunta para o Gerador de Casos BDD:\n> ")
            bdd_agent.print_response(prompt)
        elif escolha == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
