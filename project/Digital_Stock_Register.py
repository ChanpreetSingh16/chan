import matplotlib.pyplot as plt
import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
print("Welcome to the Digital Stock Register. v1.0-jun26")

def cmdmenu1():
    print(f"\n\n{'Actions':<20}{'Commands':<8}")
    print("-"*28)
    print(f"{'Items Related':<20}{'1':<8}")
    print(f"{'Categories Related':<20}{'2':<8}")
    print(f"{'Vendors Related':<20}{'3':<8}")
    print(f"{'Employees Related':<20}{'4':<8}")
    print(f"{'Departments Related':<20}{'5':<8}")
    print(f"{'Issuing Related':<20}{'6':<8}")
    print(f"{'Returning Related':<20}{'7':<8}")
    print(f"{'Exit':<20}{'0':<8}\n")
def genum(a,b):
    if a == "cat":
        tab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
    elif a == "ven":
        tab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
    elif a == "dep":
        tab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    elif a == "emp":
        tab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep = ",")
    num = f"{tab.shape[0]+1:0{b}d}"
    return num

#Categories
def addtocat():
    cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
    name=input("Please enter Category Name  ")
    code="C"+str(genum("cat",3))
    b=0
    cats=cattab["Category"]
    while b == 0:
        for j in range(0,cattab.shape[0]):
            if cats[j].lower() != name.lower():
                pass
            else:
                while cats[j].lower() == name.lower():
                    name = input("This Category already exists, please enter new category   ")
        b=1
    cattab.loc[cattab.shape[0]] = [ code, name]
    cattab.to_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep=",", index=False)
    print(f"Category {name} with code {code} added successfully!")
def catser(d):
    cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
    codes=cattab["Code"]
    cats=cattab["Category"]
    l=[]
    c=input("You want to search by what?[Category(cat)/Code(cod)]").lower()
    if c=="cat":
        for i in range(0,cattab.shape[0]):
            if d.lower() in cats[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(cattab.iloc[l])
        else:
            print("\nNo resluts.")
    elif c=="cod":
        for i in range(0,cattab.shape[0]):
            if d.lower() in codes[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(cattab.iloc[l])
        else:
            print("\nNo resluts.")
def updatecat():
    old=input("Enter Category name to be updated  ")
    new=input("Enter new Category name  ")
    cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
    cats=cattab["Category"]
    codes=cattab["Code"]
    l=""
    for i in range(0, cattab.shape[0]):
        if cats[i] == old:
            l = i
            break
    if l != "":
        cattab.loc[l, "Category"] = new
        cattab.to_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep=",", index=False)
        print(f"Category {old} updated to {new} at Code {codes[l]} successfully!")
    elif l == "":
        print(f"Category {old} not found.")

#Vendors
def addtoven():
    ventab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
    name=input("Please enter Vendor Name  ")
    code="V"+str(genum("ven",3))
    b=0
    vens=ventab["Vendor Name"]
    while b == 0:
        for j in range(0,ventab.shape[0]):
            if vens[j].lower() != name.lower():
                pass
            else:
                while vens[j].lower() == name.lower():
                    name = input("This Vendor already exists, please enter new Vendor   ")
        b=1
    ventab.loc[ventab.shape[0]] = [ code, name]
    ventab.to_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep=",", index=False)
    print(f"Vendor {name} with ID {code} added successfully!")
def updateven():
    old=input("Enter Vendor name to be updated  ")
    new=input("Enter new Vendor name  ")
    ventab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
    vens=ventab["Vendor Name"]
    codes=ventab["ID"]
    l=""
    for i in range(0, ventab.shape[0]):
        if vens[i] == old:
            l = i
            break
    if l != "":
        ventab.loc[l, "Vendor Name"] = new
        ventab.to_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep=",", index=False)
        print(f"Vendor name {old} updated to {new} at ID {codes[l]} successfully!")
    elif l == "":
        print(f"Vendor {old} not found.")
def venser(d):
    ventab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
    codes=ventab["ID"]
    vens=ventab["Vendor Name"]
    l=[]
    c=input("You want to search by what?[Vendor Name(name)/Vendor ID(id)]").lower()
    if c=="name":
        for i in range(0,ventab.shape[0]):
            if d.lower() in vens[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(ventab.iloc[l])
        else:
            print("\nNo resluts.")
    elif c=="id":
        for i in range(0,ventab.shape[0]):
            if d.lower() in codes[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(ventab.iloc[l])
        else:
            print("\nNo resluts.")

#Departments
def addtodep():
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    name=input("Please enter Department Name  ")
    code="D"+str(genum("dep",3))
    b=0
    deps=deptab["Department"]
    while b == 0:
        for j in range(0,deptab.shape[0]):
            if deps[j].lower() != name.lower():
                pass
            else:
                while deps[j].lower() == name.lower():
                    name = input("This Department already exists, please enter new Department   ")
        b=1
    deptab.loc[deptab.shape[0]] = [ code, name]
    deptab.to_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep=",", index=False)
    print(f"Department {name} with ID {code} added successfully!")
def updatedep():
    old=input("Enter Department name to be updated  ")
    new=input("Enter new Department name  ")
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    deps=deptab["Department"]
    codes=deptab["ID"]
    l=""
    for i in range(0, deptab.shape[0]):
        if deps[i] == old:
            l = i
            break
    if l != "":
        deptab.loc[l, "Department"] = new
        deptab.to_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep=",", index=False)
        print(f"Department name {old} updated to {new} at ID {codes[l]} successfully!")
    elif l == "":
        print(f"Department {old} not found.")
def depser(d):
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    codes=deptab["ID"]
    deps=deptab["Department"]
    stat=deptab["Status"]
    l=[]
    c=input("You want to search by what?[Department(1)/Department ID(2)/Status(3)]").lower()
    if c=="1":
        for i in range(0,deptab.shape[0]):
            if d.lower() in deps[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(deptab.iloc[l])
        else:
            print("\nNo resluts.")
    elif c=="2":
        for i in range(0,deptab.shape[0]):
            if d.lower() in codes[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(deptab.iloc[l])
        else:
            print("\nNo resluts.")
    elif c=="3":
        for i in range(0,deptab.shape[0]):
            if d.lower() == stat[i].lower():
                l.append(i)
            else:
                pass
        if len(l) != 0:
            print("\n")
            print(deptab.iloc[l])
        else:
            print("\nNo resluts.")
    else:
        print("Invalid Choice.")
def changedepstat():
    dept=input("Enter Department ID")
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    deps=deptab["ID"]
    stat=deptab["Status"]
    l=""
    for i in range(0, deptab.shape[0]):
        if deps[i] == dept:
            l = i
            break
    if l != "":
        ask=input("Enter new status of the Department.[Active(1)/Inactive(2)]")
        if ask == "1":
            a="Active"
        elif ask == "2":
            a="Inactive"
        else:
            print("\nInvalid choice\n.")
            return
        deptab.loc[l, "Status"] = a
        deptab.to_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep=",", index=False)
        print(f"Status of Department with ID {dept} changed to {a} successfully!")
    elif l == "":
        print(f"\nDepartment ID {dept} not found.")
#Employees
def checkphn(p):
    p=str(p)
    if len(p) != 10:
        while len(p) != 10:
            p=input("Please enter correct phone number of 10 digits.  ")
    return int(p)
def addtoemp():
    emptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep = ",")
    name=input("Please enter Employee Name  ")
    phno=int(input("Enter Phone Number   "))
    phno=checkphn(phno)
    empp=list(emptab["Phone No."])
    if phno in empp:
        while phno in empp:
            print("Employee with given phone number(s) already exists.")
            phno = str(input("Please enter valid phone number"))
            phno=checkphn(phno)
    deptn = input("Enter Deparment Name  ").lower()
    code="E"+str(genum("emp",4))
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    codes=list(deptab["ID"])
    deps=list(deptab["Department"])
    l=[]
    for i in range(0,deptab.shape[0]):
        if deptn == deps[i].lower():
            l.append(i)
    if len(l) == 0:
        while len(l)==0:
            print(f"{deptn} Department not found.")
            deptn = input("Enter Correct Deparment Name  ").lower()
            for i in range(0,deptab.shape[0]):
                if deptn == deps[i].lower():
                    l.append(i)
    deptid=codes[l[0]]
    emptab.loc[emptab.shape[0]] = [ code, name, deptid, "Active", phno]
    emptab.to_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep=",", index=False)
    print(f"Employee {name} with ID {code}, Department ID {deptid} and Phone No.(s) {phno} added successfully!")
def updateemp():
    emptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep = ",")
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    codes=emptab["Emp. ID"]
    iD=input("Enter Employee ID")
    if iD not in list(codes):
        while iD not in list(codes):
            iD = input("Employee not found, Please enter correct ID  ")
    l=""
    for i in range(0, len(list(codes))):
        if list(codes)[i] == iD:
            l=i
            break
    para=input("What you want to update?[Name(1)/Status(2)/Phone Numbers(3)/Department(4)")
    if para == "1":
        n=input("Enter new Name")
        emptab.loc[l, "Emp. Name"] = n
    elif para == "2":
        ask=input("Enter the Status you want to set.[Active(1)/Retired(2)/Suspended(3)/Dismissed(4)]  ")
        if ask not in "1234":
            while ask not in "1234":
                ask=input("Please enter valid choice   ")
        dicti={"1":"Active","2":"Retired","3":"Suspended","4":"Dismissed"}
        emptab.loc[l, "Status"]=dicti[ask]
    elif para == "3":
        phno=int(input("Enter Phone Number   "))
        phno=checkphn(phno)
        empp=list(emptab["Phone No."])
        empp.pop(l)
        if phno in empp:
            while phno in empp:
                print("Employee with given phone number(s) already exists.")
                phno = int(input("Please enter valid phone number"))
                phno=checkphn(phno)
        emptab.loc[l, "Phone No."]=phno
    elif para == "4":
        deps=list(deptab["Department"])
        deptn=input("Enter New Department Name").lower()
        k=[]
        for i in range(0,len(deps)):
            if deptn.lower() == deps[i].lower():
                k.append(i)
            else:
                pass
        if len(k) == 0:
            while len(k)==0:
                print(f"{deptn} Department not found.")
                deptn = input("Enter Correct Deparment Name  ").lower()
                for i in range(0,len(deps)):
                    if deptn.lower() == deps[i].lower():
                        k.append(i)
                    else:
                        pass
        deptid=list(deptab["ID"])[k[0]]
        emptab.loc[l, "Dept. ID"]=deptid
    else:
         print("Inavlid Choice")
         return
    emptab.to_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep=",", index=False)
    print(f"Employee Data updated successfully!")
def empser(a):
    emptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep = ",")
    deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
    para=input("What are the parameters you want to search by?[Name(1)/Status(2)/Phone Numbers(3)/Department Name(4)")
    if para in "12":
        if para == "1":
            emps=list(emptab["Emp. Name"])
        elif para == "2":
            emps=list(emptab["Status"])
        k=[]
        for i in range(0, len(emps)):
            if a.lower() in emps[i].lower():
                k.append(i)
        if len(k) != 0:
            print("\n")
            print(emptab.iloc[k])
        else:
            print("\nNo Results.\n")
    elif para in "34":
        if para == "3":
            emps=list(emptab["Phone No."])
            k=[]
            for i in range(0, len(emps)):
                if str(a) in str(emps[i]):
                    k.append(i)
            if len(k) != 0:
                print("\n")
                print(emptab.iloc[k])
            else:
                print("\nNo Results.\n")
        elif para == "4":
            deptids=list(deptab["ID"])
            deptnames=list(deptab["Department"])
            emps=list(emptab["Dept. ID"])
            b=None
            for i in range(0,len(deptnames)):
                if a.lower() in deptnames[i].lower():
                    b=i
                    break
            a=deptids[b]
            k=[]
            for i in range(0, len(emps)):
                if str(a) == str(emps[i]):
                    k.append(i)
            if len(k) != 0:
                print("\n")
                print(emptab.iloc[k])
            else:
                print("\nNo Results.\n")


cmd=0
while cmd != "0":
    cmdmenu1()

    cmd=input("Please Enter Command  ")

    if cmd == "1":
        print("")
    elif cmd ==  "2":
        catcmd = 0
        while catcmd != "0":
            print(f"\n\n{'Actions':<25}{'Commands':<8}")
            print("-"*33)
            print(f"{'Show Categories':<25}{'1':<8}")
            print(f"{'Search Categories':<25}{'2':<8}")
            print(f"{'Add Categories':<25}{'3':<8}")
            print(f"{'Update Categories':<25}{'4':<8}")
            print(f"{'Exit':<25}{'0':<8}\n")
            catcmd = input("Please Enter Command  ").lower()
            
            if catcmd == "1":
                cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
                print("\n")
                print(cattab)
            elif catcmd == "3":
                addtocat()
                askcata=input("Want to add more[Yes(Y)/No(N)]?")
                while askcata.lower() == "y":
                    addtocat()
                    askcata=input("Want to add more[Yes(Y)/No(N)]?")
            elif catcmd == "2":
                q = input("Enter Query")
                catser(q)
            elif catcmd == "4":
                updatecat()
            elif catcmd == "0":
                print("\nExited Category menu.\n")
    elif cmd ==  "3":
        vencmd = 0
        while vencmd != "0":
            print(f"\n\n{'Actions':<25}{'Commands':<8}")
            print("-"*33)
            print(f"{'Show Vendors':<25}{'1':<8}")
            print(f"{'Search Vendors':<25}{'2':<8}")
            print(f"{'Add Vendors':<25}{'3':<8}")
            print(f"{'Update Vendors':<25}{'4':<8}")
            print(f"{'Exit':<25}{'0':<8}\n")
            vencmd = input("Please Enter Command  ").lower()
            
            if vencmd == "1":
                ventab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
                print("\n")
                print(ventab)
            elif vencmd == "3":
                addtoven()
                askvena=input("Want to add more[Yes(Y)/No(N)]?")
                while askvena.lower() == "y":
                    addtoven()
                    askvena=input("Want to add more[Yes(Y)/No(N)]?")
            elif vencmd == "2":
                q = input("Enter Query")
                venser(q)
            elif vencmd == "4":
                updateven()
            elif vencmd == "0":
                print("\nExited Vendors Menu.\n")
    elif cmd ==  "5":
        depcmd = 0
        while depcmd != "0":
            print(f"\n\n{'Actions':<25}{'Commands':<8}")
            print("-"*33)
            print(f"{'Show Departments':<25}{'1':<8}")
            print(f"{'Search Departments':<25}{'2':<8}")
            print(f"{'Add Departments':<25}{'3':<8}")
            print(f"{'Update Departments':<25}{'4':<8}")
            print(f"{'Exit':<25}{'0':<8}\n")
            depcmd = input("Please Enter Command  ").lower()
            
            if depcmd == "1":
                deptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/dept.csv", sep = ",")
                print("\n")
                print(deptab)
            elif depcmd == "3":
                addtodep()
                askdepa=input("Want to add more[Yes(Y)/No(N)]?")
                while askdepa.lower() == "y":
                    addtodep()
                    askdepa=input("Want to add more[Yes(Y)/No(N)]?")
            elif depcmd == "2":
                q = input("Enter Query")
                depser(q)
            elif depcmd == "4":
                what=input("What you want to update?(Department Name(dept)/Department Status(stat)").lower()
                if what == "dept": 
                    updatedep()
                elif what == "stat":
                    for i in range(0,5):
                        word=input("Please Enter Password")
                        if word == "Reader987":
                            changedepstat()
                            break
                        else:
                            if i==4:
                                print("\nAll attempts finished and failed.")
                            else:
                                print(f"\nWrong Password, Try again. Attempts left - {5-(i+1)}")
            elif depcmd == "0":
                print("\nExited Departments Menu.\n")
    elif cmd ==  "4":
        empcmd = 0
        while empcmd != "0":
            print(f"\n\n{'Actions':<25}{'Commands':<8}")
            print("-"*33)
            print(f"{'Show Employees':<25}{'1':<8}")
            print(f"{'Search Employees':<25}{'2':<8}")
            print(f"{'Add Employees':<25}{'3':<8}")
            print(f"{'Update Employees':<25}{'4':<8}")
            print(f"{'Exit':<25}{'0':<8}\n")
            empcmd = input("Please Enter Command  ").lower()
            
            if empcmd == "1":
                emptab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/emp.csv", sep = ",")
                print("\n")
                print(emptab.to_string())
            elif empcmd == "3":
                addtoemp()
                askempa=input("Want to add more[Yes(Y)/No(N)]?")
                while askempa.lower() == "y":
                    addtoemp()
                    askempa=input("Want to add more[Yes(Y)/No(N)]?")
            elif empcmd == "2":
                q = input("Enter Query")
                empser(q)
            elif empcmd == "4":
                for i in range(0,5):
                    word=input("Please Enter Password")
                    if word == "Reader987":
                        updateemp()
                        break
                    else:
                        if i==4:
                            print("\nAll attempts finished and failed.")
                        else:
                            print(f"\nWrong Password, Try again. Attempts left - {5-(i+1)}")
            elif empcmd == "0":
                print("\nExited Employees Menu.\n")
    elif cmd == "0":
        print("Thank You")
    




#https://www.programiz.com/online-compiler/4udhsWOpQHZl7
#depart and pho no. update
