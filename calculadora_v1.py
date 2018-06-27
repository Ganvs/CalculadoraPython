# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

def soma(num1, num2):
    return print("A soma dos dois números é " + str(num1 + num2));

def subtrair(num1, num2):
    return print("A subtração dos dois números é: " + str(num1 - num2))

def multiplicar(num1, num2):
    return print("A multiplicação dos dois números é " + str(num1 * num2))

def dividir(num1, num2):
    return print("A divisão dos dois números é " + str(num1 / num2))


print("\n******************* Python Calculator *******************")
print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - Sair")
opcao = 1


while opcao != 0:
    opcao = int(input("Opção: "))
    if opcao == 0:
        break
    elif opcao < 0 or opcao > 4:
        print("Opção inválida")
        continue
    else:
        num1 = int(input("Informe o primeiro número: "))
        num2 = int(input("Informe o segundo número: "))

        if opcao == 1:
            soma(num1, num2)
        elif opcao == 2:
            subtrair(num1, num2)
        elif opcao == 3:
            multiplicar(num1, num2)
        elif opcao == 4:
            dividir(num1, num2)
        else:
            print("Inválido")

print("Volte sempre!")