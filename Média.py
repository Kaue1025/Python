varialvel = [10]
total = 0
for numb in range(1,11):
    varialvel.append (float (input("Digite um numero:")))
for numb2 in range(1,11):
    total = total + varialvel[numb2]
print("A media é", total / 10)