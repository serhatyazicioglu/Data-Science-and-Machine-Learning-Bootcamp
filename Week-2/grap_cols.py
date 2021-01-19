import pandas as pd

df = pd.read_csv("titanic.csv")


def grap_cols(dataframe, cat_th=10, car_th=20, target="", id=False, date=False):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() <= cat_th and
                   dataframe[col].dtypes != "O"]

    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]

    final_cat_cols = cat_cols + num_but_cat
    final_cat_cols = [col for col in final_cat_cols if col not in cat_but_car]

    target = [col for col in dataframe.columns if target in col]

    id = [col for col in dataframe.columns if "Id" in col]

    date = [col for col in dataframe.columns if dataframe[col].dtypes == "datetime64"]

    shape_control = len(num_cols) + len(final_cat_cols) - len(id)

    if df.shape[1] == shape_control:
        return cat_cols, num_cols, num_but_cat, cat_but_car, final_cat_cols, target, id, date
    else:
        print("Lost columns!")


cat_cols, num_cols, num_but_cat, cat_but_car, final_cat_cols, target, id, date = grap_cols(df, target="Survived", id="PassengerId")



