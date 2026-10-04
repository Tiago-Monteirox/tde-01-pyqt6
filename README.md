# Lista de tarefas com PyQt6

Aplicação desktop do TDE 1 de Programação em Python. O projeto possui uma tela para listar/concluir tarefas e outra para cadastrar título e descrição.

## Como rodar

Requisitos: Python 3.14 e [uv](https://docs.astral.sh/uv/).

```bash
git clone <URL_DO_REPOSITORIO>
cd tde-01
uv sync
uv run app.py
```

Se o ambiente virtual já existir com outra versão do Python, recrie-o:

```bash
uv venv --clear --python 3.14
uv sync
uv run app.py
```

O `uv.lock` fixa as versões das dependências. No macOS, o aplicativo prepara automaticamente o caminho dos plugins do Qt.

## Estrutura

- `app.py`: janela principal e navegação entre as telas.
- `modelo_tarefas.py`: repositório das tarefas em memória.
- `tela_lista.py`: listagem, descrição e conclusão das tarefas.
- `tela_adicionar.py`: formulário de cadastro.
- `saida_slides/`: apresentação do trabalho.
