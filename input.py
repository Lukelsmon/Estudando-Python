metros = int(input("Digite a quantidade de metros: "))
milimetros = metros * 1000
print(metros, "metros equivalem a", milimetros, "milímetros.")

# input() é uma função que permite ao usuário inserir dados durante a execução do programa. O valor inserido é sempre tratado como uma string, por isso usamos int() para converter a entrada em um número inteiro.


# Exemplo de uso do input() para calcular a área de um retângulo
base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
print("A área do retângulo é:", area)

# O código acima solicita ao usuário que insira a base e a altura de um retângulo, converte essas entradas para números de ponto flutuante (float) e calcula a área multiplicando a base pela altura. Em seguida, imprime o resultado na tela.