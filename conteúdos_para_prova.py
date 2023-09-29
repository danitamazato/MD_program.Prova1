# Em teoria dos conjuntos aprendemos que....
# Aplicando essa ideia, este programa tem como objetivo ajudar estudantes a organizarem uma rotina de revisão de uma disciplina antes de uma prova. A pessoa insere os tópicos que precisa revisar e a prioridade de cada tópico.

def organizar_revisao():
    topicos = []

    while True:
        topico = input("Digite o nome do tópico a ser revisado (ou 'sair' para terminar): ")
        if topico.lower() == 'sair':
            break

        try:
            prioridade = int(input("Digite a prioridade do tópico (um número maior indica maior prioridade): "))
            topicos.append((topico, prioridade))
        except ValueError:
            print("A prioridade deve ser um número inteiro.")

    # Ordena os tópicos com base na prioridade
    topicos.sort(key=lambda x: x[1])

    print("\nOrganização para a revisão:")
    for i, (topico, _) in enumerate(topicos, start=1):
        print(f"{i}. Revisar {topico}")

if __name__ == "__main__":
    print("Bem-vindo à organização de revisão para a prova!")
    organizar_revisao()