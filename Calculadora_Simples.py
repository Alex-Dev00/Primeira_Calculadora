# AS FUNÇÕES ESTÃO PRONTAS

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero!"
    return num1 / num2

def ler_numeros():
    while True:
        try:    
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida! Digite apenas números.\n")

def main():
    while True:
        
        print(10 * "-")
        print("CALCULADORA")
        print(10 * "-")
        print("[1] SOMA \n[2] SUBTRAÇÃO \n[3] MULTIPLICAÇÃO \n[4] Divisão \n[5] Sair da Calculadora")

        escolha = input("Escolha uma das opções acima:")

        
        if escolha == '1':
            num1, num2 = ler_numeros()
            print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}.")

        elif escolha == '2':
            num1, num2 = ler_numeros()
            print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)} ")

        elif escolha == '3':
            num1, num2 = ler_numeros()
            print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")

        elif escolha == '4':
            num1, num2 = ler_numeros()
            print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")


        elif escolha == '5':
            print("Saindo da calculadora... Até logo!")
            break

        else:
            print("Opção invalida, tente novamente.")

if __name__ == "__main__":
    main()