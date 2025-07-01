'''
import os
os.getcwd()

print(os.getcwd())
'''
'''
import os 
try:
    os.mkdir("d")
    os.mkdir("e")
    os.mkdir("f")
except:
    print("error:/")
'''
'''
import os

arquivo_path="diretório"

try:   os.rmdir(arquivo_path)
    print(f"""\033[0;32m Pasta '{arquivo_path}'removida com sucesso! ;D""")
except FileNotFoundError:
    print(f"""\032[0;32m Pasta '{arquivo_path}'removida com sucesso! ;D""")
except OSError:
    print(f"""\033[0;32m Pasta '{arquivo_path}'não há arquivo! :(""")
'''
def le_binario():
    try:
        with open("binary.jpg", "rb") as fs1:
          dados = fs1.read()  
          print(type(dados))
        with open("teste01.jpg", "wb") as fs2:
           fs2.write()

    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
        print("OK! ~_~")
    
    import os

    try:
        os.remove("teste02.jpg")
        print(f"Excluido {"teste1.jpg"}")
    except:
        print("não foi possivel")
    
le_binario()

