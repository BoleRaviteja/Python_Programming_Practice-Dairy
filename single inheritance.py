# sample program using single inheritance

class parent:
    def F1(self):
        print("parent class")

class child(parent):
    def F2(self):
        print("child class")


#object declaration
x=child()
x.F1()
x.F2()
