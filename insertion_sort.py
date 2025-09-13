def insertion_sort(array:list):
    l=len(array)
    for i in range(1,l):
        insert_index=i
        insert_value=array[i]
        while insert_index>0 and insert_value<array[insert_index-1]:
            array[insert_index-1],array[insert_index]=insert_value,array[insert_index-1]
            insert_index-=1

    return array

print(insertion_sort([14, 15, 13, 12, 14, 16, 13, 15, 14, 12, 13, 16]))


def insertion_sort_2(array:list):
    l=len(array)
    for i in range(1,l):
        insert_index=i
        insert_value=array[i]
        while insert_index>0 and insert_value<array[insert_index-1]:
            array[insert_index]=array[insert_index-1]
            insert_index-=1

        array[insert_index]=insert_value

    return array

print(insertion_sort_2([14, 15, 13, 12, 14, 16, 13, 15, 14, 12, 13, 16]))

#Ambas funciones sirven, la segunda corresponde a una implementación mas estrica del video y la primera a una propia