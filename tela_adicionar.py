"""Tela 2: cadastro de uma nova tarefa."""

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class TelaAdicionar(QWidget):
    """Formulário para adicionar uma tarefa ao repositório em memória."""

    salvou = pyqtSignal()
    cancelou = pyqtSignal()

    def __init__(self, repositorio, parent=None):
        super().__init__(parent)
        self.repositorio = repositorio
        self._montar_interface()

    def _montar_interface(self):
        titulo = QLabel("Tela 2 - Adicionar tarefa")
        titulo.setObjectName("tituloTela")

        legenda = QLabel("Preencha os dados. Cancelar retorna para a Tela 1.")
        legenda.setObjectName("legenda")

        self.campo_titulo = QLineEdit()
        self.campo_titulo.setPlaceholderText("Ex.: revisar o roteiro")

        self.campo_descricao = QTextEdit()
        self.campo_descricao.setPlaceholderText("Detalhes opcionais")
        self.campo_descricao.setFixedHeight(110)

        formulario = QFormLayout()
        formulario.addRow("Título *", self.campo_titulo)
        formulario.addRow("Descrição", self.campo_descricao)

        botao_cancelar = QPushButton("Cancelar (Tela 1)")
        botao_salvar = QPushButton("Salvar")
        botao_cancelar.clicked.connect(self.cancelar)
        botao_salvar.clicked.connect(self.salvar)

        botoes = QHBoxLayout()
        botoes.addStretch()
        botoes.addWidget(botao_cancelar)
        botoes.addWidget(botao_salvar)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(18)
        layout.addWidget(titulo)
        layout.addWidget(legenda)
        layout.addLayout(formulario)
        layout.addLayout(botoes)

    def salvar(self):
        titulo = self.campo_titulo.text().strip()
        if not titulo:
            QMessageBox.warning(
                self,
                "Título obrigatório",
                "Digite um título antes de salvar a tarefa.",
            )
            self.campo_titulo.setFocus()
            return

        self.repositorio.adicionar(titulo, self.campo_descricao.toPlainText())
        self.campo_titulo.clear()
        self.campo_descricao.clear()
        self.salvou.emit()

    def cancelar(self):
        self.campo_titulo.clear()
        self.campo_descricao.clear()
        self.cancelou.emit()
