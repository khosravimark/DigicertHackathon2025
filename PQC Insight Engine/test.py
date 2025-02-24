import pandas as pd

df = pd.read_csv("pqc_training_data.csv")
print(df["OS Type"].unique())  # Check all unique OS types

