'''
l=[60,27, 69, 13]
maximo=l[0]
for e in l:
    if e > maximo:
        maximo = e
print(maximo)
'''
'''
L=[5,9,13]
for x, e in enumerate(l):
    print("[%d] %d" % (x,e))
'''

def divide(x,y):
     try:
       result = (x/y)
     except ZeroDivisionError:
        print("Por favor, nao utilize zeros!")
     except:
       print("\033[91m Algo deu errado...")
     else:
       print(f"Seu resultado é: {result}")
     finally:
       print("\033[92m Vamos de novo]")
divide(13,0)


    


    

