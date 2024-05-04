"""====================================================================================================================
Descrição do Problema:
Rafael é um entusiasta da culinária e adora experimentar novas receitas de diversos países. No entanto, ele enfrenta
dificuldades em organizar suas receitas favoritas e muitas vezes acaba perdendo as que mais gostou. Como um programador
dedicado, você decidiu ajudá-lo a criar um sistema de Gerenciamento de Receitas para que Rafael possa manter o controle
de suas descobertas gastronômicas.

Requisitos funcionais:
1. Cadastro de Receitas: O sistema deve permitir que Rafael cadastre informações sobre cada receita, incluindo nome,
país de origem, ingredientes e modo de preparo.

2. CRUD de Receitas: Rafael deve poder adicionar, visualizar, atualizar e excluir receitas de sua coleção por um menu
interativo.

3. Filtragem por País: O sistema deve permitir a visualização das receitas de acordo com o país de origem, facilitando
a busca por culinárias específicas.

4. Armazenamento em Banco de Dados: Todas as informações sobre as receitas devem ser armazenadas em um banco de dados
para persistirem além da execução do programa (arquivo .txt ou .csv).

5. Lista de Favoritos: Rafael deve poder marcar suas receitas favoritas para acessá-las facilmente em uma lista
separada.

6. Sugestão de Receitas Aleatórias: O sistema deve apresentar uma funcionalidade para sugerir receitas aleatórias de
diferentes países, incentivando Rafael a experimentar novos pratos.

7. Ter pelo menos uma outra funcionalidade a mais que não está descrita aqui neste documento. Sejam criativos e
divirtam-se!

Requisitos não funcionais:
1. Deve ser feito em Python sem o uso de bibliotecas adicionais.
    a. Utilizar a linha de comando para entrada e saída;
    b. Exceções de bibliotecas:
        ■ os ⇾ os.system("clear") ou “cls”.

2. Os dados devem ser salvos em um arquivo no formato .csv ou .txt;
    a. O trabalho deve ser feito em grupo.
    b. Trabalhos que não forem feitos em grupo perderão 50% da nota.

3. O código deve estar organizado, portanto, deve conter:
    a. Funções para dividir o código de forma lógica e evitar repetições;
    b. Tratamento de exceções, para garantir que seu código esteja pronto para tratar casos inesperados;
    c. Legibilidade do código, incluindo nomeação de variáveis e funções.

4. Deve ser feito um manual do usuário, explicando como utilizar a ferramenta e restrições gerais que a aplicação tenha.
    a. Fiquem à vontade para escolher como será feito esse manual. Pode ser um pdf, site, vídeo, carta…

5. Não será aceito entregas atrasadas.

6. Apresentação:
    a. A equipe deve apresentar o projeto feito para os professores.
    b. Todos envolvidos da equipe devem explicar alguma parte, e perguntas direcionadas serão feitas durante a
       apresentação.
    c. O manual deve conter o fluxograma do projeto.

7. A entrega será em uma atividade do classroom
    a. O que deve ser entregue:
        ■ Código da aplicação;
        ■ Manual do usuário.

Critérios de avaliação:
    ● Apresentação (50 pontos - nota individual):
        ○ Participação durante a apresentação do projeto;
        ○ Perguntas durante a apresentação.
    ● Código (50 pontos - nota por grupo):
        ○ Legibilidade e Organização do código;
        ○ Tratamento de erros;
        ○ Utilização de Arquivos;
        ○ Apresentação da ferramenta e manual do usuário;
        ○ Funcionalidade extra.
===================================================================================================================="""
from os import path

# Função para adicionar receitas ao arquivo receitas.txt
def adicionar_receitas():
    # Cria o "banco de dados" receitas.txt no mesmo diretório do projeto caso ele não exista
    if not path.exists("receitas.txt"):
        # Abre o arquivo em modo escrita
        with open("receitas.txt", "w", encoding='utf-8') as f:
            # Não faz nada
            pass

    receitas = []
    print('Adicione receitas (-1 para parar)')

    cont = 1
    while True:
        # Solicita para o usuário digitar as informações da nova receita
        nome_receita = input(f'Digite o nome da {cont}ª receita: ')
        if nome_receita == '-1':
            break
        pais_origem = input(f'Digite o país de origem da {cont}ª receita: ')
        if pais_origem == '-1':
            break
        ingredientes_receita = input(f'Digite os ingredientes da {cont}ª receita separados por vírgula: ')
        if ingredientes_receita == '-1':
            break
        modo_preparo = input(f'Digite o modo de preparo da {cont}ª receita: ')
        if modo_preparo == '-1':
            break

        # Cria um novo dicionário receita a cada iteração do loop
        receita = {
            'nome': nome_receita,
            'origem': pais_origem,
            'ingredientes': ingredientes_receita,
            'preparo': modo_preparo
        }

        # Adiciona a nova receita no final da lista receitas
        receitas.append(receita)

        cont += 1

    # Abre o arquivo em modo apêndice
    with open("receitas.txt", "a") as f:
        # Percorre a lista de receitas
        for receita in receitas:
            # Escreve a receita no arquivo
            f.write(f"{receita['nome']}\n{receita['origem']}\n{receita['ingredientes']}\n{receita['preparo']}\n")

    print(receitas)
    return

# Função para visualizar todas as receitas que estão no arquivo receitas.txt
def visualizar_receitas():
    return

# Função atualizar as receitas do arquivo receitas.txt
def atualizar_receitas():
    return

# Função para exluir receitas do arquivo receitas.txt
def excluir_receitas():
    return

# Menu do gerenciador de receitas
opcao = ''
while opcao != '5':
    opcao = input("""
===========================
  Gerenciador de Receitas
===========================

Escolha uma opção:
[ 1 ] - Adicionar Receitas
[ 2 ] - Visualizar Receitas
[ 3 ] - Atualizar Receitas
[ 4 ] - Excluir Receitas
[ 5 ] - Sair do Programa
    
Sua opção: """)
    if opcao == '1':
        adicionar_receitas()
    elif opcao == '2':
        visualizar_receitas()
    elif opcao == '3':
        atualizar_receitas()
    elif opcao == '4':
        excluir_receitas()
    elif opcao == '5':
        print('Programa encerrado!')
        break
    else:
        print('Opção inválida!')
