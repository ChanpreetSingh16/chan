import matplotlib.pyplot as plt
import pandas as pd

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
    l=[]
    c=input("You want to search by what?[Department(dept)/Department ID(id)]").lower()
    if c=="dept":
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
    elif c=="id":
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
            print(f"{'Search Categories(name)':<25}{'2':<8}")
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
                updatedep()
            elif depcmd == "0":
                print("\nExited Departments Menu.\n")
    elif cmd == "0":
        print("Thank You")
    




#https://www.programiz.com/online-compiler/4udhsWOpQHZl7
