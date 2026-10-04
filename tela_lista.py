"""Tela 1: exibição e conclusão das tarefas."""

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class TelaLista(QWidget):
    """Lista as tarefas e permite mudar seu status diretamente."""

    pedir_adicao = pyqtSignal()

    def __init__(self, repositorio, parent=None):
        super().__init__(parent)
        self.repositorio = repositorio
        self._atualizando = False
        self._montar_interface()
        self.atualizar_lista()

    def _montar_interface(self):
        titulo = QLabel("Tela 1 - Minhas tarefas")
        titulo.setObjectName("tituloTela")

        legenda = QLabel("Marque a caixa para concluir uma tarefa.")
        legenda.setObjectName("legenda")

        self.lista = QListWidget()

        botao_adicionar = QPushButton("Abrir Tela 2 - Adicionar tarefa")
        botao_adicionar.clicked.connect(self.pedir_adicao.emit)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(12)
        layout.addWidget(titulo)
        layout.addWidget(legenda)
        layout.addWidget(self.lista)
        layout.addWidget(botao_adicionar)

    def atualizar_lista(self):
        self._atualizando = True
        self.lista.clear()
        for indice, tarefa in enumerate(self.repositorio.tarefas):
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, indice)
            self.lista.addItem(item)
            linha = LinhaTarefa(tarefa)
            linha.status_alterado.connect(
                lambda concluida, item=item, linha=linha: self._alterar_status(
                    item, linha, concluida
                )
            )
            item.setSizeHint(linha.sizeHint())
            self.lista.setItemWidget(item, linha)
        self._atualizando = False

    def _alterar_status(self, item, linha, concluida):
        if self._atualizando:
            return
        indice = item.data(Qt.ItemDataRole.UserRole)
        self.repositorio.alternar_concluida(indice, concluida)
        linha.aplicar_status(concluida)


class RotuloClicavel(QLabel):
    """Título que mantém o mesmo comportamento de clique do checkbox."""

    clicado = pyqtSignal()

    def mousePressEvent(self, evento):
        if evento.button() == Qt.MouseButton.LeftButton:
            self.clicado.emit()
        super().mousePressEvent(evento)


class LinhaTarefa(QWidget):
    """Linha visual com checkbox centralizado e status explícito."""

    status_alterado = pyqtSignal(bool)

    def __init__(self, tarefa, parent=None):
        super().__init__(parent)
        self.checkbox = QCheckBox()
        self.checkbox.setAccessibleName(tarefa["titulo"])
        self.checkbox.setChecked(tarefa["concluida"])
        self.checkbox.setFixedWidth(32)
        self.checkbox.setMinimumHeight(36)
        self.checkbox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.checkbox.stateChanged.connect(self._emitir_status)

        self.titulo = RotuloClicavel(tarefa["titulo"])
        self.titulo.setObjectName("tituloTarefa")
        self.titulo.setMinimumHeight(36)
        self.titulo.setWordWrap(True)
        self.titulo.setCursor(Qt.CursorShape.PointingHandCursor)
        self.titulo.clicado.connect(self.checkbox.click)

        self.descricao = QLabel(tarefa["descricao"])
        self.descricao.setObjectName("descricaoTarefa")
        self.descricao.setWordWrap(True)
        self.descricao.setVisible(bool(tarefa["descricao"]))
        self.descricao.setToolTip(tarefa["descricao"])

        self.status = QLabel()
        self.status.setMinimumWidth(124)
        self.status.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        texto = QVBoxLayout()
        texto.setContentsMargins(0, 0, 0, 0)
        texto.setSpacing(6)
        texto.addWidget(self.titulo)
        texto.addWidget(self.descricao)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(18, 10, 24, 10)
        layout.setSpacing(12)
        layout.addWidget(self.checkbox, 0, Qt.AlignmentFlag.AlignTop)
        layout.addLayout(texto, 1)
        layout.addWidget(self.status)
        self.aplicar_status(tarefa["concluida"])

    def _emitir_status(self, estado):
        self.status_alterado.emit(estado == Qt.CheckState.Checked.value)

    def aplicar_status(self, concluida):
        fonte = QFont(self.titulo.font())
        fonte.setStrikeOut(concluida)
        self.titulo.setFont(fonte)
        self.titulo.setStyleSheet(
            "color: %s; font-size: 16px;" % ("#6b7280" if concluida else "#172033")
        )
        self.checkbox.setStyleSheet(
            "QCheckBox { padding: 0px; }"
            "QCheckBox::indicator:unchecked { width: 26px; height: 26px; "
            "border: 2px solid #8b9bad; border-radius: 6px; "
            "background: #ffffff; }"
            "QCheckBox::indicator:checked { "
            "width: 26px; height: 26px; }"
        )
        self.status.setText("Concluída" if concluida else "Pendente")
        self.status.setStyleSheet(
            "color: %s; font-weight: 600; font-size: 13px;"
            % ("#228b68" if concluida else "#607086")
        )
