## program for taking user input and printing the string no of times as per user input

'''s=str(input("enter the string : "))
n=int(input("enter no of times:"))
for i in range (0,n):
    print(s) '''

def numbers(abc):
    s=str(input("enter the string : "))
    n=int(input("enter no of times:"))
    print((s+"")*n)
numbers('abc')