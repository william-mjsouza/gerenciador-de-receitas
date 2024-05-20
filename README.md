# Sistema de Gerenciamento de Receitas

## Índice
- Descrição
- Requisitos
- Funcionalidades
- Uso
- Fluxograma
- Autores

## Descrição
Este é um sistema de gerenciamento de receitas desenvolvido em Python, que permite ao usuário adicionar, favoritar, visualizar, atualizar e excluir receitas. O sistema também sugere receitas aleatórias, identifica a receita com a menor quantidade de ingredientese e mostrar ao usuário as receitas de um determinado país.

## Requisitos
  Pacotes utilizados:
    - Python 3.12
    - Importação da biblioteca random

## Funcionalidades
### Adicionar Receitas
Permite adicionar novas receitas ao banco de dados.
- Solicita ao usuário o nome da receita, país de origem, ingredientes e modo de preparo.
- O usuário pode optar por marcar uma receita como favorita.

### Visualizar Receitas
- Exibe todas as receitas cadastradas no banco de dados ou somente as favoritas.
- O usuário pode optar por visualizar os detalhes de cada receita, incluindo país de origem, ingredientes e modo de preparo.
- O usuário pode ver as receitas de um determinado país.

### Atualizar Receitas
- Permite ao usuário atualizar as informações de uma ou mais receitas cadastradas.
- Solicita ao usuário os nomes das receitas que deseja atualizar e, em seguida, as novas informações (país de origem, ingredientes e modo de preparo).


### Excluir Receitas
- Permite ao usuário excluir uma ou mais receitas cadastradas.
- Solicita ao usuário os nomes das receitas que deseja excluir e confirmação antes da exclusão.

### Sugerir Receitas
- A função sugerir receitas pode ser usada para sugerir uma receita aleatória do banco de dados.

### Receita com Menor Quantidade de Ingredientes
- Identifica a receita com a menor quantidade de ingredientes cadastrada no banco de dados
- Exibe o nome da receita com a menor quantidade de ingredientes ou os nomes das receitas caso haja empate.

###Favoritar Receitas
- Permite ao usuário marcar uma receita como favorita.
- Solicita ao usuário o nome da receita que deseja favoritar.
## Uso
- Para utilizar este sistema, basta executar o arquivo gerenciador-de-receitas.py em um ambiente Python. O sistema guiará o usuário por meio de menus interativos para realizar as operações desejadas.

## Autores
- Arthur Leal
- Bruno Carvalho
- Thiago De Lavor
- William Souza.






