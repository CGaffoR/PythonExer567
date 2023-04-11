numeros = []

for i in range(5):
    numero = int(input("Digite um número : "))
    numeros.append(numero)

soma = 0 

for numero in numeros:
    print(f"{soma} + {numero}: {soma+numero}")
    soma += numero

print(f"A soma foi de: {soma}")
