#program that takes n number of integers as input and print the maximum num, minimum num sum of all the numbrs

n=int(input("Enter the number of integers:"))
numbers = input("Enter the integers: ")
numbers = [int(x) for x in numbers.split()]
print("Maximum number is:", max(numbers))
print("Minimum number is:", min(numbers))
print("Sum of all numbers is:", sum(numbers))

    
    