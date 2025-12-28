print("====minha calculadora====")

num1 = float(input("insira o primeiro numero: "))
operação = input("insira a operação (+, -, *, /): ")
num2 = float(input("insira o segundo numero: "))

if operação == "+":
    resultado = num1 + num2
elif operação == "-":
    resultado = num1 - num2
elif operação == "*":
    resultado = num1 *num2
elif operação == "/":
    if num2 == 0:
        resultado = "Erro : divisão por zero!"
    else:
        resultado = num1 / num2
else:
    resultado = "operação invalida!"

print("resultado:", resultado)
