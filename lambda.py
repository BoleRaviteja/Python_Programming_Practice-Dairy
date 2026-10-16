#lambda function :anonymous function

n=lambda x:x*x
print(n(5))

add=lambda a,b:a+b
print(add(10,30))

sub=lambda a,b:a-b

x=int(input())
y=int(intput())
print('subtraction',sub(x,y))

#find even or odd

x=lambda n:1 if n%2==0 else 0

print(x(10))

#find big number

big=lambda a,b,c,d: a if a>b and a>c and a>d else b if b>c and b>d else c if c>d else d
print('big number',big(10,4,67,45))
