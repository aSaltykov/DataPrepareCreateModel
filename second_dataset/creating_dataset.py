import pandas as pd

df = pd.read_csv('paraphrased_articles.csv')

df1 = pd.DataFrame()
df2 = pd.DataFrame()

df1['Text1'] = df['Abstract']
df1['Text2'] = df['ParaphrasedAbstract']
df1['Similarity'] = [1] * len(df)

df2['Text1'] = df['Abstract']
df2['Text2'] = df['Abstract'].sample(frac=1).reset_index(drop=True)
df2['Similarity'] = [0] * len(df)

new_df = pd.concat([df1, df2])

new_df = new_df[new_df['Text1'] != new_df['Text2']]

new_df = new_df.reset_index(drop=True)

new_df.to_csv('new_dataset.csv', index=False)
