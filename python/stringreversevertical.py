# write a pyhton program to print userinput string in reverse vertical order

n=str(input("enter the string : "))
n=n[::-1]
print(n)
for i in range(len(n)):
    print(n[i])
    