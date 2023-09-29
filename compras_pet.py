# Conjunto é uma estrutura que agrupa objetos e constitui uma base para construir estruturas mais complexas. Podemos definir um conjunto como uma coleção de "zero" ou "mais objetos" distintos chamados de elementos do conunto, os quais não possuem qualquer ordem associada.

# O programa a seguir, utiliza conceitos aprendidos em teoria dos conjuntos para resolver um problema que alguns pais de pet sofrem ao esquematizar a compra de produtos para os seus pets. A ideia é que o programa organize os produtos em conjuntos de acordo com a periodicidade de sua compra, ajudando os pais de pet na tarefa de não deixá-los sem os suprimentos. Problematização: um pai de pet esquecido, sempre esquece de comprar a ração de seu pet na data correta, resultado: ele acaba tendo que se virar para comprar, às pressas, o alimento para que seu pet não passe fome.

def agrupar_compras(produtos):
    quinzenal = []
    mensal = []
    mes_e_meio = []

# O programa agrupa os produtos em três listas diferentes, dependendo da frequência: quinzenal (15 dias), mensal (30 dias) e a cada 1 mês e meio (45 dias). 

    for produto, frequencia in produtos.items():
        if frequencia == 15:
            quinzenal.append(produto)
        elif frequencia == 30:
            mensal.append(produto)
        elif frequencia == 45:
            mes_e_meio.append(produto)

    return quinzenal, mensal, mes_e_meio

def main():
    produtos = {}

    while True:
        produto = input("Digite o nome do produto (ou 'sair' para terminar): ")
        if produto.lower() == 'sair':
            break

        try:
            frequencia = int(input("Digite a frequência de compra em dias para {} (por exemplo, 15 para quinzenal): ".format(produto)))
            produtos[produto] = frequencia
        except ValueError:
            print("A frequência deve ser um número inteiro.")

    quinzenal, mensal, mes_e_meio = agrupar_compras(produtos)

    print("\nProdutos a serem comprados quinzenalmente:")
    print(quinzenal)

    print("\nProdutos a serem comprados mensalmente:")
    print(mensal)

    print("\nProdutos a serem comprados a cada 1 mês e meio:")
    print(mes_e_meio)

if __name__ == "__main__":
    main()