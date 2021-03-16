import numpy as np
import pandas as pd

df = pd.read_csv("datasets/Advertising.csv")

# b = 2.90, w1 = 0.04, w2 = 0.17, w3= 0.002
# b = 1.70, w1 = 0.09, w2 = 0.20, w3= 0.017

# 1- Model denklemi nedir?
# y = 2.90 + 0.04 * TV + 0.17 * RADIO + 0.002 * NEWSPAPER
# y = 1.70 + 0.09 * TV + 0.20 * RADIO + 0.017 * NEWSPAPER

df["first_sales_pred"] = 2.90 + 0.04 * df["TV"] + 0.17 * df["radio"] + 0.002 * df["newspaper"]

df["second_sales_pred"] = 1.70 + 0.09 * df["TV"] + 0.20 * df["radio"] + 0.017 * df["newspaper"]

# MSE
np.mean((df["sales"] - df["first_sales_pred"]) ** 2)
np.mean((df["sales"] - df["second_sales_pred"]) ** 2)

# RMSE
np.sqrt(np.mean((df["sales"] - df["first_sales_pred"]) ** 2))
np.sqrt(np.mean((df["sales"] - df["second_sales_pred"]) ** 2))

# MAE
np.mean(np.abs(df["sales"] - df["first_sales_pred"]))
np.mean(np.abs(df["sales"] - df["second_sales_pred"]))

# first_sales_pred olarak tanımladığımız model denkleminin verdiği sonuçlar diğer model denklemine
# kıyasla daha doğru sonuçlar verdiğinden bu model tercih edilebilir.


