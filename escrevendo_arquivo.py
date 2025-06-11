try:
    arquivo=open("binary", "jpg", "rb")
    print(type(arquivo))
except:
    print('arquivo não existe!-_- ')