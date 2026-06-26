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
    elif a == "itm":
        tab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item.csv", sep = ",")
    num = f"{tab.shape[0]+1:0{b}d}"
    return num

#Categories
def addtocat(a):
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
    if a == "i":
        return code
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
def addtoven(a):
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
    if a == "i":
        return code
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
#Items
def validate(d):
    dicti = {"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}
    
    while len(d) != 10 or d[2] != "/" or d[5] != "/":
        d = input("Please enter date in DD/MM/YYYY format  ")
    day = d[0:2]
    mon = d[3:5]
    year = int(d[6:10])
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        dicti["02"] = 29
    else:
        dicti["02"] = 28
    while mon not in dicti:
        mon = input("Please Enter Valid Month(MM)  ")

    while int(day) < 1 or int(day) > dicti[mon]:
        day = input("Please Enter Valid Day(DD)  ")

    d = day + "/" + mon + "/" + str(year)

    return d
def valiven(iD):
    ventab = pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
    venids = list(ventab["ID"])
    while iD != ";new" and iD not in venids:
        print(f"Vendor ID {iD} not found")
        iD=input("Please Enter correct ID or Enter the command ';new' to Add New Vendor  ")
    if iD == ";new":
        iD = addtoven("i")
    return iD
def valicat(iD):
    cattab = pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
    cats = list(cattab["Category"])
    nc=[]
    for i in range(0, len(cats)):
        nc.append(cats[i].lower())
    cats = nc
    while iD != ";new" and iD.lower() not in cats:
        print(f"Category {iD} not found")
        iD=input("Please Enter correct Category or Enter the command ';new' to Add New Category  ")
    catids = list(cattab["Code"])
    if iD == ";new":
        iD = addtocat("i")
    else:
        l=None
        for i in range(0,len(cats)):
             if iD.lower() == cats[i]:
                 l=i
                 break
        iD=catids[l]
    return iD
def venbill(a,b,c,d):
    a=str(a)
    itmtab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item.csv", sep = ",")
    bno = list(itmtab["Bill No."])
    venid = list(itmtab["Vendor ID"])
    comp = list(itmtab["Company Name"])
    name = list(itmtab["Name"])
    nc=[]
    for i in range(0, len(bno)):
        nc.append(str(bno[i]))
    bno = nc
    if a not in bno:
        return a
    else:
        l=[]
        for i in range(0,len(bno)):
            if a == bno[i]:
                l.append(i)
        for j in l:
           if b == venid[j] and c.lower() == comp[j].lower() and d.lower() == name[j].lower():
                return ";cancel"
        return a
def newitm():
    itmtab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item.csv", sep = ",")
    itmtab2 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep = ",")
    code="I"+str(genum("itm",4))
    name=input("Enter Item Name  ")
    quan=float(input("Enter quantity without units(if any)  "))
    price=float(input("Enter total amount in Rs.(Do not add the symbol 'Rs.' etc.)"))
    date=input("Enter date in the format DD/MM/YYYY  ")
    date=validate(date)
    venid=input("Enter Vendor ID or ';new' to Add New Vendor ")
    venid=valiven(venid)
    catid=input("Enter Category Name or ';new' to Add New Category  ")
    catid=valicat(catid)
    comp=input("Enter Company Name  ")
    billno=str(input("Enter Bill No.  "))
    billno=venbill(billno, venid, comp, name)
    if billno == ";cancel":
        print("\nThis item already exists.\n")
        return
    itmtab.loc[itmtab.shape[0]] = [ code, name, quan, price, date, billno, venid, comp, catid]
    itmtab.to_csv("C:/Users/HP/Downloads/chan project ip/item.csv", sep=",", index=False)
    print(f"Item {name} with ID {code},Company {comp}, Quantity {quan}, Price {price}, Bill No. {billno}, Vendor ID {venid}, Category Code {catid} on {date} added Successfully!")
    itmtab2.loc[itmtab2.shape[0]] = [ code, name, quan, "OK"]
    itmtab2.to_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep=",", index=False)
    print(f"Item {name} with ID {code}, Quantity {quan} and Status 'OK' added Successfully!")
def chkquan(iid, q):
    itmtab2 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep = ",")
    quans=float(list(itmtab2["Non-issued Quantity"])[iid])
    while float(q) > quans:
        q = input("Non-issued qunatity less than the entered quantity. Please enter correct quantity or ';cancel' to cancel the procedure  ")
        if q.lower() == ";cancel":
            return q
            break
    return float(q)
def adddishis():
    itmtab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item.csv", sep = ",")
    itmtab2 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep = ",")
    itmtab3 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item3.csv", sep = ",")
    iid=input("Enter Item ID  ")
    ids=list(itmtab["ID"])
    while iid not in ids :
        iid=input("Item ID not found. Please Enter correct ID  ")
    l=None
    for i in range(0,len(ids)):
        if iid == ids[i]:
            l=i
            break
    name=list(itmtab["Name"])[l]
    date=input("Enter date in the format DD/MM/YYYY  ")
    date=validate(date)
    ask=input("Item Disposed Off(Destroyed) or Sold?[Disposed(1)/Sold(2)]  ")
    a=""
    dquan=""
    squan=""
    tm=""
    svid=""
    if ask == "1":
        dquan = input("Enter Disposed Off Quantity without units(if any)  ")
        dquan = chkquan(l, dquan)
        if dquan == ";cancel":
            return
        squan = 0
        tm = 0
        svid = "-"
        a="Disposed Off"
    elif ask == "2":
        dquan = 0
        squan = input("Enter Sold Quantity without units(if any)  ")
        squan = chkquan(l, squan)
        if squan == ";cancel":
            return
        tm = float(input("Enter Total Money Recieved in Rs.(Do no enter any symbol like 'Rs.')  "))
        svid =input("Enter Vendor ID or ';new' to Add New Vendor ")
        svid=valiven(svid)
        a=f", Quantity {squan}, Sold to Vendor with ID {svid} and got Rs. {tm}"
    else:
        print("Invalid choice")
        return
    itmtab3.loc[itmtab3.shape[0]] = [ iid, name, dquan, squan, tm, svid, date]
    niq = float(list(itmtab2["Non-issued Quantity"])[l])
    niq -= (squan+dquan)
    cs = list(itmtab2["Current Status"])[l]
    if niq <= 0:
        niq=0
        cs="Extinguished"
    itmtab2.loc[l] = [ iid, name, niq, cs]
    itmtab2.to_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep=",", index=False)
    itmtab3.to_csv("C:/Users/HP/Downloads/chan project ip/item3.csv", sep=",", index=False)
    print(f"Item {name} with ID {iid} {a} on {date} successfully!")
def updstat():
    itmtab2 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep = ",")
    iid=input("Enter Item ID  ")
    ids=list(itmtab2["ID"])
    while iid not in ids :
        iid=input("Item ID not found. Please Enter correct ID  ")
    l=None
    for i in range(0,len(ids)):
        if iid == ids[i]:
            l=i
            break
    if list(itmtab2["Current Status"])[l] == "Extinguished":
        print(f"\nItem {iid} Extinguished, further changing of status denied.\n")
        return
    stat=input("Enter the new Status of the Item  ")
    name=list(itmtab2["Name"])[l]
    niq = list(itmtab2["Non-issued Quantity"])[l]
    itmtab2.loc[l] = [ iid, name, niq, stat]
    itmtab2.to_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep=",", index=False)
    print(f"Status of Item ID {iid} changed to {stat} successfully!")
def upddis():
    itmtab3 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item3.csv", sep = ",")
    itmtab2 =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep = ",")
    iid=input("Enter Item ID  ")
    ids=list(itmtab3["ID"])
    dates=list(itmtab3["Date"])
    while iid not in ids:
        iid=input("ID not found. Please enter valid ID  ")    
    date=input("Enter date in the format DD/MM/YYYY  ")
    date=validate(date)
    l=[]
    for i in range(0,len(ids)):
        if dates[i] == date:
            l.append(i)
    if len(l) < 1:
        print("Entry Not Found.")
        return
    elif len(l) > 1:
        print("These entries have been found, please select one by entering the index[number in the column prior to the ID column]\n")
        print(itmtab3[l])
        print("\n")
        ind=int(input("Enter Index  "))
        while ind not in l:
            ind=int(input("Please enter valid index"))
    else:
        ind=l[0]
    name=list(itmtab3["Name"])[ind]
    doq=list(itmtab3["Dispossed Off Quantity"])[ind]
    tm=list(itmtab3["Money Received"])[ind]
    stvi=list(itmtab3["Sold to Vendor ID"])[ind]
    nd=list(itmtab3["Date"])[ind]
    b=list(itmtab2["Non-issued Quantity"])[iid]
    ask = input("Do you want to update date?[Yes(y)/No(n)]?")
    if ask == "y":
        nd = input("Enter new date")
        nd=validate(nd)
    else:
        if stvi == "-":
            a=float(input("Enter new Disposed Off Quantity  "))
            while a < 0:
                a=float(input("Please enter a positive value  "))
            while (doq+b)<a:
                p=f"Please enter quantity less than or equal to {doq+b}  "
                a=float(input(p))
            doq=a
        else:
            ask=input("What do you want to update?[
                
        
#auto update quant and oher col. on update of items and dispose

cmd=0
while cmd != "0":
    cmdmenu1()

    cmd=input("Please Enter Command  ")

    if cmd == "1":
        itmcmd= 0
        while itmcmd != "0":
            print(f"\n\n{'Actions':<25}{'Commands':<8}")
            print("-"*33)
            print(f"{'Show Items':<25}{'1':<8}")
            print(f"{'Search Items':<25}{'2':<8}")
            print(f"{'Add Items':<25}{'3':<8}")
            print(f"{'Update Items':<25}{'4':<8}")
            print(f"{'Exit':<25}{'0':<8}\n")
            itmcmd = input("Please Enter Command  ").lower()

            if itmcmd == "1":
                ask=input("What you want to view?[Purchases(1)/Status(2)/Dispose Off History(3)]")
                itmtab=""
                if ask not in "123":
                    print("\nInvalid Choice\n")
                    pass
                elif ask == "1":
                    itmtab = pd.read_csv("C:/Users/HP/Downloads/chan project ip/item.csv", sep = ",")
                elif ask == "2":
                    itmtab = pd.read_csv("C:/Users/HP/Downloads/chan project ip/item2.csv", sep = ",")
                elif ask == "3":
                    itmtab = pd.read_csv("C:/Users/HP/Downloads/chan project ip/item3.csv", sep = ",")
                print("\n")
                print(itmtab)
            elif itmcmd == "3":
                cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
                print("\n")
                print(cattab)
                print("\n")
                ventab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/vendors.csv", sep = ",")
                print(ventab)
                print("\n")
                ask=input("What you want to add?[New Purchase(1)/Dispose Off Entry(2)]")
                if ask == "1":
                    newitm()
                    askitm=input("Want to add more[Yes(Y)/No(N)]?")
                    while askitm.lower() == "y":
                        newitm()
                        askitm=input("Want to add more[Yes(Y)/No(N)]?")
                elif ask == "2":
                    adddishis()
                    askitm=input("Want to add more[Yes(Y)/No(N)]?")
                    while askitm.lower() == "y":
                        adddishis()
                        askitm=input("Want to add more[Yes(Y)/No(N)]?")
            elif itmcmd == "4":
                ask=input("Which Table you want to Update>[Purchases(1)/Dispose Off or Sold(2)/Current Status(3)]")
                if ask == "1":
                    upditm()
                    askitm=input("Want to Update more[Yes(Y)/No(N)]?")
                    while askitm.lower() == "y":
                        upditm()
                        askitm=input("Want to Update more[Yes(Y)/No(N)]?")
                elif ask == "2":
                    upddis()
                    askitm=input("Want to Update more[Yes(Y)/No(N)]?")
                    while askitm.lower() == "y":
                        upddis()
                        askitm=input("Want to Update more[Yes(Y)/No(N)]?")
                elif ask == "3":
                    updstat()
                    askitm=input("Want to Update more[Yes(Y)/No(N)]?")
                    while askitm.lower() == "y":
                        updstat()
                        askitm=input("Want to Update more[Yes(Y)/No(N)]?")
                else:
                    print("Invalid Choice.")
            elif itmcmd == "0":
                print("\nExited Items menu.\n")
                    
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
                addtocat("")
                askcata=input("Want to add more[Yes(Y)/No(N)]?")
                while askcata.lower() == "y":
                    addtocat("")
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
                addtoven("")
                askvena=input("Want to add more[Yes(Y)/No(N)]?")
                while askvena.lower() == "y":
                    addtoven("")
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
    




