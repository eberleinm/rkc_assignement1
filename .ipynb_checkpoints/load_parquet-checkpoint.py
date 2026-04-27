import pandas as pd
df = pd.read_parquet('train-product-review.parquet')
dfcsv = df.to_csv('train-product-review.csv', index=False)
print(df.head())