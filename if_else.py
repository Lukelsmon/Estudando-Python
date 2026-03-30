# o If e Else são estruturas de controle de fluxo em Python que permitem executar diferentes blocos de código com base em condições.
# A estrutura básica do If é a seguinte:
# if condição:
#     bloco de código a ser executado se a condição for verdadeira
# O Else é usado para executar um bloco de código quando a condição do If é falsa. A estrutura básica do Else é a seguinte:
# else:
#     bloco de código a ser executado se a condição do If for falsa
# Exemplo de uso do If e Else:
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você não é maior de idade.")

# No exemplo acima, o programa solicita ao usuário que insira sua idade. Em seguida, verifica se a idade é maior ou igual a 18. Se for, imprime "Você é maior de idade." Caso contrário, imprime "Você não é maior de idade."

# Um exemplo mais complexo de If e Else:
nota = float(input("Digite a nota do aluno: "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")

# o Elif é uma abreviação de "else if" e é usado para verificar múltiplas condições. Porém, tenha em mente que o Elif é opcional e pode ser usado quantas vezes forem necessárias. Em situações de empresas, o Elif é muito útil para lidar com várias condições de forma organizada e legível.    