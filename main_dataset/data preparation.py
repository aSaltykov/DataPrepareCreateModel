import pandas as pd
import string


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def clean_text(text):
    text = text.replace(u'\xa0', u' ')
    return ''.join(char for char in text if char.isprintable())


def process_file(file_name):
    df = pd.read_csv(file_name, sep="\t", on_bad_lines='skip')

    required_columns = df[["gold_label", "sentence1", "sentence2"]].copy()

    required_columns.dropna(subset=['sentence1', 'sentence2'], inplace=True)

    required_columns.loc[:, "sentence1"] = required_columns["sentence1"].str.lower()
    required_columns.loc[:, "sentence2"] = required_columns["sentence2"].str.lower()

    required_columns.loc[:, "sentence1"] = required_columns["sentence1"].apply(remove_punctuation)
    required_columns.loc[:, "sentence2"] = required_columns["sentence2"].apply(remove_punctuation)

    required_columns.loc[:, "sentence1"] = required_columns["sentence1"].apply(clean_text)
    required_columns.loc[:, "sentence2"] = required_columns["sentence2"].apply(clean_text)

    output_file_name = file_name.replace(".txt", "_preprocessed.csv")
    required_columns.to_csv(output_file_name, index=False)


process_file("multinli_1.0_train.txt")
