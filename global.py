#local variable vs global variables
n=10
k=10
def f1():
    x=100
    global k
    print(x)
    print(n)
    k=k+10
    print('global:',k)

#main program
f1()
n=n+10
print(n)
print('k value',k)
