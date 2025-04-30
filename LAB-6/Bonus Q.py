emp = [(101,'Amit',35,'HR',10000),(103,'Asit',37,'IT',12000),(102,'Veer',36,'Mkt',11000)]
print(emp)
department=(("HR","Human Resource","F-block"),("IT","Information Technology","C-Block"),("Mkt","Marketing","D-Block"))

while 1:
    print("1 == Filter Employee Name by Department")
    print("2 == Sort Employee by salary")
    print("3 == Get the employee with highest salary")
    print("4 == Update the salary of employee")
    print("5 == Department Details")
    print("6 == Exit")
    c=int(input("Enter your choice : "))

    if(c==2):
        # sort employee by salary
        l1 = [i[4] for i in emp]
        l1.sort()
        l2 = []
        for i in l1:
            for j in emp:
                if(isinstance(j,tuple)):
                    if(i==emp[4]):
                        l2.append(i)
        print("Sort employee by salary : ",l2)

    elif(c==1):
        # filter employee names by dept
        l3 = []
        role = input("Enter a role : ")
        for i in emp:
            if(isinstance(i,tuple)):
                if(role==i[3]):
                    l3.append(i)
        print(l3)

    elif(c==3):
        # Find the emp with highest salary
        for j in emp:
            if(isinstance(j,tuple)):
                if(l1[len(l1)-1]==j[4]):
                   print("Highest salary employee : ",j)

    elif(c==4):
        # Update emp salary
        l4 = []
        no = 0
        id = int(input("Entre a id of update salary : "))
        upd_sal = int(input("Entre a salary : "))
        for i in emp:
            if(isinstance(i,tuple)):
                if(id==i[0]):
                    l4 = list(emp[no])
                    l4[4] = upd_sal
                    emp[no] = tuple(l4)
            no += 1
        print("Update employee salary : ",emp)

    elif(c==5):
        dept = input("Enter which department details you want:")
        for i in department:
            if dept==i[0]:
                print("The detail of the department are ")
                print("Full form =",i[1])
                print("Location",i[2])

    elif(c==6):
        break
    else:
        print("Invalid enter.")
























