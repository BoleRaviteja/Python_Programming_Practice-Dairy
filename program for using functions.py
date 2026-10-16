#program for using functions

def prime():
    n=int(input('enter a number:'))
    i=1
    ctr=0
    while i<n:
        if n%i==0:
            ctr=1
        i+=1
    if ctr==2:
        print('prime number')
    else:
        print('not prime number')

def perfect():
    n=int(input('enter a number:'))
    i=1
    s=0
    while i<n:
        if n%

def sumofdigts():
     

def reverse():
    n=int(input('enter a number:'))
    s=0
    while n>0:
        d=n%10
        s=s*10+d
        n=n//10
    print('reverse order',s)

def palendrome():
    pass

def Armstrong():
    pass

def strong():
    pass

#main program
while True:
    print('1.prime')
    print('2.perfect')
    print('3.sumofnumbers')
    print('4.reverse')
    print('5.palendrome')
    print('6.Armstrong')
    print('7.strong')
    print('8.exit')

    ch=int(input('select your choice'))
    if ch==1:
        prime()
    elif ch==2:
        perfect()
    elif ch==3:
        sumofnumbers()
    elif ch==4:
        reverse()
    elif ch==5:
        palendrome()
    elif ch==6:
        Armstrong()
    elif ch==7:
        strong()
    elif ch==8:
        break
    else:
        print('invalid choice')
        
        
        
        
