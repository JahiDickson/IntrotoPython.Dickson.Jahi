sum=0

for x in range(1,1000):
    if x%3==0:
        if x%5==0:
            sum=sum+x
        else:
            sum=sum+x
    elif x%5==0:
        sum=sum+x
    else:
        sum=sum
print sum