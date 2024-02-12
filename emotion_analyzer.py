'''
Run this line in the command prompt b4 execution:

    python -m textblob.download_corpora

Doing so will ensure that the MissingCorpusError won't occur while running.

'''

from nrclex import NRCLex
import json
import os
import csv
import sys

# Prevents csv.Error: field larger than field limit.
maxInt = sys.maxsize
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

# input: string, name of json corpus file
def json_analyzer(json_file):
    text = ""
    with open(json_file, 'r') as file:
        data = json.load(file)
        total = len(data)
        current = 1
        for article in data:
            text += str(article['content'] + ' ')
            print(str(current) + "/" + str(total), end='\r')
            current += 1
    return NRCLex(text)

# csv input
def csv_analyzer(csv_file):
    file_name = os.path.basename(csv_file)
    file_name = os.path.splitext(file_name)[0]

    with open(csv_file) as file:
        reader = csv.reader(file)
        aff_freq = open(f'outputs/{file_name}_AFFECT_FREQUENCIES.txt', 'a')
        raw_scores = open(f'outputs/{file_name}_RAW_SCORES.txt', 'a')
        top_emote = open(f'outputs/{file_name}_TOP_EMOTIONS.txt', 'a')

        for row in reader:
            text_object = NRCLex(str(row[0]))

            aff_freq.write(str(text_object.affect_frequencies) + '\n')
            raw_scores.write(str(text_object.raw_emotion_scores) + '\n')
            top_emote.write(str(text_object.top_emotions) + '\n')

        aff_freq.close()
        raw_scores.close()
        top_emote.close()


# csv_analyzer('data/articles.csv')
# csv_analyzer('data/quotes_by_article.csv')
csv_analyzer('data/transcripts.csv')