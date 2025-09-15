def factorial(n):
    if n<2:
        return 1
    else:
        return n * factorial(n-1)
a=int(input('Enter no. for which you want to calculate factorial'))
x=factorial(a)
print('Factorial is ',x)
    