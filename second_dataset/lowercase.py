import pandas as pd

df = pd.read_csv('similarity_dataset.csv')

df['Text1'] = df['Text1'].str.lower()
df['Text2'] = df['Text2'].str.lower()

df.to_csv('similarity_dataset.csv', index=False)
