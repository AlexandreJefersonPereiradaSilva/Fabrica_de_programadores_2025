import types

def diz_o_tipo(a):
  tipo = type(a)
  if tipo == str:
    return("String")
  elif tipo == list:
    return("Lista")
  elif tipo == dict:
    return("Dicionário")
  elif tipo == int:
    return("Número inteiro")
  elif tipo == float:
    return("Número decimal")
  elif tipo == types.FunctionType:
    return("Função")
  elif tipo == types.BuiltinFunctionType:
    return("Função interna")
  else:
    return(str(tipo))

nome=input()



print(diz_o_tipo("Olá, mundo!"))
print(diz_o_tipo(2))
print(diz_o_tipo(17))
print(diz_o_tipo("LOL"))
print(diz_o_tipo([5]))
print(diz_o_tipo(5.9))
print(diz_o_tipo(input))
print(diz_o_tipo())

