#program for calculation game using random module
score=0 #global variable
import random
def level2():
    print('you entered level2')
    global score
ch=0
ctr=0
ctr1=0
while ch<10:
    x=random.randint(1,10)
    y=random.randint(1,20)
    k=int(input(f"{x}+{y}="))

    if k==x+y:
        print('sucess..!')
        score+=10
        ctr+=1
    else:
        print('wrong..!')
        ctr+=1
        ch+=1
        if ctr1==3:
           print('you have fail..!')
           break
           print("final score",score)

#main program    
ch=0
ctr=0
ctr1=0
while ch<10:
    x=random.randint(1,10)
    y=random.randint(1,10)
    k=int(input(f"{x}+{y}="))

    if k==x+y:
        print('sucess..!')
        score+=10
        ctr+=1
    else:
      print('wrong..!')
      ctr+=1
      ch+=1
      if ctr1==3:
         print('improve your self try agin..!')
         break
if ctr>5:
   print('you reached level1')
   print('your score is;',score)
   k=input('shall to move level2[y/n]')
   if k=='y':
       level2()



         
    
      
