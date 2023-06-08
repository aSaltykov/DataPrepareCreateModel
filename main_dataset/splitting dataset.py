import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('multinli_1.0_train_preprocessed.csv')

data = data.sample(frac=1, random_state=42).reset_index(drop=True)

train_data, remaining = train_test_split(data, train_size=120000, random_state=42)
valid_data, test_data = train_test_split(remaining, train_size=18000, test_size=18000, random_state=42)

train_data.to_csv('train_data.csv', index=False)
valid_data.to_csv('valid_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)
