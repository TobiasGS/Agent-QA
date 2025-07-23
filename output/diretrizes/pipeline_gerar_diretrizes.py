from app.agentes.agente_base_conhecimento import AgenteBaseConhecimento
from app.utils.arquivo import salvar_arquivo
from app.utils.texto import juntar_arquivos_em_pasta
from datetime import datetime
import os

# 1. Carregar a base de conhecimento (como já faz atualmente)
conteudo_base = juntar_arquivos_em_pasta("base_de_conhecimento")

# 2. Inicializa o agente
agente = AgenteBaseConhecimento()

# 3. Gera diretrizes
resposta = agente.executar(conteudo_base)

# 4. Salvar diretrizes
timestamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
nome_base = f"diretrizes_{timestamp}.md"
caminho_saida = os.path.join("output", "diretrizes", nome_base)
salvar_arquivo(resposta, caminho_saida)

print(f"✅ Diretrizes geradas e salvas em: {caminho_saida}")
