import pandas as pd

users = pd.read_csv("users.csv")
purchases = pd.read_csv("purchases.csv")
df = purchases.merge(users, how="inner", on="uid")

# country, device, gender, age kırılımında toplam kazançlar nedir?
agg_df = df.groupby(["country", "device", "gender", "age"]).agg({"price": "sum"})

agg_df = agg_df.sort_values("price", ascending=False)

agg_df.reset_index(inplace=True)

bins = [0, 19, 24, 31, 41, agg_df["age"].max()]
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["age"].max())]
agg_df["age_cat"] = pd.cut(agg_df["age"], bins, labels=mylabels)

agg_df["customers_level_based"] = [row[0] + "_" + row[1].upper() + "_" + row[2] + "_" +
                                   str(row[5]) for row in agg_df.values]


agg_df["customers_level_based"].count()
agg_df = agg_df.groupby("customers_level_based").agg({"price": "mean"})
agg_df = agg_df.reset_index()
agg_df["customers_level_based"].count()

agg_df["segment"] = pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])

agg_df.groupby(["segment"]).agg({"price": "sum"})

# What segment is a 42 year old Turkish woman using IOS in?
new_user = "TUR_IOS_F_41_75"
new_customers = agg_df[agg_df["customers_level_based"] == new_user]
new_customers
