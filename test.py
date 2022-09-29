
lista = ['[a,b,c]', '[d,e,f]']
resultado = []
for elemento in lista:    
    resultado.append(elemento.strip('[]').split(','))

print(resultado)
print(type(resultado))