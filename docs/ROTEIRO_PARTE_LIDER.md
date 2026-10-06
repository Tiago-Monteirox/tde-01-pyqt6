# Roteiro da parte do líder — arquitetura e estrutura básica

**Objetivo:** explicar o item 3.3 mostrando janelas, widgets, layouts, eventos e o esqueleto de uma tela PyQt6.

**Duração:** aproximadamente 5 minutos.

**Como gravar:** abra somente o `app.py` e siga o arquivo de cima para baixo. As referências abaixo já estão atualizadas para a versão em arquivo único.

## 1. Abertura e esqueleto mínimo (30 s)

**Fala:**

> “Vou explicar como a nossa interface foi organizada em PyQt6. O projeto agora está concentrado no `app.py`: os widgets formam as telas, os layouts posicionam os componentes e os sinais conectam as ações do usuário.”

Mostre este esqueleto curto:

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
janela = QWidget()
janela.show()
sys.exit(app.exec())
```

**Fala:**

> “`QApplication` prepara o ambiente gráfico e controla o loop de eventos. `QWidget` é a base de uma tela. `show()` exibe a janela, e `app.exec()` aguarda cliques, digitação e outros eventos. No projeto real, usamos classes próprias que herdam de `QWidget` e uma janela principal baseada em `QMainWindow`.”

## 2. Imports, estilo e preparação do Qt — `app.py:3–73` (30 s)

Role até `app.py:3–25`.

**Fala:**

> “No início ficam os imports. Aqui estão os widgets usados na demonstração: `QLabel`, `QPushButton`, `QCheckBox`, `QLineEdit`, `QTextEdit`, `QListWidget` e os layouts vertical, horizontal e de formulário. Também importamos `pyqtSignal`, que permite uma parte da interface avisar outra quando algo acontece.”

Mostre `ESTILO` em `app.py:27–51`.

> “`ESTILO` concentra o visual da aplicação: cores, bordas, espaçamentos e tamanho do checkbox. Ele é aplicado uma única vez no início e não interfere na separação entre telas e eventos.”

Passe rapidamente por `_preparar_plugins_qt` em `app.py:54–73`.

> “Esse helper trata a localização dos plugins do Qt no macOS quando o projeto é executado com uv. Ele é uma configuração de ambiente; a lógica da interface começa na próxima classe.”

## 3. Linha visual de uma tarefa — `LinhaTarefa` (`app.py:76–139`) (1 min)

Mostre `LinhaTarefa` em `app.py:76–139`.

**Fala:**

> “`LinhaTarefa` herda de `QWidget` e representa uma tarefa. No construtor (`app.py:79–119`), criamos o checkbox, os textos e o status. Título e descrição ficam em um `QVBoxLayout` (`app.py:107–111`); esse bloco, o checkbox e o status ficam lado a lado em um `QHBoxLayout` (`app.py:113–119`).”

Mostre o trecho do evento:

```python
self.checkbox.toggled.connect(self.aplicar_status)
```

> “O sinal `toggled` chama `aplicar_status` (`app.py:128–139`), que atualiza o status e risca o título quando necessário. `mousePressEvent` (`app.py:121–126`) permite fazer a mesma alternância clicando no título.”

## 4. Tela 1: lista de tarefas — `TelaLista` (`app.py:142–179`) (1 min)

Mostre `TelaLista` em `app.py:142–179`.

**Fala:**

> “`TelaLista` é a primeira tela e herda de `QWidget`. O sinal `pedir_adicao` (`app.py:145`) abre o formulário. No construtor (`app.py:147–169`), `QLabel`, `QListWidget` e `QPushButton` são organizados por um `QVBoxLayout`.”

Agora mostre `atualizar_lista` em `app.py:171–178`.

> “`atualizar_lista` limpa a lista e, para cada tarefa, cria uma `LinhaTarefa` (`app.py:76–139`) dentro de um `QListWidgetItem`. Assim, cada item recebe sua própria linha visual.”

## 5. Tela 2: cadastro — `TelaAdicionar` (`app.py:181–251`) (1 min)

Mostre `TelaAdicionar` em `app.py:181–251`.

**Fala:**

> “`TelaAdicionar` é o formulário da segunda tela. Os sinais `salvou` e `cancelou` (`app.py:184–185`) avisam à janela principal. No construtor (`app.py:187–224`), `QLineEdit`, `QTextEdit`, `QFormLayout` e `QPushButton` montam o formulário.”

Mostre `salvar` em `app.py:226–246`.

> “`salvar` (`app.py:226–246`) valida o título; se estiver vazio, mostra `QMessageBox.warning`. Caso contrário, acrescenta o dicionário à lista, limpa os campos e emite `salvou`. `cancelar` (`app.py:248–251`) apenas limpa e emite `cancelou`.”

## 6. Janela principal e navegação — `JanelaPrincipal` (`app.py:254–281`) (1 min)

Mostre `JanelaPrincipal` em `app.py:254–281`.

**Fala:**

> “`JanelaPrincipal` é o contêiner geral. No construtor (`app.py:257–273`), a mesma lista `tarefas` é compartilhada por `TelaLista` (`app.py:142–179`) e `TelaAdicionar` (`app.py:181–251`). O `QStackedWidget` (`app.py:266–269`) guarda as duas telas, e os sinais chamam `mostrar_adicao` (`app.py:275–277`) ou `mostrar_lista` (`app.py:279–281`).”

## 7. Inicialização e fechamento (40 s)

Mostre `main` em `app.py:284–290` e o bloco final em `app.py:293–294`.

**Fala:**

> “`main` (`app.py:284–290`) prepara os plugins, cria `QApplication`, aplica `ESTILO`, instancia `JanelaPrincipal`, mostra a janela e inicia `app.exec()`. O bloco final (`app.py:293–294`) chama `main` quando executamos `uv run app.py`.”

Mostre a aplicação funcionando, abra a Tela 2, salve uma tarefa e marque o checkbox.

> “`QMainWindow` contém as telas; os widgets exibem e recebem ações; os layouts organizam a interface; e os sinais conectam os eventos. Mesmo em um único arquivo, cada classe mantém uma responsabilidade clara.”

### Checklist antes de gravar

- Abrir apenas `app.py` e seguir as seções na ordem.
- Mostrar a referência de linha antes de cada classe ou método.
- Demonstrar abrir a Tela 2, salvar uma tarefa e marcar o checkbox.
- Manter o código legível e terminar em cerca de 4–5 minutos.
