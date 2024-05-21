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
        print('[ 7 ] - Favoritar receitas')
        print('[ 8 ] - Sair do Programa')
        print('')
        # Garante que a opção digitada seja um número e que esteja no intervalo de 1 a 7
        while True:
            opcao = input('Sua opção: ')
            try:
                opcao = int(opcao)
                if (opcao >= 1) and (opcao <= 7):
                    break
                else:
                    print('[AVISO] Opção inválida! Deve ser um número de 1 a 7, por favor digite novamente.')
            except ValueError:
                print('[AVISO] Opção inválida! Deve ser um número de 1 a 7, por favor digite novamente.')
        if opcao == 1:
            novas_receitas = []
            # Cria um novo banco de dados, caso não exista, e permite adicionar novas receitas nele
            gerenciar_receitas.adicionar_receitas(novas_receitas, 'a')
        elif opcao == 2:
            # Exibe as receitas com as informações de país de origem, ingredientes e modo de preparo
            gerenciar_receitas.visualizar_receitas(True, False)
        elif opcao == 3:
            gerenciar_receitas.atualizar_receitas()
        elif opcao == 4:
            gerenciar_receitas.excluir_receitas()
        elif opcao == 5:
            gerenciar_receitas.sugerir_receitas()
        elif opcao == 6:
            gerenciar_receitas.menor_receita()
        elif opcao == 7:
            gerenciar_receitas.favoritar_receitas()
        elif opcao == 8:
            print('Programa encerrado!')
            break

        continuar = input('Deseja continuar usando o programa [S/N]? ').upper()

    print('Programa encerrado!')
