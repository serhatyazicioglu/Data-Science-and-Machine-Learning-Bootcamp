import pandas as pd
df = pd.read_csv("titanic.csv")

cat_cols = []
num_cols = []

def grab_col_names(dataframe):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    return cat_cols, num_cols


cat_cols, num_cols = grab_col_names(df)

"Object Variables : {}, Numeric Variables: {}".format(cat_cols, num_cols)
