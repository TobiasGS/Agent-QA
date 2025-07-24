from typing import List
import requests
from langchain_core.embeddings import Embeddings

class GroqEmbeddings(Embeddings):
    def __init__(self, api_key: str, model: str = "text-embedding-3-small"):
        self.api_key = api_key
        self.model = model

    def embed_query(self, text: str) -> List[float]:
        return self._embed([text])[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embed(texts)

    def _embed(self, texts: List[str]) -> List[List[float]]:
        try:
            url = "https://api.groq.com/openai/v1/embeddings"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": self.model,
                "input": texts
            }
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            return [item["embedding"] for item in data["data"]]
        except requests.exceptions.RequestException as e:
            print(f"Erro ao fazer requisição: {e}")
            return None

vetores = GroqEmbeddings("sua_api_key").embed_documents(["texto1", "texto2"])
if vetores is not None:
    vetor_dim = len(vetores[0])
    print(vetor_dim)
else:
    print("Erro ao obter vetores")