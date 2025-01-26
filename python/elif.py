#if n is odd print weird
#if n is even and in range of 2 to 5 orint not weird
#if n is even and in range of 6 to 20 print weird
#if n is even and greater than 20 print not weird 



n=int(input("enter the number"))
if n%2==0 and n>20 :
    print("not weird")
elif n%2==0 and n>=6 and n<=20 :
    print("weird")
elif n%2==0 and n>=2 and n<=5 :
    print("not weird")
else :
    print("weird")