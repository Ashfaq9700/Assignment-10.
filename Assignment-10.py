#1. Write a python script to print the first 10 multiples of 5.
"""
userInput = 5
count = 1
for x in range(1,11):
    print(x*userInput)
"""
# 2. Write a python script to print first 10 multiples of N
"""
userInput = int(input("Enter Number :"))
count = 1
for x in range(1,11):
    print(x*userInput)
"""

# 3. Write a python script to print first M multiples of N.
"""n_multi = int(input("Enter Multiplication Number : "))
m_multi = int(input("How Many Multiple values you want :"))
                            
for x in range(1,m_multi+1):
    print(n_multi*x)
"""

# 4. Write a python script to print the first 10 multiples of N in reverse order.
"""userInput = int(input("multiples of N :"))

for i in range(10, 0, -1):
    print(i*userInput)
"""

#5. Write a python script to print table of user’s choice
"""
userInput = int(input("Enter Table to print : "))
for i in range(1,11):
    print(i*userInput)
"""

#6. Write a python script to print first N even natural numbers.
"""
n = int(input("How Many Even Natural Numbers :"))
n = n*2
for x in range(2,n+1,2):
    print(x)
"""

#7. Write a python script to print first N odd natural numbers
"""
n = int(input("Enter N : "))
n = n*2
for i in range(1,n+1,2):
    print(i)
"""
#8. Write a python script to print squares of first N natural numbers.
"""
n = int(input("Enter N numbers : "))
for i in range(1,n+1):
    print(i**2)
"""
# 9. Write a python script to print cubes of first N natural numbers.
"""
n = int(input("Enter N numbers : "))
for i in range(1,n+1):
    print(i**3)
"""
#10. Write a python script to display all prime numbers within a range.
# range start = 15 end = 45 
# a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).
for i in range(5,50+1):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        print(i)




        


