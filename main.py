salario1: float; salario2:float
nome1: str; nome2: str
idade: int
sexo: str

nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input("Salário da primeira pessoa: "))

nome2 = input("Nome da segunda pessoa: ")
salario2 = float(input("Salário da segunda pessoa: "))

idade = int(input("Digite uma idade: "))
sexo = input("Digite um sexo (F/M): ")

print(f"Nome1: {nome1}")
print(f"Salário1: {salario1:.2f}")

print(f"Nome2: {nome2}")
print(f"Salário2: {salario2:.2f}")

print(f"Idade: {idade}")

print(f"Sexo: {sexo}")