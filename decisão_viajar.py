# Raciocínio lógico é uma organização ou estruturação de raciocínios que nos permite, de acordo com determinadas normas, chegar a uma conclusão ou resolver um problema. Esse raciocínio é importante porque nos permite, principalmente, resolver problemas práticos do dia a dia. Embora ele seja importante para cálculos, por exemplo, está mais relacionado à nossa habilidade de encontrar o caminho correto para a resolução de um impasse do que necessariamente nossa habilidade com os números.

# O programa a seguir, procura aplicar conceitos da lógica em um dilema que muitos enfrentam: viajar hoje, vale a pena ou é melhor continuar em casa? Neste programa, consideramos apenas o clima como fator determinante para tal decisão.

def decidir_viajar(temperatura, chovendo):
    if 20 <= temperatura <= 30 and not chovendo:
        return "Você pode viajar."
    else:
        return "Melhor ficar em casa."

# Informações sobre o clima atual:
temperatura = float(input("Digite a temperatura atual (em graus Celsius): "))
chovendo = input("Está chovendo? (sim/não): ").lower()

# Converter a resposta sobre chuva em um valor booleano
chovendo = chovendo == 'sim'

# Decidindo se podemos sair de casa
resultado = decidir_viajar(temperatura, chovendo)
print(resultado)