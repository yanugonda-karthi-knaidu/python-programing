#program for right half pyramid 
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()  #print() is used to print in a new line
        


#program for left half pyramid
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("*",end=" ")
    print()  #print() is used to print in a new line
        

#program for full pyramid
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()  #print() is used to print in a new line
    
    
#program for inverted pyramid
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print("*",end=" ")
    print()  #print() is used to print in a new line
    for k in range(1,i+1):
      print(" ",end=" ")
            
#program for 

            