from sklearn.ensemble import RandomForestRegressor
import pandas as pd

data = {
    "rainfall":[10,50,70,20,30],
    "temperature":[32,35,38,40,42],
    "aqi":[100,200,300,250,350],
    "risk":[0.2,0.6,0.8,0.4,0.9]
}

df=pd.DataFrame(data)

X=df[["rainfall","temperature","aqi"]]
y=df["risk"]

model=RandomForestRegressor()
model.fit(X,y)

print("Risk model trained")
