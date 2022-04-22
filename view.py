import os
import maskpass
from controller import CadastrarUsuario, LogarUsuario


def limpar_tela():
    os.system('cls')

limpar_tela()

while True:
    main_menu = int(input('Sistema de Casdastro e Autenticação\n'
                         f"{'1 - Realizar Cadastro':<35}"
                         f"{'2 - Realizar Login':<35}"
                          '3 - Sair\n'
                          'Sua opção: '))
    limpar_tela()

    if main_menu == 1:
        while True:
            print('Crie sua conta em nosso sistema\n')
            nome = input('Nome: ')
            email = input('Email: ')
            senha = maskpass.askpass('Senha: ', mask = "*")

            CadastrarUsuario.cadastrar_usuario(nome, email, senha)
            
            limpar_tela()

            manter = int(input('Registrar um novo cadastro?\n'
                              f"{'1 - Sim':<15}"
                               '2 - Não\n'
                               'Sua opção: '))
            
            if manter == 1:
                limpar_tela()
                continue
            elif manter == 2:
                limpar_tela()
                break
    
    elif main_menu == 2:
        while True:
            print('Faça login em nosso sistema\n')
            email = input('Email: ')
            senha = maskpass.askpass('Senha: ', mask = "*")

            LogarUsuario.login(email, senha)

            limpar_tela()

            logar = int(input('Registrar um novo login?\n'
                              f"{'1 - Sim':<15}"
                               '2 - Não\n'
                               'Sua opção: '))
            
            if logar == 1:
                limpar_tela()
                continue
            elif logar == 2:
                limpar_tela()
                break

    elif main_menu == 3:
        break