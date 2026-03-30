# % ou porcentagem é um operador matemático que representa a divisão de um número por 100. Ele é usado para calcular porcentagens, descontos, aumentos, entre outros.

# Em Python, o operador % também é conhecido como operador de módulo, que retorna o resto da divisão entre dois números. Por exemplo:
a = 10
b = 3
resto = a % b
print("O resto da divisão de", a, "por", b, "é:", resto)

# O que sobrou desta divisão esencialmente o que o operador % retorna. No exemplo acima, o resultado será 1, pois 10 dividido por 3 é igual a 3 com um resto de 1.
# O operador % também pode ser usado para calcular porcentagens. Por exemplo, se quisermos calcular 20% de um valor, podemos usar a seguinte fórmula:
valor = 100
porcentagem = 20
resultado = valor * (porcentagem / 100)
print(porcentagem, "% de", valor, "é:", resultado)