def somar(array):
    soma = 0
    for numero in array:
        soma += numero
    media = soma / len(array)
    return media


array = [1,2,3,4,5]

print(somar(array))
