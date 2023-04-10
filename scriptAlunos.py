aluno = {}

for i in range(3):
    nome = input(f"Digite o nome do aluno ${i+1}: ")
    nota = float(input(f"Digite a nota do aluno ${i+1}: "))
    aluno[nome] = nota

print(aluno)