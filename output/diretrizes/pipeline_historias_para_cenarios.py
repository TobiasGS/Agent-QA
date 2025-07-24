from agents.bdd_knowledge_agent import AgenteBaseConhecimento
from utils.arquivo import salvar_arquivo, ler_arquivo
from utils.arquivo import salvar_arquivo
import os
from agents.gerador_bdd import AgenteGeradorCenarios


# 1. Ler história de usuário
caminho_historia = "historias/Historia de Usuário.docx"
historia = ler_arquivo(caminho_historia)

# 2. Ler diretrizes previamente geradas
caminho_diretrizes = "output/diretrizes/diretrizes_mais_recente.md"
diretrizes = ler_arquivo(caminho_diretrizes)

# 3. Prompt com história e diretrizes
prompt = f"""
Utilize as seguintes diretrizes para gerar os cenários BDD da história abaixo:

Diretrizes:
{diretrizes}

História:
{historia}
"""

# 4. Geração de cenários
agente = AgenteGeradorCenarios()
cenarios_gerados = agente.executar(prompt)

# 5. Salvar cenários
salvar_arquivo(cenarios_gerados, "output/resultados/cenarios_gerados.md")
