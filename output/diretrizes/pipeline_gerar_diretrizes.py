from agents.bdd_knowledge_agent import gerar_diretrizes_bdd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils.arquivo import salvar_arquivo
from utils.texto import juntar_arquivos_em_pasta
from datetime import datetime

# 1. Carrega base de conhecimento
conteudo_base = juntar_arquivos_em_pasta("base_de_conhecimento")

# 2. Gera diretrizes
resposta = gerar_diretrizes_bdd(conteudo_base)

# 3. Salva arquivo
timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
nome_base = f"diretrizes_{timestamp}.md"
caminho_saida = os.path.join("output", "diretrizes", nome_base)
salvar_arquivo(resposta, caminho_saida)

print(f"✅ Diretrizes geradas e salvas em: {caminho_saida}")
