"""Aplicativo de lista de tarefas demonstrado no TDE 1."""

import os
import stat
import sys
from pathlib import Path

from PyQt6.QtCore import QCoreApplication, QLibraryInfo, Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QStackedWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

ESTILO = """
QMainWindow, QWidget { background: #f7f9fc; color: #172033; }
#linhaTarefa { background: #f7f9fc; }
#linhaTarefa QLabel { background: transparent; }
#linhaTarefa QCheckBox { padding: 0px; }
#linhaTarefa QCheckBox::indicator { width: 26px; height: 26px; }
#linhaTarefa QCheckBox::indicator:unchecked {
    border: 2px solid #8b9bad; border-radius: 6px; background: #ffffff;
}
#tituloTela { color: #143d66; font-size: 26px; font-weight: 700; }
#legenda { color: #65758b; }
#descricaoTarefa { color: #607086; font-size: 13px; }
QLineEdit, QTextEdit, QListWidget {
    background: white; border: 1px solid #c9d3df; border-radius: 6px;
    padding: 8px; font-size: 14px;
}
QListWidget { padding: 4px; }
QListWidget::item { padding: 0px; border-bottom: 1px solid #e1e7ee; }
QListWidget::item:selected { background: #f7fafd; color: #172033; }
QPushButton {
    background: #1f6aa5; color: white; border: none;
    border-radius: 6px; padding: 10px 16px; font-weight: 600;
}
QPushButton:hover { background: #174f7c; }
"""


def _preparar_plugins_qt():
    """Garante que o macOS consiga enxergar os plugins instalados pelo uv."""
    if sys.platform != "darwin":
        return

    plugin_root = Path(QLibraryInfo.path(QLibraryInfo.LibraryPath.PluginsPath))
    hidden_flag = getattr(stat, "UF_HIDDEN", 0)
    if not plugin_root.exists() or not hidden_flag:
        return

    # Alguns ambientes do macOS marcam o .venv inteiro como hidden. O Qt
    # ignora plugins com essa flag, então removemos apenas a flag visual.
    for caminho in (plugin_root, *plugin_root.rglob("*")):
        try:
            flags = os.stat(caminho).st_flags
            os.chflags(caminho, flags & ~hidden_flag)
        except OSError:
            pass

    QCoreApplication.addLibraryPath(str(plugin_root))


class LinhaTarefa(QWidget):
    """Linha visual com checkbox centralizado e status explícito."""

    def __init__(self, tarefa, parent=None):
        super().__init__(parent)
        self.setObjectName("linhaTarefa")
        self.tarefa = tarefa

        self.checkbox = QCheckBox()
        self.checkbox.setAccessibleName(tarefa["titulo"])
        self.checkbox.setChecked(tarefa["concluida"])
        self.checkbox.setFixedWidth(32)
        self.checkbox.setMinimumHeight(36)
        self.checkbox.setCursor(Qt.CursorShape.PointingHandCursor)
        self.checkbox.toggled.connect(self.aplicar_status)

        self.titulo = QLabel(tarefa["titulo"])
        self.titulo.setMinimumHeight(36)
        self.titulo.setWordWrap(True)
        self.titulo.setCursor(Qt.CursorShape.PointingHandCursor)

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

    def mousePressEvent(self, evento):
        """Clique no título alterna a tarefa, igual ao clique no checkbox."""
        ponto = evento.position().toPoint()
        if evento.button() == Qt.MouseButton.LeftButton and self.titulo.geometry().contains(ponto):
            self.checkbox.click()
        super().mousePressEvent(evento)

    def aplicar_status(self, concluida):
        self.tarefa["concluida"] = concluida
        self.titulo.setStyleSheet(
            "font-size: 16px; color: #6b7280; text-decoration: line-through;"
            if concluida
            else "font-size: 16px; color: #172033;"
        )
        self.status.setText("Concluída" if concluida else "Pendente")
        self.status.setStyleSheet(
            "font-weight: 600; font-size: 13px; color: %s"
            % ("#228b68" if concluida else "#607086")
        )


class TelaLista(QWidget):
    """Tela 1: lista as tarefas e permite mudar seu status diretamente."""

    pedir_adicao = pyqtSignal()

    def __init__(self, tarefas, parent=None):
        super().__init__(parent)
        self.tarefas = tarefas

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
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista.clear()
        for tarefa in self.tarefas:
            linha = LinhaTarefa(tarefa)
            item = QListWidgetItem()
            item.setSizeHint(linha.sizeHint())
            self.lista.addItem(item)
            self.lista.setItemWidget(item, linha)


class TelaAdicionar(QWidget):
    """Tela 2: formulário que acrescenta uma tarefa à lista em memória."""

    salvou = pyqtSignal()
    cancelou = pyqtSignal()

    def __init__(self, tarefas, parent=None):
        super().__init__(parent)
        self.tarefas = tarefas

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

        self.tarefas.append(
            {
                "titulo": titulo,
                "descricao": self.campo_descricao.toPlainText().strip(),
                "concluida": False,
            }
        )
        self.campo_titulo.clear()
        self.campo_descricao.clear()
        self.salvou.emit()

    def cancelar(self):
        self.campo_titulo.clear()
        self.campo_descricao.clear()
        self.cancelou.emit()


class JanelaPrincipal(QMainWindow):
    """Coordena a navegação entre as duas telas."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de tarefas - PyQt6")
        self.setMinimumSize(560, 440)

        tarefas = []
        self.tela_lista = TelaLista(tarefas)
        self.tela_adicionar = TelaAdicionar(tarefas)

        self.paginas = QStackedWidget()
        self.paginas.addWidget(self.tela_lista)
        self.paginas.addWidget(self.tela_adicionar)
        self.setCentralWidget(self.paginas)

        self.tela_lista.pedir_adicao.connect(self.mostrar_adicao)
        self.tela_adicionar.salvou.connect(self.mostrar_lista)
        self.tela_adicionar.cancelou.connect(self.mostrar_lista)

    def mostrar_adicao(self):
        self.paginas.setCurrentWidget(self.tela_adicionar)
        self.tela_adicionar.campo_titulo.setFocus()

    def mostrar_lista(self):
        self.tela_lista.atualizar_lista()
        self.paginas.setCurrentWidget(self.tela_lista)


def main():
    _preparar_plugins_qt()
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    janela = JanelaPrincipal()
    janela.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()













