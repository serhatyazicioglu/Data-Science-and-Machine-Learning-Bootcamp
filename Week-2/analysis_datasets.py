import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv("train.csv")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


def summary(dataframe, cat_th=10, car_th=20):
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() <= cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    final_cat_cols = cat_cols + num_but_cat
    final_cat_cols = [col for col in final_cat_cols if col not in cat_but_car]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"Categorical Variables: {len(cat_cols)}, {cat_cols}")
    print(f"Numerical Numbers: {len(num_cols)} : {num_cols}")
    print(f"Numerical Variables: {len(num_cols)}, Num but Cat Variables: {len(num_but_cat)}")
    print(f"Categorical Variables: {len(cat_cols)}, Cat but Car Variables: {len(cat_but_car)}")
    print(f"Categorical Variables:{len(final_cat_cols), final_cat_cols}")

    return cat_cols, num_cols, num_but_cat, cat_but_car, final_cat_cols


cat_cols, num_cols, num_but_cat, cat_but_car, final_cat_cols = summary(df)
final_num_cols = [col for col in num_cols if col not in num_but_cat]


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}), end="\n\n\n")


for col in final_cat_cols:
    cat_summary(df, col)

final_num_cols = [col for col in num_cols if col not in num_but_cat]
df[final_num_cols].describe([0.05, 0.10, 0.25, 0.50, 0.75, 0.80, 0.90, 0.95, 0.99]).T


def num_hist(dataframe, numeric_col):
    col_counter = 0
    for col in numeric_col:
        dataframe[col].hist(bins=20)
        plt.xlabel(col)
        plt.title(col)
        plt.show()
        col_counter += 1
    print(f"{col_counter} variables have been plotted")
num_hist(df, final_num_cols)


def target_summary_with_cat(dataframe, categorical_col, target):
    for col in categorical_col:
        if col not in target:
            print(pd.DataFrame({"target_mean": dataframe.groupby(col)[target].mean()}), end="\n\n\n")


target_summary_with_cat(df, final_cat_cols, target)


def target_summary_with_num(dataframe, target, numerical_col):
    print(dataframe.groupby(target).agg({numerical_col: "mean"}), end="\n\n\n")

