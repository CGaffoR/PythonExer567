def ler_valores():
    tempo = float(input("Digite o tempo gasto na viagem (em horas): "))
    velocidade_media = float(input("Digite a velocidade média durante a viagem (em km/h): "))
    return tempo, velocidade_media

def calcular_distancia(tempo, velocidade_media):
    distancia = tempo * velocidade_media
    return distancia

def calcular_litros(distancia):
    litros_usados = distancia / 12
    return litros_usados

def apresentar_resultado(tempo, velocidade_media, distancia, litros_usados):
    print(f"Tempo gasto na viagem: {tempo:.2f} horas")
    print(f"Velocidade média durante a viagem: {velocidade_media:.2f} km/h")
    print(f"Distância percorrida: {distancia:.2f} km")
    print(f"Quantidade de litros utilizada na viagem: {litros_usados:.2f} litros")
