import time

t:int=int(input())


def check(arr1, arr2):
    result=True
    for i in range(len(arr1)):
        if(arr1[i]+arr2[i])%3==0:
            continue
        else:
            result=False

    return result


for i in range(t):

    size=int(input())

    arr=list(map(int,input().split()))

    new=arr[:]

    result=[]

    flag=False
    while(not(flag)):
        print(new)
        comprobation=check(arr,new)
        print(comprobation)
        time.sleep(5)
        if(comprobation):
            print(*new)
            flag=True

        else:
            new=new[1:]+new[:1]






