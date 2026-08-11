import os
import json
from dados import carregar_tarefas, salvar_tarefas

tarefas = carregar_tarefas()

def exibir_titulo_programa():
        print("=" * 35)
        print("""  
        L̲i̲s̲t̲a̲ d̲e̲ T̲a̲r̲e̲f̲a̲s̲

    🇸​​​​​🇮​​​​​🇸​​​​​🇹​​​​​🇪​​​​​🇲​​​​​🇦​​​​​ 🇩​​​​​🇪​​​​​ 🇨​​​​​🇴​​​​​🇳​​​​​🇹​​​​​🇷​​​​​🇴​​​​​🇱​​​​​🇪​​​​​ 🇩​​​​​🇪​​​​​ 🇹​​​​​🇦​​​​​🇷​​​​​🇪​​​​​🇫​​​​​🇦​​​​​🇸​​​​​
        """)
        print("=" * 35)

def exibir_opcoes():
    print("\n1- Adicionar tarefa") 
    print("2- Listar tarefas") 
    print("3- Marcar como concluída") 
    print("4- Remover tarefa") 
    print("5- Sair")

def finalizar_programa():
    exibir_subtitulo('Encerrando o Programa')
    exit()

def voltar_ao_menu_principal():
    input('\nDigite ENTER para voltar ao menu principal > ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def adicionar_tarefa():
    exibir_subtitulo('Cadastro de nova tarefa')
    nome_tarefa = input('Digite o nome da nova tarefa: ')
    nova_tarefa = {
        'nome': nome_tarefa,
        'concluido': False
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f'A tarefa {nome_tarefa} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_tarefas():
    exibir_subtitulo('Listando tarefas')
    for indice, tarefa in enumerate(tarefas):
        if tarefa['concluido']:
            print(f'{indice + 1} - [X] {tarefa['nome']}')
        else:
            print(f'{indice + 1} - [ ] {tarefa['nome']}')
    voltar_ao_menu_principal()

def marcar_tarefa():
    exibir_subtitulo('Marcar Tarefa Concluida')
    for indice, tarefa in enumerate(tarefas):
        print(f'{indice + 1} - {tarefa['nome']}')

    escolha = int(input('\nDigite o número da tarefa concluída: '))

    if escolha >= 1 and escolha <= len(tarefas):
        tarefas[escolha - 1]['concluido'] = True
        salvar_tarefas(tarefas)
        print('\nTarefa marcada como concluída!')
    else:
        print('\nNúmero de tarefa inválido!')
    voltar_ao_menu_principal()

def remover_tarefa():
    exibir_subtitulo('Remover Tarefa')
    for indice, tarefa in enumerate(tarefas):
        print(f'{indice + 1} - {tarefa['nome']}')
    escolha = int(input('\nDigite o numero da tarefa que quer remover: '))
    if escolha >= 1 and escolha <= len(tarefas):
        tarefa_removida = tarefas.pop(escolha - 1)
        salvar_tarefas(tarefas)
        print(f'\nA tarefa {tarefa_removida['nome']} foi removida com sucesso!')
    else:
        print('\nNúmero de tarefa inválido!')

    voltar_ao_menu_principal()

def escolher_opcao():
    opcao = input("\nEscolha uma opção: ")
    print(opcao)

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_tarefa()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        finalizar_programa()
    else:
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_titulo_programa()
    exibir_opcoes()
    escolher_opcao()



if __name__ == '__main__':

    while True:
        main()