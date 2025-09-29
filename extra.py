import math

def es_entero(number:float):
    entero=int(number)
    if(number-entero)==0:
        return True
    else:
        return False
    

expression=input().split()
print(expression)

relevant=list(expression[2])

a=""
position=0
for caracter in relevant:
    #print(caracter)
    if caracter!="f":
        a+=caracter
        position+=1
    else:
        break


b=""
for i in range(position+4,len(relevant)):
    #print(caracter)
    if relevant[i]!=")":
        b+=relevant[i]
    else:
        break


driving_exponent=""
relevant_inverse=relevant[::-1]
for caracter in relevant_inverse:
    if caracter!="^":
        driving_exponent+=caracter
    else:
        break

print(a)
print(b)
print(driving_exponent)

k:float=math.log(int(a),int(b))

#print(k)

impresion:str=""

#Verificación de casos
if k>int(driving_exponent):
    if(es_entero(k)):
        cadena1="O(n^"+str(int(k))+"))"
        impresion=cadena1

    else:
        cadena1="O(n^log_("+str(b)+")("+str(a)+"))"
        impresion=cadena1

elif k<int(driving_exponent):
    cadena1="O(n^"+driving_exponent+"))"
    impresion=cadena1

else:
    if int(k)==1:
        cadena1="O(lg(n))"
        impresion=cadena1

    else:
        cadena1="O(n^"+k+""


print(impresion)

