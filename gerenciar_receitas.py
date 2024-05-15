def favoritar_receitas():
    return


# Função para adicionar receitas ao arquivo receitas.txt
def adicionar_receitas(receitas: list, modo: str) -> None:
    # Se receitas for uma lista vazia, será preenchida a lista com novas receitas
    if modo == 'a':
        print('Adicione receitas (-1 para parar)')

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
                if favorita == 'S':
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

    # Abre o arquivo em modo apêndice ou escrita (depende do lugar do código que chama esta função)
    with open("receitas.txt", modo, encoding="utf-8") as f:
        # Percorre a lista de receitas
        for receita in receitas:
            # Escreve a receita no arquivo
            f.write(f"{receita['nome']}\n{receita['origem']}\n{receita['ingredientes']}\n{receita['preparo']}\n")

    return


# Função para visualizar todas as receitas que estão no arquivo receitas.txt
def visualizar_receitas(detalhes: bool) -> list:
    receitas = []
    linhas = []
    # Abre o arquivo em modo leitura
    with open("receitas.txt", 'r', encoding="utf-8") as f:
        print('-' * 20)
        print('Receitas cadastradas')
        print('-' * 20)
        # Percorre cada linha do arquivo
        for i, linha in enumerate(f):
            # Adiciona a linha na lista linhas
            linha = linha[:-1]      # Remove o \n
            linhas.append(linha)
            # Exibe o nome
            if (i == 0) or (i % 4 == 0):
                print(f'{int(i / 4) + 1}ª receita: {linha}')
            if detalhes:
                # Exibe o país
                if (i == 1) or (i % 5 == 0):
                    print(f'\tPaís de origem: {linha}')
                # Exibe o ingrediente
                elif (i == 2) or (i % 6 == 0):
                    print(f'\tIngredientes: {linha}')
                # Exibe o modo de preparo
                elif (i == 3) or (i % 7 == 0):
                    print(f'\tModo de preparo: {linha}')

        print('-' * 20)

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

    return receitas


# Função para atualizar as receitas do arquivo receitas.txt
def atualizar_receitas():
    # Exibe para o usuário todas as receitas que estão no banco de dados
    receitas = visualizar_receitas(False)

    # Pergunta ao usuário quais receitas ele quer atualizar
    receitas_mudar = input('Quais destas receitas você quer atualizar [digite separado por vírgula]? ').split(',')

    # Remove os espaços antes e depois dos nomes das receitas e deixa todos os caracteres deles em minúsculas
    for i in range(len(receitas_mudar)):
        receitas_mudar[i] = receitas_mudar[i].strip().lower()

    # Solicita ao usuário que digite as novas informações de cada receita que ele escolheu modificar
    for i in range(len(receitas_mudar)):
        print(receitas_mudar[i])
        for j in range(len(receitas)):
            if receitas[j]['nome'] == receitas_mudar[i]:
                print('Digite -1 para não modificar')
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

    return


# Função para exluir receitas do arquivo receitas.txt
def excluir_receitas():
    # Exibe o nome das receitas que estão cadastradas no banco de dados
    receitas = visualizar_receitas(False)

    # Pede pro usuário digitar os nomes das receitas que ele quer apagar separados por vírgula
    receitas_para_excluir = input('Digite os nomes das receitas que você quer excluir separados por vírgula: ').split(',')

    # Pede pro usuário confirmar que é esssa mesmo que ele quer excluir
    print(f'As receitas que serão excluídas são: {receitas_para_excluir}')
    resposta = input('Confirma a exclusão delas [S/N]? ').upper()
    while resposta != 'S':
        # Pede pro usuário digitar os nomes das receitas que ele quer apagar separados por vírgula
        receitas_para_excluir = input('Digite novamente os nomes das receitas que você quer excluir: ').split(',')

        # Pede pro usuário confirmar que é esssa mesmo que ele quer excluir
        print(f'As receitas que serão excluídas são: {receitas_para_excluir}')
        resposta = input('Confirma a exclusão delas [S/N]? ').upper()

    # Remove os espaços antes e depois dos nomes das receitas e deixa todos os caracteres deles em minúsculas
    for i in range(len(receitas_para_excluir)):
        receitas_para_excluir[i] = receitas_para_excluir[i].strip().lower()

    excluir = []
    # Remove da lista receitas as receitas cujos nomes foram informados pelo usuário
    for i in range(len(receitas_para_excluir)):
        for j in range(len(receitas)):
            if receitas[j]['nome'] == receitas_para_excluir[i]:
                print(f'[AVISO] {receitas[j]['nome']} foi excluído!')
                excluir.append(j)
                break
    # Remove da lista receitas
    for indice in excluir:
        receitas.pop(indice)

    # Atualiza no banco de dados
    adicionar_receitas(receitas, 'w')

    return


def sugerir_receitas():
    return
