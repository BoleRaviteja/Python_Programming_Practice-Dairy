Name=input('Enter name:')
number=input('Enter Account Number: ')
units=int(input('Enter no.of Units'))
if units<=100:
    bill=units*1.5
elif units<=200:
    bill=(100*1.5)+(units-100)*2.5
elif units<=500:
    bill=(100*1.5)+(100*2.5)+(untis-200)*4
else:
    bill=(100*1.5)+(200*2.5)+(300*4)+(units-500)*6
bill+=50
print(Name)
print(number)
print(units)
print(bill)
