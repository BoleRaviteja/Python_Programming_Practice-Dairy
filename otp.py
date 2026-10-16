import random
x=random.randint(10000,99999)
print('otp generation',x)
y=int(input('enter otp'))
if x==y:
      print('success')
else:
    print('invalid otp')

