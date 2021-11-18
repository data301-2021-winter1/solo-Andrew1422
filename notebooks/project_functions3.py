import pandas as pd
import numpy as np

def removeColumnsByIndex(table, columns):
    return table.drop(columns = table.columns[columns])



def assign_index_to_month(table):
    index=[]
    table1=table.copy()
    for i in table1["Month"]:
        if i=="January":
            index.append(1)
        elif i=="February":
            index.append(2)
        elif i=="March":
            index.append(3)
        elif i=="April":
            index.append(4)
        elif i=="May":
            index.append(5)
        elif i=="June":
            index.append(6)
        elif i=="July":
            index.append(7)
        elif i=="August":
            index.append(8)
        elif i=="September":
            index.append(9)
        elif i=="October":
            index.append(10)
        elif i=="November":
            index.append(11)
        elif i=="December":
            index.append(12)
        else:
            index.append(0)
    table1["Month_index"]=index
    return table1



    def info(df):
    df1=(
        print(f"Number of rows and columns: {df.shape}")
    )
    df2=(
        display(df.head)
    )
    df3=(
        sns.set(style = "darkgrid")
    )
    df4=(
        plt.figure(figsize=(19,10))
    )
    df5=(
        sns.lineplot(x="Month", y="Area (hectares)", hue="Jurisdiction", data = area_burned_by_month)
    )
    df6=(
        plt.show()
    )