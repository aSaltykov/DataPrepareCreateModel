import pandas as pd

similarity_df = pd.read_csv('translated_new_dataset.csv')

identical_texts_df = similarity_df[['Text1']].drop_duplicates()
identical_texts_df['Text2'] = identical_texts_df['Text1']
identical_texts_df['Similarity'] = 1

similarity_df_updated = pd.concat([similarity_df, identical_texts_df])

similarity_updated = similarity_df_updated[
    ~similarity_df_updated['Text1'].isin(['Text1', 'Текст1', 'Text2', 'Текст2'])]
similarity_df_updated = similarity_df_updated[
    ~similarity_df_updated['Text2'].isin(['Text1', 'Текст1', 'Text2', 'Текст2'])]

similarity_df_updated.to_csv('similarity_dataset.csv', index=False)
