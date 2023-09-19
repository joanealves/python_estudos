# MAIOR_IDADE = 18

# idade = int(input("Informe sua idade: "))

# if idade >= MAIOR_IDADE:
#    print ("Você tem que se alistar")

# if idade <=MAIOR_IDADE :
#    print ("Já pode votar!")

# else:
#    print("Ainda não pode dirigir")

# exemplo 2

conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial= 450

if conta_normal:
   if saldo >= saque:  
      print("Saque realizado com sucesso!")
   elif saque <=(saldo + cheque_especial):
       print("Saque realizado com limite do cheque especial") 
   else:
      print('Não foi possivel realiar o saque, saldo insuficiente!')
elif conta_universitaria:
   if saldo >=saque:
      print('Saque realiado com sucesso!')
   else:
      print("Saldo insuficiente!")     