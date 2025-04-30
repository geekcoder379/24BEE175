class Matrix:
    def __init__(self,flag):
        if(flag==0):
            self.I = [[0,0,0],[0,0,0],[0,0,0]]
        else:
            self.I = flag
    
    def printM(self):
        print(self.I)

    def __add__(self,x):
        obA = Matrix(0)
        for i in range(len(self.I)):
            for j in range(len(self.I[0])):
                obA.I[i][j] = self.I[i][j] + x.I[i][j]
        return obA
        '''i00 = self.I[0][0]+x.I[0][0]
        i01 = self.I[0][1]+x.I[0][1]
        i02 = self.I[0][2]+x.I[0][2]
        i10 = self.I[1][0]+x.I[1][0]
        i11 = self.I[1][1]+x.I[1][1]
        i12 = self.I[1][2]+x.I[1][2]
        i20 = self.I[2][0]+x.I[2][0]
        i21 = self.I[2][1]+x.I[2][1]
        i22 = self.I[2][2]+x.I[2][2]
        return Matrix([[i00,i01,i02],[i10,i11,i12],[i20,i21,i22]])'''

    def __del__(self):
        print("Memory will free")

obj1 = Matrix([[1,0,0],[0,1,0],[0,0,1]])
obj1.printM()

obj2 = Matrix([[2,0,0],[0,2,0],[0,0,2]])
obj2.printM()

obj3 = obj1 + obj2
obj3.printM()