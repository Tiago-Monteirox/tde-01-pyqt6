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

As pessoas abaixo são posições a preencher com os nomes reais. Cada integrante deve conhecer sua parte e conseguir explicar sua participação; a explicação detalhada do código fica com o líder.

| Integrante | Responsabilidade de preparação | Parte no vídeo | Tempo |
| --- | --- | --- | --- |
| 1 — líder | Coordenar integração, revisar requisitos e reunir as gravações | Explicar todo o código, do `app.py` às duas telas, ao modelo e aos sinais | 3:00–7:15 e encerramento |
| 2 | Preparar contexto e objetivo do trabalho | Fazer a abertura e explicar o que é o PyQt6 e onde ele faz sentido | 0:00–1:30 |
| 3 | Preparar instalação e exemplo mínimo executável | Mostrar o uso do `uv`, a execução e o fluxo geral do aplicativo | 1:30–3:00 |
| 4 | Verificar os fluxos das duas telas | Demonstrar cadastro, descrição, conclusão e cancelamento, sem explicar código | 7:15–9:30 |
| 5 | Pesquisar limitações e organizar referências | Apresentar análise crítica, fontes e próximos passos | 9:30–11:15 |

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

O roteiro completo, com as falas prontas e as transições entre os integrantes, está em [`ROTEIRO_APRESENTACAO.md`](ROTEIRO_APRESENTACAO.md). A versão atual deixa toda a explicação do código com o líder e distribui entre os demais integrantes o contexto, a instalação, a demonstração e a análise crítica.
