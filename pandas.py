import pandas as pd
users = pd.read_csv('users.csv')
purchases = pd.read_csv('purchases.csv')

df = purchases.merge(users, how="inner", on="uid")

df["uid"].nunique()

df["price"].nunique()

df["price"].value_counts()

df["country"].value_counts()

df.groupby("country").agg({"price": ["sum"]}).head()

df["device"].value_counts()

df.groupby(["country"]).agg({"price": ["mean"]})

df.groupby(["device"]).agg({"price": ["mean"]})

df.groupby(["country", "device"]).agg({"price": "sum"})
