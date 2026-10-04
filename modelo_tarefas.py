"""Modelo em memória usado pelas duas telas do aplicativo."""


class RepositorioTarefas:
    """Mantém as tarefas durante a execução do programa."""

    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo, descricao=""):
        """Adiciona uma tarefa pendente e retorna o dicionário criado."""
        tarefa = {
            "titulo": titulo.strip(),
            "descricao": descricao.strip(),
            "concluida": False,
        }
        self.tarefas.append(tarefa)
        return tarefa

    def alternar_concluida(self, indice, concluida):
        """Atualiza o status da tarefa indicada."""
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["concluida"] = concluida
