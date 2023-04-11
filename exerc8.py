def ler():
    temperatura = float(input("Digite a temperatura em graus Celsius: "))
    return temperatura

def converter(temperatura):
    temperaturaConvertida = (9 * temperatura + 160) / 5
    return temperaturaConvertida

def mostrar(temperatura):
    print(f"A temperatura em graus Fahrenheit é: {temperatura:.2f}")

temp = ler();

temp = converter(temp);

mostrar(temp)
