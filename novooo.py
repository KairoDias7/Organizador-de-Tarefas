import os
import json

tarefas = ['Estudar Python', 'Fazer exercicio', 'Estudar Git']

def salvar_tarefas(tarefas):
    with open("tarefasp.json", "w", encoding="utf-8") as tarefasp:
        json.dump(tarefas, tarefasp, indent=4, ensure_ascii=False)


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
    tarefas.append(nome_tarefa)
    salvar_tarefas(tarefas)
    print(f'A tarefa {nome_tarefa} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_tarefas():
    exibir_subtitulo('Listando tarefas')
    for tarefa in tarefas:
        print(f'.{tarefa}')
    voltar_ao_menu_principal()


def escolher_opcao():
    opcao = input("\nEscolha uma opção: ")
    print(opcao)

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        print("Marcar tarefas concluídas")
    elif opcao == "4":
        print("Remover tarefa")
    elif opcao == "5":
        finalizar_programa()
    else:
        opcao_invalida()
        
def main():
    os.system('cls')
    exibir_titulo_programa()
    exibir_opcoes()
    escolher_opcao()


## salvar tarefas


if __name__ == '__main__':
    salvar_tarefas(tarefas)


    while True:
        main()