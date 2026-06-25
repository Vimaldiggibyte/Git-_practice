import pandas as pd


df = pd.read_csv(r"C:\practice_git\data\clean_sales.csv")

print(df.describe())

print(' Columns : ',df.columns)
print(' Rows : ',df.shape)
print("Print only the column one ", df.columns[0])
print("Print only the column two ", df.columns[1])
print("Print only the column three ", df.columns[2])


