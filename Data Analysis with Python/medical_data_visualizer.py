import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")
# 2
df['overweight'] = (df["weight"] / (df["height"]/100)**2).apply(lambda x:1 if x > 25 else 0)

# 3 Normalize data for glucose and cholesterol
df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars = "cardio", value_vars = ["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
                     var_name = "feature", value_name = "value" )
    # 6
    df_cat = df_cat.groupby(["cardio", "feature", "value"]).size().reset_index(name = "count")
  

    # 7
    figure = sns.catplot(
        data = df_cat,
        x = "feature",
        y = "count",
        hue = "value",
        col = "cardio",
        kind = "bar"
    ).set_axis_labels("variable", "total")

    # 8
    fig = figure.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df["ap_lo"] <= df["ap_hi"]) & 
                     (df["height"] >= df["height"].quantile(0.025)) &
                     (df["height"] <= df["height"].quantile(0.975)) &
                     (df["weight"] >= df["weight"].quantile(0.025)) & 
                     (df["weight"] <= df["weight"].quantile(0.975))]

    # 12
    corr = df_heat.corr()
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask=mask, fmt='.1f', annot=True)

    # 16
    fig.savefig('heatmap.png')
    return fig
