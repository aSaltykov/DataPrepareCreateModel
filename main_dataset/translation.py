import csv
import os

from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS']


def translate_to_ukrainian(text):
    client = translate.Client()
    translation = client.translate(text, target_language='uk')
    return translation['translatedText']


def translate_dataset(input_file, max_lines, start_line=0):
    output_file = "translated_" + input_file
    line_count = 0
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'a', encoding='utf-8',
                                                                 newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for i, row in enumerate(reader):
            if i < start_line:
                continue
            if line_count >= max_lines:
                break
            gold_label, sentence1, sentence2 = row
            sentence1_ukr = translate_to_ukrainian(sentence1)
            sentence2_ukr = translate_to_ukrainian(sentence2)
            writer.writerow([gold_label, sentence1, sentence2])
            writer.writerow([gold_label, sentence1, sentence2_ukr])
            writer.writerow([gold_label, sentence1_ukr, sentence2])
            writer.writerow([gold_label, sentence1_ukr, sentence2_ukr])
            line_count += 4


translate_dataset('train_data.csv', 120000)
translate_dataset('test_data.csv', 19000)
translate_dataset('valid_data.csv', 19000)


