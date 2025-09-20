t:int=int(input()) 
for i in range(t):
    score=0
    conditions,limit=map(int,input().split())
    actual_minute=0
    position=0

    for j in range(conditions):
        c,p=map(int,input().split())
        if((c-actual_minute)%2==0 and (position-p)%2==0):
            score+=c-actual_minute
            actual_minute=c
            position=p
        
        elif((c-actual_minute)%2==0 and (position-p)%2!=0):
            score+=c-actual_minute-1
            actual_minute=c
            position=p  
        
        elif((c-actual_minute)%2!=0 and (position-p)%2!=0):
            #print("Entre donde debía")
            score+=c-actual_minute
            #print("c es ",str(c))
            #print("actual minute es ",str(actual_minute))
            #print("score es  "+str(score))
            actual_minute=c
            position=p

        else:
            score+=c-actual_minute-1
            actual_minute=c
            position=p

    if(actual_minute<limit):
        #print("escore actual es ",str(score))
        #print("actual minute es ",str(actual_minute))
        #print("limit es ",str(limit))
        score+=limit-actual_minute

    
    print(score)


