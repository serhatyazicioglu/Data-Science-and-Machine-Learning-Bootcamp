import pandas as pd
df = pd.read_csv("titanic.csv")

def summary(dataframe):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() <= 20 and dataframe[col].dtypes != "O"]
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > 20 and dataframe[col].dtypes == "O"]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"Categorical Variables: {len(cat_cols)}, {cat_cols}")
    print(f"Numerical Numbers: {len(num_cols)} : {num_cols}")
    print(f"Numerical Variables: {len(num_cols)}, Num but Cat Variables: {len(num_but_cat)}")
    print(f"Categorical Variables: {len(cat_cols)}, Cat but Car Variables: {len(cat_but_car)}")



