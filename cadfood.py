print(""""
██╗░░░██╗██╗░░░██╗███╗░░░███╗███╗░░░███╗██╗░░░██╗
╚██╗░██╔╝██║░░░██║████╗░████║████╗░████║╚██╗░██╔╝
░╚████╔╝░██║░░░██║██╔████╔██║██╔████╔██║░╚████╔╝░
░░╚██╔╝░░██║░░░██║██║╚██╔╝██║██║╚██╔╝██║░░╚██╔╝░░
░░░██║░░░╚██████╔╝██║░╚═╝░██║██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░ \n""")

print('1. Cadastrar Restaurante')
print('2. Listar Restaurante')
print('3. Ativar Restaurante')    
print('4. Sair\n')

opcao_escolhida =input('Escolha uma opcao: ')
print(f'Voce escolheu a opcao: {opcao_escolhida}')

if opcao_escolhida == '1':
    print("Cadastrar Restaurante")
elif opcao_escolhida == '2':
    print("Listar Restaurante")
elif opcao_escolhida == '3':
    print("Ativar Restaurante")
elif opcao_escolhida == '4':
    print("Encerrando o programa... ")
else:
    print("Opcao Invalida")

