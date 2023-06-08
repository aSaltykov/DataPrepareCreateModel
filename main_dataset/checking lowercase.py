import pandas as pd


def check_and_lower(df, column):
    if not df[column].str.islower().all():
        df[column] = df[column].str.lower()
        return True
    return False


def ensure_lowercase(file_name):
    df = pd.read_csv(file_name)

    columns_to_check = ["gold_label", "sentence1", "sentence2"]
    changes_made = any(check_and_lower(df, col) for col in columns_to_check)

    if changes_made:
        df.to_csv(file_name, index=False)
        print(f"Changes made to {file_name}")
    else:
        print(f"No changes necessary for {file_name}")


ensure_lowercase('translated_train_data.csv')
ensure_lowercase('translated_test_data.csv')
ensure_lowercase('translated_valid_data.csv')
