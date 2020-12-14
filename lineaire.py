import pandas as pd
from sklearn.linear_model import LinearRegression

depenses = pd.read_csv("depenses_anonymes.csv")
prediction = depenses[["salaire", "depenses"]]

regression1 = LinearRegression()
regression1.fit(prediction["salaire"], prediction["depenses"])
prediction["prediction_depenses"] = regression1.predict(prediction["salaire"])

depenses.to_csv("predictions_1.csv.csv",index=False)

prediction = depenses[["salaire", "age", "depenses"]]

regression1 = LinearRegression()
regression1.fit(prediction[["salaire", "age"]], prediction["depenses"])
prediction["prediction2_depense"] = regression1.predict(prediction[["salaire", "age"]])

depenses.to_csv("predictions_2.csv.csv",index=False)