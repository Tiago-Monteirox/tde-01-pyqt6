# TDE 1 — organização do grupo e do vídeo

## Base do trabalho

Fonte: `TDE 1 - Interface Gráfica Python - 2026-02.pdf` (4 páginas).

- Grupo com cinco integrantes, conforme informado pelo líder.
- Apresentação em vídeo, conforme informado pelo líder. O enunciado original descreve apresentação ao vivo; o roteiro adapta a execução e a explicação do código para uma gravação.
- Limite de 12 minutos. Meta do roteiro: 11min30s, com 30s de margem.
- Biblioteca confirmada: PyQt6. No PDF, “Thiago” aparece no grupo 02.
- Prazo: consultar o Teams. O PDF não informa uma data.

## Entregáveis

1. Aplicativo Python de lista de tarefas com duas telas funcionando.
2. Arquivos `.py` com nomes claros e código organizado e comentado.
3. Slides de apoio à explicação, solicitados pelo grupo; são opcionais no enunciado.
4. Vídeo com a participação dos cinco integrantes, incluindo aplicativo em execução e código no editor.
5. Instruções de instalação e execução para facilitar a reprodução pelo grupo.

## Divisão proposta

As pessoas abaixo são posições a preencher com os nomes reais. Cada integrante deve entender sua implementação e conseguir explicar suas decisões.

| Integrante | Responsabilidade de preparação | Parte no vídeo | Tempo |
| --- | --- | --- | --- |
| 1 — líder | Coordenar integração, revisar requisitos e reunir as gravações | Abrir a apresentação; explicar o que é a biblioteca, mantenedor, origem, propósito e usos | 0:00–2:00 |
| 2 | Preparar instalação e exemplo mínimo executável | Mostrar instalação, importações, primeira janela/tela e organização de widgets, layouts e eventos | 2:00–4:00 |
| 3 | Implementar a tela da lista e a conclusão de tarefas | Demonstrar a Tela 1 e explicar seu código e seus componentes | 4:00–6:30 |
| 4 | Implementar cadastro, validação e navegação de retorno | Demonstrar a Tela 2 e explicar seu código, Salvar e Cancelar | 6:30–9:00 |
| 5 | Verificar os fluxos, pesquisar limitações e organizar referências | Mostrar casos de validação; explicar vantagens, desvantagens, quando usar e onde aprender | 9:00–11:30 |

O líder coordena, mas as tarefas de implementação e a fala ficam distribuídas. O PDF prevê avaliação parcialmente individual e desconto para membros que não participam.

## Requisitos funcionais do aplicativo

Armazenamento exclusivamente em memória: uma lista de dicionários Python. Sem banco de dados ou arquivo de tarefas; ao encerrar, os dados podem desaparecer.

Exemplo de estrutura a compartilhar entre as telas:

```python
tarefas = [
    {
        "titulo": "Revisar a apresentação",
        "descricao": "Ensaiar a explicação das duas telas",
        "concluida": False,
    }
]
```

O exemplo ilustra o formato dos dados; não exige que o aplicativo comece com uma tarefa cadastrada.

### Tela 1 — tarefas cadastradas

- Exibir todas as tarefas, com título e status.
- Permitir concluir uma tarefa diretamente na lista.
- Diferenciar visualmente pendentes e concluídas, incluindo texto de status.
- Disponibilizar navegação para a tela de adicionar tarefa.

### Tela 2 — adicionar tarefa

- Campo de título obrigatório.
- Campo de descrição opcional.
- Salvar adiciona um dicionário à lista compartilhada e retorna à Tela 1 atualizada.
- Cancelar descarta os dados digitados e retorna sem criar uma tarefa.
- Rejeitar título vazio. Usar `strip()` para também rejeitar apenas espaços.

## Sequência dos slides

1. Título: “Lista de tarefas com PyQt6”, integrantes e objetivo.
2. PyQt6 em uma frase: bindings Python para Qt, desktop multiplataforma e widgets nativos.
3. Instalação e primeira janela: `uv sync`, `uv run app.py`, imports e `QApplication`/`QWidget`.
4. Esqueleto do aplicativo: imports, `JanelaPrincipal`, `QStackedWidget`, sinais e `app.exec()`.
5. Esqueleto de uma tela: herança de `QWidget`, widgets, layout e eventos.
6. Tela 1: lista em memória, checkbox de conclusão, diferenciação visual e navegação.
7. Tela 2: título, descrição, validação, Salvar, Cancelar e retorno à lista.
8. Avaliação crítica: vantagens, limitações e quando escolher ou evitar PyQt6.
9. Como continuar aprendendo: documentação oficial, exemplos e fontes usadas.

As falas e os tempos ficam no roteiro e nas notas dos slides. Durante a demonstração, gravar o aplicativo e o editor com texto legível. As duas telas precisam ser executadas e ter seu código explicado.

## Sequência de demonstração

1. Abrir o aplicativo e mostrar a lista inicialmente vazia.
2. Abrir o cadastro e tentar salvar com o título vazio; mostrar a validação.
3. Cadastrar uma tarefa com título e descrição e mostrar o retorno à lista.
4. Cadastrar outra tarefa sem descrição, evidenciando que o campo é opcional.
5. Marcar uma tarefa como concluída e mostrar a diferença de status e aparência.
6. Iniciar outro cadastro e cancelar; mostrar que nenhuma tarefa foi adicionada.
7. No editor, explicar os trechos das duas telas, a lista de dicionários e os eventos.

## Verificação e gravação

- Testar o aplicativo em dois computadores diferentes, como exige o PDF.
- Confirmar título vazio e título com apenas espaços.
- Confirmar cadastro com e sem descrição, conclusão, navegação e cancelamento.
- Confirmar que as duas telas compartilham a mesma lista de tarefas.
- Ensaiar as falas e medir a duração final, incluindo transições.
- Cada integrante grava sua parte em ordem; as partes com demonstração incluem captura do aplicativo e do editor.
- Conferir áudio, legibilidade do código e participação dos cinco integrantes no vídeo final.
- Consultar o Teams para o prazo e as instruções atualizadas de envio do vídeo.

## Critérios de avaliação do PDF

| Critério | Pontos |
| --- | ---: |
| Domínio técnico | 2,5 |
| Qualidade do código | 2,0 |
| Demonstração das duas telas | 2,5 |
| Análise crítica | 1,5 |
| Didática e clareza | 1,0 |
| Tempo e organização | 0,5 |
| Total | 10,0 |

## Informações que faltam

- Preencher os nomes dos cinco integrantes antes da entrega; até lá, usar as posições da divisão proposta.
- Consultar o prazo no Teams.

## Roteiro de fala para a gravação

### Integrante 1 — abertura e contexto (0:00–2:00)

“Olá, somos o grupo ___ e neste vídeo vamos apresentar o PyQt6 por meio de um aplicativo de lista de tarefas. PyQt6 é o conjunto de bindings Python para o framework Qt. Ele permite construir aplicações gráficas de desktop com widgets, layouts e eventos, mantendo acesso ao ecossistema Qt. O projeto resolve o problema de criar interfaces multiplataforma sem abandonar Python. Hoje vamos mostrar a instalação, a estrutura das telas, o código e a execução.”

### Integrante 2 — instalação e estrutura (2:00–4:00)

“Usamos `uv` para reproduzir o ambiente: `uv sync` instala as dependências do `pyproject.toml` conforme o `uv.lock`, e `uv run app.py` executa o programa no ambiente correto. O esqueleto começa pelos imports e pela criação de `QApplication`, que inicializa o ambiente e mantém o loop de eventos. Depois definimos `JanelaPrincipal`, criamos o repositório e as duas telas, colocamos ambas em um `QStackedWidget` e definimos essa pilha como conteúdo central. No final, `show()` exibe a janela e `app.exec()` inicia o loop. Dentro de cada tela, os widgets entram em um layout e a comunicação acontece por sinais, como `clicked` e os sinais próprios `salvou`, `cancelou` e `pedir_adicao`.”

### Integrante 3 — Tela 1 (4:00–6:30)

“A Tela 1 usa um `QListWidget` para organizar as linhas, mas cada linha é um `LinhaTarefa` com seu próprio `QCheckBox`. Assim o checkbox fica centralizado e o status aparece ao lado. O índice do item é guardado no `QListWidgetItem` e usado para atualizar o dicionário correspondente. Quando a tarefa é concluída, emitimos `status_alterado`, aplicamos texto riscado e mudamos a cor. O botão de adicionar emite um sinal que leva à Tela 2.”

### Integrante 4 — Tela 2 (6:30–9:00)

“A Tela 2 usa `QLineEdit` para o título e `QTextEdit` para a descrição opcional. Antes de salvar, removemos espaços e rejeitamos título vazio com uma mensagem de validação. Com um título válido, o repositório adiciona um dicionário com título, descrição e status pendente. O sinal `salvou` atualiza a lista e volta à Tela 1. Cancelar limpa os campos e retorna sem alterar os dados.”

### Integrante 5 — demonstração e análise (9:00–11:30)

“Agora demonstramos o fluxo completo: lista vazia, tentativa inválida, cadastro com descrição, cadastro sem descrição, conclusão direta e cancelamento. Como vantagem, PyQt6 oferece muitos widgets, layouts maduros, documentação do Qt e aplicações desktop multiplataforma. Como limites, a distribuição costuma exigir mais cuidado que uma aplicação web simples, a instalação é maior e a licença deve ser avaliada conforme o projeto. Indicamos a documentação oficial do Riverbank e os exemplos de Qt como caminho para aprofundar.”

### Encerramento (11:30–12:00)

“Com isso mostramos a biblioteca, a estrutura, as duas telas, o código e os principais trade-offs. Obrigado.”
