# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/Average-price-seasonally-adjusted-2022-08.csv")
print(df)

# Checking For NAN
print(df.isnull().sum())

# Checking unique values
print(df["Region_Name"].unique())

# Converting to numeric
print(df.shape)
df["Average_Price_SA"]=pd.to_numeric(df["Average_Price_SA"],errors="raise" )
print(df.shape)

# Converting to datetime
df["Date"]=pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["Year"]=df["Date"].dt.year

# Filtering Years
yrs=df[(df["Year"]>=2003) & (df["Year"]<=2021)]

# Choosing top 10 largest regions
top_10_regions=(
    yrs.groupby("Region_Name")["Average_Price_SA"]
        .mean()
            .nlargest(10)
                .index
                )
                df_top = yrs[yrs["Region_Name"].isin(top_10_regions)]
                print(df_top)

                # Creating a pivot
                df_pivot=df_top.pivot_table(
                    index="Year",
                        columns="Region_Name",
                            values="Average_Price_SA",
                                aggfunc="mean"
                                )
                                sns.set_palette("deep")

                                plt.figure(figsize=(12,8))

                                # Final stage: creating the heatmap
                                sns.heatmap(
                                    df_pivot,
                                        annot=True,
                                            fmt=".0f",
                                                cmap="coolwarm",
                                                    cbar_kws={"label": "Average Price (£)"},
                                                        linewidths=0.5
                                                        )
                                                        plt.title("🇬🇧 Heatmap: UK 10 largest regions Sales (2003-2021).")
                                                        plt.ylabel("Sales")
                                                        plt.xlabel("Region")
                                                        plt.xticks(rotation=45)
                                                        plt.yticks(rotation=0)
                                                        plt.tight_layout()
                                                        plt.show()
