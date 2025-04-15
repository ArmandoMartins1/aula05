alunos = int(input("Informe o numero de alunos: "))
i=1
soma=0
while i<=alunos:
    notas = float(input("Digite a nota do aluno: "))
    soma+=notas
    i+=1

media=soma/alunos
print(f"A média da turma é: {media:.2f}")