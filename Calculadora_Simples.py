# AS FUNÇÕES ESTÃO PRONTAS

def mostrar_menu():


def soma(num1, num2):
    resultado = num1 + num2
    return resultado

def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero!"

    resultado = num1 / num2
    return resultado

while True:
    # FAZER O LAYOUT DE OPÇÃO DA CALCULADORA
    print(10 * "-")
    print("CALCULADORA")
    print(10 * "-")
    print("[1] SOMA \n[2] SUBTRAÇÃO \n[3] MULTIPLICAÇÃO \n[4] Divisão \n[5] Sair da Calculadora")
    escolha = input("Escolha uma das opções acima:")
    # FAZER AS ESCOLHAS USANDO IF 
    if escolha == '1':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o seugndo número: "))
        resultado_soma = soma(num1, num2)
        print(f"A soma do número {num1} e do número {num2} é igual a {resultado_soma}.")

    elif escolha == '2':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("digite o segundo número: "))
        resultado_subtracao = subtracao(num1, num2)
        print(f"A subtração do número {num1} e do número {num2} é igual a {resultado_subtracao}")

    elif escolha == '3':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado_multiplicacao = multiplicacao(num1, num2)
        print(f"A multiplicação do número {num1} e do número {num2} é igual a {resultado_multiplicacao}")

    elif escolha == '4':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado_divisao = divisao(num1, num2)
        print(f"A divisão do número {num1} e do número {num2} é igual a {resultado_divisao}")

    elif escolha == '5':
        print("Saindo da calculadora")
        break

    else:
        print("Opção invalida, tente novamente.")