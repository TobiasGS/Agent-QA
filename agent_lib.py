class Agent:
    def __init__(self, model, description, markdown=False):
        self.model = model
        self.description = description
        self.markdown = markdown

    def run(self, prompt):
        # Aqui você implementa a chamada ao modelo
        return {"text": f"Simulação de resposta para: {prompt}"}