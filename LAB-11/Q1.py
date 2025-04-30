'''class Mycomplex_number:
    n1_r = 4
    n1_i = 4
    n2_r = 5
    n2_i = 5
obj1 = Mycomplex_number()
print(obj1.n1_r,"+ i",obj1.n1_i)
print(obj1.n2_r,"+ i",obj1.n2_i)
print("Addition : ",obj1.n1_r+obj1.n2_r,"+ i",obj1.n1_i+obj1.n2_i)
print("Subtraction : ",obj1.n1_r-obj1.n2_r,"+ i",obj1.n1_i-obj1.n2_i)'''

class Complex_Number:
    def __init__(self,r=0,i=0):
        self.r = r
        self.i = i
        print("In init")

    def print_cn(self):
        if(self.i>=0):
            print(self.r,"+i",self.i)
        else:
            print(self.r,"-i",-self.i)

    def __add__(self,x=0):  #__name__ now it become sysytem define method
        a = self.r+x.r
        b = self.i+x.i
        return Complex_Number(a,b)
        '''ansob = Complex_Number()
        ansob.r = self.r+x.real
        ansob.i = self.i+x.i
        return ansob'''

    
    def __sub__(self,x=0):  #__sub__ = -
        a = self.r-x.r
        b = self.i-x.i
        return Complex_Number(a,b)
    
    def __mul__(self,y=0):  #__mul__ = *
        a = self.r*y.r - self.i*y.r  #(a+ib)*(n+im)=a*n-b*m+i(a*m+b*n)
        b = self.r*y.i + self.i*y.r
        return Complex_Number(a,b)
    
    def __truediv__(self,m=0):  #__truediv__ = /
        a = -(self.r*m.r+self.i*m.i)/(m.r**2+m.i**2)
        b = (self.r*m.i-self.i*m.r)/(m.r**2+m.i**2)
        return Complex_Number(a,b)
    
    def __del__(self):
        print("Memory will free")

cn1 = Complex_Number(1,1)
cn1.print_cn()

cn2 = Complex_Number(-2,-2)
cn2.print_cn()

obj1 = cn1 + cn2 #obj1 = cn1.__add__(cn2)
obj1.print_cn()

obj2 = cn1 - cn2 #obj2 = cn1.__sub__(cn2)
obj2.print_cn()

obj3 = cn1*cn2 #obj3 = cn1.__mul__(cn2)
obj3.print_cn()

obj4 = cn1/cn2 #obj4 = cn1.__truediv(cn2)
obj4.print_cn()