import pandas as pd

def preencher_planilha_com_cenarios(cenarios, caminho_modelo, caminho_saida):
    df = pd.read_csv(caminho_modelo)

    novos_cenarios = []
    for i, c in enumerate(cenarios, 1):
        novos_cenarios.append({
            "ID do Cenário": i,
            "Título": c.get("titulo", "Título do cenário"),
            "Resumo": c.get("resumo", ""),  # se não houver, você pode usar o título ou funcionalidade
            "Pré-Condições": c.get("precondicoes", ""),
            "Passos para Execução": "\n".join(c.get("passos", [])),
            "Dados do Teste": c.get("dados_teste", ""),  # você pode ajustar se tiver dados específicos
            "Resultado Esperado": c.get("resultado_esperado", ""),
            "Status": "",  # deixar em branco para preenchimento manual depois
            "Observações/Evidências": "",
            "Requisito Associado": c.get("requisito", ""),  # se tiver
            "Executor": "",
            "Responsável": "",
            "Data de Execução": ""
        })

    df_novo = pd.DataFrame(novos_cenarios)
    df_novo.to_csv(caminho_saida, index=False, encoding='utf-8-sig')
    print(f"[LOG] Planilha preenchida com sucesso em {caminho_saida}")
