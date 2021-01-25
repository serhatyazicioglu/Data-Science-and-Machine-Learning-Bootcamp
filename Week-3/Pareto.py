import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

df_ = pd.read_excel("online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()
df[~df["Invoice"].str.contains("C", na=False)]
df = df[df["Quantity"] > 0]
df.dropna(inplace=True)
df["TotalPrice"] = df["Quantity"] * df["Price"]


def pareto_principle(groupby_col_name, col_name):
    """
    :param groupby_col_name: yapılmak istenen kırılımın column name'i
    :param col_name: pareto hesabının incelenmesi istenilen column name'i
    :return: girilen col_name'in %80'ini ve daha fazlasını oluşturan değerlerin sayısı ve bunların tüm değerlere oranı.
    """

    counter = 0
    total = 0

    dataframe = df.groupby(groupby_col_name).agg({col_name: lambda x: x.sum()}).sort_values(col_name,
                                                                                            ascending=False)
    dataframe.reset_index(inplace=True)

    for i in dataframe[col_name]:
        total = total + i
        counter = counter + 1
        if (total / dataframe[col_name].sum()) >= 0.8:
            break
    ratio = (counter / df[groupby_col_name].nunique()) * 100

    if groupby_col_name == "StockCode":
        print(f"{col_name} değerinin %80'i veya daha fazlasını ilk {counter} ürün oluşturmuştur."
              f" Bunlar tüm ürünlerin ½ {ratio} 'sidir.")
    elif groupby_col_name == "Customer ID":
        print(f"{col_name} değerinin %80'i veya daha fazlasını ilk {counter} müşteri oluşturmuştur."
              f" Bunlar tüm müşterilerin ½ {ratio} 'sidir.")


pareto_principle("Customer ID", "TotalPrice")
pareto_principle("StockCode", "TotalPrice")
