import pandas as pd
import sklearn.preprocessing as prep

# Recuperation des données
depenses = pd.read_csv("depenses.csv")

# Modification de la colonne ville
uniqueVilles = depenses["ville"].unique()
for i in range(len(uniqueVilles)):
    depenses["ville"] = depenses["ville"].replace(uniqueVilles[i], "ville" + str(i))

# Modification de la colonne nom
for i in range(len(depenses["nom"])):
    depenses.at[i, "nom"] = "id" + str(i)

# Normalisation des 3 autres colonnes
depenses["age"] = prep.scale(depenses["age"])
depenses["salaire"] = prep.scale(depenses["salaire"])
depenses["depenses"] = prep.scale(depenses["depenses"])

# Ecriture dans un nouveau fichier csv
depenses.to_csv("depenses_anonymes.csv",index=False)