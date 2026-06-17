import pandas as pd
df = pd.DataFrame({"Code":["c01"], "Categorie":["Computer"]})
df.to_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep=",", index=False)
ndf = pd.read_csv("C:/Users/HP/Downloads/chan project ip/categ.csv", sep = ",")
#print(ndf.shape[0])
#print(ndf)
#print(ndf.iloc[0])
#ndf.loc[ndf.shape[0]+1] = [ ndf.shape[0], "c02", "furniture"]
#ndf.loc[ndf.shape[0]+1] = [ ndf.shape[0], "c03", "f"]
#print(ndf)

