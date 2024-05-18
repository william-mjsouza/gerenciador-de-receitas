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

# Importa as funções do gerenciador de receitas
import gerenciar_receitas

# Função principal
if __name__ == '__main__':
    # Menu do gerenciador de receitas
    continuar = 'S'
    while continuar[0] == 'S':
        print('===========================')
        print('  Gerenciador de Receitas  ')
        print('===========================')
        print('')
        print('[ 1 ] - Adicionar Receitas')
        print('[ 2 ] - Visualizar Receitas')
        print('[ 3 ] - Atualizar Receitas')
        print('[ 4 ] - Excluir Receitas')
        print('[ 5 ] - Sugerir Receitas')
        print('[ 6 ] - Menor Receita')
        print('[ 7 ] - Sair do Programa')
        print('')
        opcao = input('Sua opção: ')
        if opcao == '1':
            novas_receitas = []
            # Cria um novo banco de dados, caso não exista, e permite adicionar novas receitas nele
            gerenciar_receitas.adicionar_receitas(novas_receitas, 'a')
        elif opcao == '2':
            # Exibe as receitas com as informações de país de origem, ingredientes e modo de preparo
            receitas_info = True
            gerenciar_receitas.visualizar_receitas(receitas_info)
        elif opcao == '3':
            gerenciar_receitas.atualizar_receitas()
        elif opcao == '4':
            gerenciar_receitas.excluir_receitas()
        elif opcao == '5':
            gerenciar_receitas.sugerir_receitas()
        elif opcao == '6':
            gerenciar_receitas.menor_receita()
        elif opcao == '7':
            print('Programa encerrado!')
            break
        else:
            print('Opção inválida!')

        continuar = input('Deseja continuar usando o programa [S/N]? ').upper()
