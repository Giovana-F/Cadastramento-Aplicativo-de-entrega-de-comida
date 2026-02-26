import os

def exibir_nome_do_progrma():
    print(""""
██╗░░░██╗██╗░░░██╗███╗░░░███╗███╗░░░███╗██╗░░░██╗
╚██╗░██╔╝██║░░░██║████╗░████║████╗░████║╚██╗░██╔╝
░╚████╔╝░██║░░░██║██╔████╔██║██╔████╔██║░╚████╔╝░
░░╚██╔╝░░██║░░░██║██║╚██╔╝██║██║╚██╔╝██║░░╚██╔╝ ░
░░░██║░░░╚██████╔╝██║░╚═╝░██║██║░╚═╝░██║░░░██║░░░
░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░ \n""")#caso de importante identação, pois sem o tab no começo do print, da erro

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')    
    print('4. Sair\n')

def finalizar_app():
    os.system('cls') #limpa a tela do terminal, para deixar mais organizado
    print("Finalizando o app...")

def escolher_opcao():
    opcao_escolhida =int(input('Escolha uma opcao: ')) #o input ret uma string. Por isso a utilização do int, assim que o usuári inseri o valor, é feito a conversão
    # opcao_escolhida = int(opcao_escolhida) #outra forma de fazer a conversão, mas nesse caso, o input ficaria sem o int, e depois seria feita a conversão. 
    # A vantagem de colocar o int direto no input é que já faz a conversão na hora, evitando erros futuros caso esqueça de converter depois.


    if opcao_escolhida == 1:
        print("Cadastrar Restaurante")
    elif opcao_escolhida == 2:
        print("Listar Restaurante")
    elif opcao_escolhida == 3:
        print("Ativar Restaurante")
    else:
        finalizar_app()

def main():
    exibir_nome_do_progrma()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':# resumindo: assim que ele for o arquivo principal do programa, as acoes serão executadas
    main()
