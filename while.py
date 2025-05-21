'''n = int(input("tabuada de: "))
x = 1
while x <= 10:
    print(n*x)
    x=x+1

#Exercicio 5.6
n = int(input("tabuada de:"))
x = 1
while x <= 10:
    print(n,"x", x,"=",n*x)
    x=x+1
'''
#Exercicio 5.7
n = int(input("tabuada :"))
fim = int(input("fim da tabuada :"))
x = 1
while x <= fim:
    print(n,"x", x,"=",n*x)
    x=x+1

#while... break
s=0
while True:
    v=int(input("dgite um número a somar ou 0 para sair"))
    if v==0:
        break
    s = s+v
print(s)




        
