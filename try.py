def syntactic(array, a):
    # array: Arreglo de los coeficientes del polinomio a dividir
    # a: termino independiente del divisor, por ejemplo, si tenemos como
    # dividendo "x-3" a=-3

    x=-a
    sub=0
    answer=[array[0]]
    for i in range(0, len(array)):
        if i==0:
            sub=x*array[i]
            continue

        result=array[i]+sub
        answer.append(result)
        sub=result*x

    return answer

#print(syntactic([-7,-8,5,-2],-2))

def divisores(numero):
    d=[]
    for i in range(1,numero+1):
        if (numero%i==0):
            d.append(i)
    return d



def minX(array):
    array.reverse()
    print(array)
    raices=divisores(array[0])
    print
    respuesta=[]
    if array[0]>0:
        # array: Arreglo de los coeficientes del polinomio a dividir
        # a: termino independiente del divisor, por ejemplo, si tenemos como
        # dividendo "x-3" a=-3

        for j in raices:

            x=j
            sub=0
            answer=[array[0]]
            for i in range(0, len(array)):
                if i==0:
                    sub=x*array[i]
                    continue

            result=array[i]+sub
            if(result<0):
                break
            

            answer.append(result)
            sub=result*x
    
        return answer[-1]
    


print(minX([0, -36, 0, 49, 0, -14, 0, 1]))







