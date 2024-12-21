import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("country_vaccinations.csv")
df.head(10)

df.isnull().sum()
missing_value=["N/a","na",np.nan]
df=pd.read_csv("country_vaccinations.csv",na_values=False)
df.isnull().sum()
df.isnull().any()

# Visualize missing values using a heatmap (optimize by using a subset of data)
subset = df.iloc[:5200, :]  # Taking the first 100 rows for better performance
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()
df.head(10)
df.dropna()
df.dropna(how="all")
df.fillna(0)
df.fillna(method="bfill")
df.interpolate()
df_dropped=df.dropna()
df_dropped