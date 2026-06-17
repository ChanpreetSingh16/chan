elif catcmd == ";delcat":
                delfromcat()
                askcatd=input("Want to delete more[Yes(Y)/No(N)]?")
                while askcatd.lower() == "y":
                    delfromcat()
                    askcatd=input("Want to delete more[Yes(Y)/No(N)]?")
            elif catcmd == ";delalcat":
                cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
                confirm = input("Are you sure you want to delete all categories, you won't be able to undo the process![Yes(y)/No(n)]").lower()
                if confirm == "y":
                    for i in range(0, cattab.shape[0]):
                        cattab=cattab.drop(i)
                    cattab.to_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep=",", index=False)
                    print("\nAll Clear.")


def delfromcat():
    cattab =  pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
    codes=cattab["Code"]
    cats=cattab["Category"]
    how=input("You want to delete by 'Code' or 'Category'?[Code(code)/Category(cat)]").lower()
    e="Please enter the " + how
    q=input(e)
    confirm=input("Are you sure you want to delete the category? You won't be able to undo this actions.[Yes(y)/No(n)]").lower()
    if confirm == "y":
        if how == "code":
            g=codes
        elif how == "cat":
            g=cats
        else:
            print("Your choice of deletion was invalid.")
            return
        k=[]
        for i in range(0, cattab.shape[0]):
            if q == g[i]:
                k.append(i)
        cattab=cattab.drop(k)
        cattab.to_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep=",", index=False)
        print("\nEntery Deleted successfully!")
            
