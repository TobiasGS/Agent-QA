from dotenv import load_dotenv
import google.generativeai as genai
import os

# Carrega as variáveis de ambiente do .env (incluindo GEMINI_API_KEY)
load_dotenv()

# Configura a API do Gemini com a chave
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Instancia o modelo Gemini
model = genai.GenerativeModel("gemini-2.5-pro")

# Função para gerar diretrizes a partir da base de conhecimento
def gerar_diretrizes_bdd(textos_base_conhecimento):
    prompt = (
        "Você é um Especialista em QA.\n"
        "Com base na seguinte base de conhecimento técnica, gere diretrizes para escrever cenários BDD:\n\n"
        f"{textos_base_conhecimento}"
    )

    # Gera a resposta com o modelo Gemini
    resposta = model.generate_content(prompt)

    # Retorna o texto da resposta
    return resposta.text if hasattr(resposta, "text") else str(resposta)
