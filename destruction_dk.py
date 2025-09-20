import heapq

t:int=int(input())

for i in range(t):
    counter=0
    n=int(input())
    dt=list(map(int, input().split()))
    on=False

    size=len(dt)

    a=[x for x in dt if x%2==0]
    b=[x for x in dt if x%2==1]

    if(len(b)==0):
        print(0)
        continue

    b_max=max(b)
    counter+=b_max
    b.remove(b_max)
    on=True

    #print("antes de pares " +str(counter))

    counter+=sum(a)

    if(len(b)==0):
        print(counter)
        continue


    on=False
    b.remove(min(b))

    size_b=len(b)
    invert=[-x for x in b]
    heapq.heapify(invert)

    c=0

    while len(b)>c:
        if(not(on)):
            counter+=-heapq.heappop(invert)
            on=True
            c+=1

        else:
            c+=1
            on=False


    print(counter)






