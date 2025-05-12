
saldo=int(input("digite o valor bancário"))
saque=int(input("digite o valor de saque"))

if saldo>=saque:
    saldo=saldo-saque
    print("O saque foi realizado com sucesso! Saia de sua conta.")

else:
   print("Não possui saldo suficiente para realizar essa operação:", saldo)


nota1=int(input("digite a primeira nota"))
nota2=int(input("digite a segunda nota"))
media=(nota1+nota2)/2 

if media>=6:
    print("aprovado")

else:
    print("reprovado")























