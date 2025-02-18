import os 

os.system("clear")

notas = []
n = []

contador = 1 

while contador <= 3:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1

print ("Quantidade de notas: ", len(notas))

print()
for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "Tirou a nota: ", nota)