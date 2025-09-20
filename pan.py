import pandas as pd 
import numpy as np 
df=pd.read_csv('dev.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.columns)
scores=df['Ladder score'].to_numpy()
print("\nNumPy Statistics on Ladder Score:")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Min:", np.min(scores))
print("Max:", np.max(scores))
if 'Log GDP per capita' in df.columns:
    gdp = df['Log GDP per capita'].dropna().to_numpy()
    gdp_norm = (gdp - gdp.min()) / (gdp.max() - gdp.min())
    df.loc[df['Log GDP per capita'].notna(), 'GDP Normalized'] = gdp_norm
print("\n🔹 Data with Normalized GDP:")
print(df[['Country name', 'Log GDP per capita', 'GDP Normalized']].head())
