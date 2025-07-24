from typing import List
import requests
from langchain_core.embeddings import Embeddings

class GroqEmbeddings(Embeddings):
    def __init__(self, api_key: str, model: str = "nomic-embed-text-v1"):
        self.api_key = api_key
        self.model = model

    def embed_query(self, text: str) -> List[float]:
        return self._embed([text])[0]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._embed(texts)

    def _embed(self, texts: List[str]) -> List[List[float]]:
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
