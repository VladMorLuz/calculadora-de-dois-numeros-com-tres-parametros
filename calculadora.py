def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2 if num2 != 0 else "Erro: divisão por zero"
    else:
        return 0

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))

resultado = calculadora(num1, num2, operacao)
print(f"Resultado: {resultado}")
