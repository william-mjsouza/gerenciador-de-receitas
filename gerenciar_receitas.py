import random

def favoritar_receitas():
    return


# Função para adicionar receitas ao arquivo receitas.txt
def adicionar_receitas(receitas: list, modo: str) -> None:
    # Se o modo de abertura do arquivo for apêndice, será preenchida a lista com novas receitas
    if modo == 'a':
        msg = 'Adicione receitas (-1 para parar)'
        tam_msg = len(msg)
        print('-' * tam_msg)
        print(msg)
        print('-' * tam_msg)
        print('')

        cont = 1
        while True:
            # Solicita para o usuário digitar as informações da nova receita
            # Nome
            nome_receita = input(f'Digite o nome da {cont}ª receita: ')
            if nome_receita == '-1':
                break
            # Pergunta se ele deseja favoritar
            else:
                favorita = input(f'Deseja adicionar {nome_receita} aos favoritos [S/N]? ').upper()
                if favorita[0] == 'S':
                    nome_receita += '*'
            # País
            pais_origem = input(f'Digite o país de origem da {cont}ª receita: ')
            if pais_origem == '-1':
                break
            # Ingredientes
            ingredientes_receita = input(f'Digite os ingredientes da {cont}ª receita separados por vírgula: ')
            if ingredientes_receita == '-1':
                break
            # Modo de Preparo
            modo_preparo = ''
            print(f'Digite o modo de preparo (passo a passo) da {cont}ª receita (-1 para parar)')
            j = 1
            while True:
                passo = input(f'{j}º passo: ')
                if passo == '-1':
                    break
                else:
                    modo_preparo += f'{passo}. '
                j += 1

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

    # Abre o arquivo em modo apêndice ou escrita (depende do lugar do código que chama esta função)
    with open("receitas.txt", modo, encoding="utf-8") as f:
        # Percorre a lista de receitas
        for receita in receitas:
            # Escreve a receita no arquivo
            f.write(f"{receita['nome']}\n{receita['origem']}\n{receita['ingredientes']}\n{receita['preparo']}\n")

    return None


# Função para visualizar todas as receitas que estão no arquivo receitas.txt
def visualizar_receitas(detalhes: bool, todas: bool) -> list:
    receitas = []
    linhas = []
    # Tenta abrir o arquivo receitas.txt em modo leitura
    try:
        with open("receitas.txt", 'r', encoding="utf-8") as f:
            # Percorre cada linha do arquivo
            for linha in f:
                # Adiciona a linha na lista linhas
                linha = linha[:-1]      # Remove o \n
                linhas.append(linha)
        # Mas caso não exista o arquivo
    except FileNotFoundError:
        print('[AVISO] Erro ao tentar ler o arquivo receitas.txt')
        print('[AVISO] Criando um novo arquivo receitas.txt ...')
        # Será criado um novo vazio
        open("receitas.txt", 'w', encoding="utf-8").close()

    # OBS: Cada receita no arquivo receita.txt é formado por um grupo de 4 linhas
    for i in range(0, len(linhas) - 3, 4):
        # Preenche o novo dicionário receita que é criado a cada iteração do loop
        nome_receita = linhas[i]
        pais_origem = linhas[i + 1]
        ingredientes_receita = linhas[i + 2]
        modo_preparo = linhas[i + 3]

        receita = {
            'nome': nome_receita,
            'origem': pais_origem,
            'ingredientes': ingredientes_receita,
            'preparo': modo_preparo
        }

        # Formado o dicionário, ele é adicionado a lista receitas
        if (i == 0) or (i % 4 == 0):
            receitas.append(receita)

    opcao = 0
    if not todas:
        # Pergunta qual tipo de visualização o usário quer ver
        msg = 'Escolha o modo de visualização'
        tam_msg = len(msg)
        print('-' * tam_msg)
        print(msg)
        print('-' * tam_msg)

        print('')
        print('[ 1 ] - Pesquisar por país')
        print('[ 2 ] - Exibir as receitas favoritas')
        print('[ 3 ] - Exibir todas as receitas')
        print('')
        # Garante que a opção digitada seja um número e que esteja no intervalo de 1 a 7
        while True:
            opcao = input('Sua opção: ')
            try:
                opcao = int(opcao)
                if (opcao >= 1) and (opcao <= 3):
                    break
                else:
                    print('[AVISO] Opção inválida! Deve ser um número de 1 a 3, por favor digite novamente.')
            except ValueError:
                print('[AVISO] Opção inválida! Deve ser um número de 1 a 3, por favor digite novamente.')
        k = 1
        if opcao == 1:
            msg = 'Receitas por País'
            tam_msg = len(msg)
            print('-' * tam_msg)
            print(msg)
            print('-' * tam_msg)
            print('')
            # Solicita que o usuário digite o nome do país para a pesquisa
            pais = input('Digite o nome do país das receitas que você quer pesquisar: ').lower()
            for i, receita in enumerate(receitas):
                if (receitas[i]["origem"]).lower() == pais:
                    # Exibe o nome
                    print(f'{k}ª receita: {receitas[i]["nome"]}')
                    if detalhes:
                        # Exibe o país
                        print(f'\tPaís de origem: {receitas[i]["origem"]}')
                        # Exibe os ingredientes
                        print(f'\tIngredientes: {receitas[i]["ingredientes"]}')
                        # Exibe o modo de preparo no formato passo a passo
                        print('\tModo de preparo:')
                        passos = receitas[i]["preparo"].split('.')
                        for j, passo in enumerate(passos):
                            print(f'\t{j + 1}º passo: {passo.strip()}')
                            if (j + 1) == (len(passos) - 1):
                                break

                        k += 1
        elif opcao == 2:
            msg = 'Receitas Favoritas'
            tam_msg = len(msg)
            print('-' * tam_msg)
            print(msg)
            print('-' * tam_msg)
            print('')
            for i, receita in enumerate(receitas):
                # Verifica se o último caracter do nome da receita é um '*' (se a receita está favoritada)
                if (receitas[i]["nome"][-1]).lower() == '*':
                    # Exibe o nome
                    print(f'{k}ª receita: {receitas[i]["nome"]}')
                    if detalhes:
                        # Exibe o país
                        print(f'\tPaís de origem: {receitas[i]["origem"]}')
                        # Exibe os ingredientes
                        print(f'\tIngredientes: {receitas[i]["ingredientes"]}')
                        # Exibe o modo de preparo no formato passo a passo
                        print('\tModo de preparo:')
                        passos = receitas[i]["preparo"].split('.')
                        for j, passo in enumerate(passos):
                            print(f'\t{j + 1}º passo: {passo.strip()}')
                            if (j + 1) == (len(passos) - 1):
                                break
                    k += 1
    if (opcao == 3) or todas:
        msg = 'Todas as Receitas'
        tam_msg = len(msg)
        print('-' * tam_msg)
        print(msg)
        print('-' * tam_msg)
        print('')
        for i, receita in enumerate(receitas):
            # Exibe o nome
            print(f'{i + 1}ª receita: {receitas[i]["nome"]}')
            if detalhes:
                # Exibe o país
                print(f'\tPaís de origem: {receitas[i]["origem"]}')
                # Exibe os ingredientes
                print(f'\tIngredientes: {receitas[i]["ingredientes"]}')
                # Exibe o modo de preparo no formato passo a passo
                print('\tModo de preparo:')
                passos = receitas[i]["preparo"].split('.')
                for j, passo in enumerate(passos):
                    print(f'\t{j + 1}º passo: {passo.strip()}')
                    if (j + 1) == (len(passos) - 1):
                        break

        print('-' * tam_msg)

    return receitas


# Função para atualizar as receitas do arquivo receitas.txt
def atualizar_receitas() -> None:
    # Exibe para o usuário todas as receitas que estão no banco de dados
    receitas = visualizar_receitas(False, True)

    # Pergunta ao usuário quais receitas ele quer atualizar
    receitas_mudar = input('Quais destas receitas você quer atualizar [digite separado por vírgula]? ').split(',')

    # Remove os espaços antes e depois dos nomes das receitas e deixa todos os caracteres deles em minúsculas
    for i in range(len(receitas_mudar)):
        receitas_mudar[i] = receitas_mudar[i].strip().lower()

    # Solicita ao usuário que digite as novas informações de cada receita que ele escolheu modificar
    for i in range(len(receitas_mudar)):
        for j in range(len(receitas)):
            if (receitas[j]['nome']).lower() == receitas_mudar[i]:
                print('OBS: Digite -1 para não modificar')
                nova_origem = input(f'Digite o novo país de origem pra receita de {receitas_mudar[i]}: ')
                if nova_origem != '-1':
                    receitas[j]['origem'] = nova_origem
                novos_ingredientes = input(f'Digite os novos ingredientes pra receita de {receitas_mudar[i]}: ')
                if novos_ingredientes != '-1':
                    receitas[j]['ingredientes'] = novos_ingredientes
                novo_preparo = input(f'Digite o novo modo de preparo pra receita de {receitas_mudar[i]}: ')
                if novo_preparo != '-1':
                    receitas[j]['preparo'] = novo_preparo

    # Atualiza no banco de dados
    adicionar_receitas(receitas, 'w')

    return None


# Função para exluir receitas do arquivo receitas.txt
def excluir_receitas() -> None:
    # Exibe o nome das receitas que estão cadastradas no banco de dados
    receitas = visualizar_receitas(False, True)

    # Pede pro usuário digitar os nomes das receitas que ele quer apagar separados por vírgula
    receitas_para_excluir = input('Digite os nomes das receitas que você quer excluir separados por vírgula: ').split(',')

    # Pede pro usuário confirmar que são esssas mesmo que ele quer excluir
    print(f'As receitas que serão excluídas são: {receitas_para_excluir}')
    resposta = input('Confirma a exclusão delas [S/N]? ').upper()
    while resposta != 'S':
        # Repete a solicitação
        receitas_para_excluir = input('Digite novamente os nomes das receitas que você quer excluir: ').split(',')

        # Repete a solicitação
        print(f'As receitas que serão excluídas são: {receitas_para_excluir}')
        resposta = input('Confirma a exclusão delas [S/N]? ').upper()

    # Remove os espaços antes e depois dos nomes das receitas e deixa todos os caracteres deles em minúsculas
    for i in range(len(receitas_para_excluir)):
        receitas_para_excluir[i] = receitas_para_excluir[i].strip().lower()

    # Remove da lista receitas as receitas cujos nomes estão na lista receitas_para_excluir
    for i in range(len(receitas_para_excluir)):
        for j in range(len(receitas)):
            if (receitas[j]['nome']).lower() == receitas_para_excluir[i]:
                print(f"[AVISO] {receitas[j]['nome']} foi excluído!")
                receitas.pop(j)
                break

    # Atualiza no banco de dados
    adicionar_receitas(receitas, 'w')

    return None


def sugerir_receitas() -> None:
    # Adquiri as receitas disponiveis
    receitas = visualizar_receitas(detalhes=False, todas=True)

    # Verifica se há receitas disponíveis
    if len(receitas) == 0:
        print('[AVISO] Não há receitas disponíveis para sugestão.')
        return

    # Pergunta ao usuário quantas receitas deseja que sejam sugeridas
    while True:
        try:
            sugestao = int(input('Quantas receitas você deseja que sejam sugeridas? '))
            if sugestao <= 0:
                print('[AVISO] Por favor, digite um número positivo.')
            else:
                break
        except ValueError:
            print('[AVISO] Por favor, digite um número válido.')

    # Seleciona aleatoriamente algumas receitas
    receitas_sugeridas = random.sample(receitas, min(sugestao, len(receitas)))

    # Exibe as receitas sugeridas
    print('Receitas Sugeridas Aleatoriamente:')
    for i, receita in enumerate(receitas_sugeridas, start=1):
        print(f'{i}. {receita["nome"]} - {receita["origem"]}')


    return None


def menor_receita() -> None:
    try:
        with open("receitas.txt", 'r', encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print('[AVISO] Erro ao tentar ler o arquivo receitas.txt')
        print('[AVISO] Criando um novo arquivo receitas.txt ...')
        with open("receitas.txt", 'w', encoding="utf-8") as f:
            pass

    menor_quantidade = float('inf')
    receitas_menor_quantidade = []

    for i in range(0, len(linhas), 4):
        ingredientes = linhas[i + 2].strip()
        quantidade_ingrediente = len(ingredientes.split(','))

        if quantidade_ingrediente < menor_quantidade:
            menor_quantidade = quantidade_ingrediente
            receitas_menor_quantidade = [linhas[i].strip()]

        elif quantidade_ingrediente == menor_quantidade:
            receitas_menor_quantidade.append(linhas[i].strip())

    if len(receitas_menor_quantidade) == 1:
        nome_receita = ''.join(receitas_menor_quantidade)
        print(f'A receita de {nome_receita} possui a menor quantidade de ingredientes.')
    elif len(receitas_menor_quantidade) > 1:
        nomes_receitas = ', '.join(receitas_menor_quantidade)
        print(f'As receitas de {nomes_receitas} possuem as menores quantidades de ingredientes.')
    else:
        print('[AVISO] Não há nenhuma receita no banco de dados, por favor adicione alguma receita')
        receitas = []
        adicionar_receitas(receitas, 'a')

    return None
