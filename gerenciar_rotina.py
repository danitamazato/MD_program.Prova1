# O programa abaixo foi pensado para utilizar conceitos da teoria dos conjuntos. Seu objetivo é manter organizada a rotina de tarefas diárias de uma pessoa. Problematização: uma pessoa recebe muitas tarefas para serem cumpridas no trabalho. Imagine que a pessoa recebe essas tarefas ao longo do dia inteiro e sempre acaba se esquecendo se fez tudo o que lhe foi solicitado. Com o programa abaixo, esse problema será solucionado! Basta a pessoa acrescentar a rotina que ela quer manter no conjuntos de rotinas para o dia. Ela pode escolher visualizar as tarefas que já listou e monitorar sua rotina com maior facilidade.

def adicionar_tarefa(rotina):
    # Adicionar uma tarefa à rotina
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    rotina.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def visualizar_rotina(rotina):
    # Exibir a rotina
    print("\nSua rotina diária:")
    for i, tarefa in enumerate(rotina, start=1):
        print(f"{i}. {tarefa}")

def main():
    # Lista para armazenar a rotina diária
    rotina_diaria = []

    while True:
        print("\n------ Menu ------")
        print("1. Adicionar tarefa")
        print("2. Visualizar rotina")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_tarefa(rotina_diaria)
        elif escolha == '2':
            visualizar_rotina(rotina_diaria)
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    print("Bem-vindo ao organizador de rotina diária!")
    main()
