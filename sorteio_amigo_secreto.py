# O programa utiliza conceitos abordados em teoria dos conjuntos e tem como objetivo acabar com os papéis para sortear o amigo secreto de fim de ano, para isso, o programa permite que sejam inseridos os nomes das pessoas. Em seguida, a pessoa digita o nome dela e descobre quem é seu amigo-secreto!

import random
# radom gera números aleatórios


def realizar_sorteio(pessoas):
    amigos_secretos = pessoas.copy()
    random.shuffle(amigos_secretos)  # embaralha a lista de pessoas
    return amigos_secretos


def encontrar_amigo_secreto(pessoas, nome_pessoa):
    try:
        index_pessoa = pessoas.index(nome_pessoa)
        # Retorna o próximo da lista (circular)
        return pessoas[(index_pessoa + 1) % len(pessoas)]
    except ValueError:
        return None


def main():
    pessoas = []

    while True:
        nome = input("Digite o nome de uma pessoa (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break

        pessoas.append(nome)

    if len(pessoas) < 2:
        print("É necessário ter pelo menos duas pessoas para fazer o sorteio.")
    else:
        print("\nResultado do sorteio do Amigo Secreto:")
        amigo_secreto = realizar_sorteio(pessoas)
        print("O sorteio foi realizado com sucesso!")

        while True:
            nome_pessoa = input(
                "Digite seu nome para saber quem é seu amigo secreto (ou 'sair' para terminar): ")
            if nome_pessoa.lower() == 'sair':
                break

            amigo = encontrar_amigo_secreto(pessoas, nome_pessoa)
            if amigo:
                print(f"Seu amigo secreto é: {amigo}")
            else:
                print("Nome não encontrado. Certifique-se de que digitou corretamente.")


if __name__ == "__main__":
    print("Bem-vindo ao sorteio do Amigo Secreto!")
    main()
