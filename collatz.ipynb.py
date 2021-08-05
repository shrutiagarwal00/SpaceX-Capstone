import random
result=[]
step=0
c=1

#result.append(int(input("Enter a seed number :: ")))
#result.append(int(random.random()*1000000000000000))


while(c==1):
    if(result[-1]%2==0):
        result.append(result[-1]//2)
    else:
        result.append(result[-1]*3+1)
    step+=1
    if result[-1]==1 and result[-2]==2 and result[-3]==4:
        c=0
    else:
        continue

print(result,"\n\nNo of steps taken :: ",step)