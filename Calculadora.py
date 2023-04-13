def calculadora():
   
   while True:
      num1 = int(input("digite o preimeiro número "))

      operacao = input("digite a operação desejada (+=1 -=2 3=* 4=/)")

      num2 = int(input ("digite o segundo número:") )

      
      if operacao =="1":
         resultado = num1 + num2

      if operacao =="2":
         resultado = num1 - num2

      if operacao =="3":
         resultado = num1 * num2

      if operacao =="4":
         operacao = num1 / num2 

      print("resultado: ", resultado)
   return

calculadora()


      

       
