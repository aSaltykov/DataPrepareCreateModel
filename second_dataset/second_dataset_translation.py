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
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'a', encoding='utf-8', newline='') as outfile:
        writer = csv.writer(outfile)
        for i, row in enumerate(csv.reader(infile)):
            if i < start_line:
                continue
            if line_count >= max_lines:
                break
            text1 = row[0]
            text2 = row[1]
            similarity = row[2]
            writer.writerow([text1, text2, similarity])
            writer.writerow([text1, translate_to_ukrainian(text2), similarity])
            writer.writerow([translate_to_ukrainian(text1), text2, similarity])
            writer.writerow([translate_to_ukrainian(text1), translate_to_ukrainian(text2), similarity])
            line_count += 4

translate_dataset('new_dataset.csv', 1000)
