

print('em que ano você nasceu?')
nasceu = int (input())


print('em que ano estamos?')
ano = int (input())


print ('voce fez aniversario esse ano digite  1 para sim  ou 2 para não   : ')
aniversario =input()


if aniversario=="1":
 idade = ano - nasceu
 print('voce tem:', ano - nasceu   )

if  aniversario=="2":
 idade = ano - nasceu -1 
 print ('voce tem:', ano - nasceu - 1  )

