def merge(left:list,right:list):
    result=[]
    #Esta funcion se encarga de combinar los dos arrays en orden, teoricamente esta diseñada
    #para que ambas listas tengan unicamente 1 elemento. (si se hace la recursividad correspondiente en la función
    #final)

    while len(right)>0 and len(left)>0:
        if left[0]<=right[0]:
            result.append(left[0])
            left.pop(0)

        else:
            result.append(right[0])
            right.pop(0)

    while len(right)>0:
        result.append(right[0])
        right.pop(0)

    while len(left)>0:
        result.append(left[0])
        left.pop(0)

    return result


def merge_sort(array:list):
    #Esta función se encarga de dividir el array a la mitad hasta que queden solo grupos de 1 elemento para
    #llamar a la siguiente función

    if len(array)<2:
        return array

    mid=len(array)//2

    return merge(left=merge_sort(array[:mid]),right=merge_sort(array[mid:]))


print(merge_sort([17, 9, 5, 12, 3, 8, 14, 7, 11, 6, 19, 1]))

