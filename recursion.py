#Recursion :function can call itself is called recursion

#factorial of a number
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

#main program
n=int(input('enter a number'))
print(factorial(n))

#sum of natural numbers
def sum_of_natural_numbers(n):
    if n==0:
        return 0
    else:
        return n + sum_of_natural_numbers(n-1)

#main program
print(sum_of_natural_numbers(10))
