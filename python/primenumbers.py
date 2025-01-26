x=1
y=50
print("prime numbers between ",x,"and",y,"are :")
for num in range(x,y+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
          print(num)
