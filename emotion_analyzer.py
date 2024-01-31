'''
Run this line in the command prompt b4 execution:

    python -m textblob.download_corpora

Doing so will ensure that the MissingCorpusError won't occur while running.

'''

from nrclex import NRCLex
import json
import csv
import sys

# need to increase max field size for csv files. some fields are very big!!!
# if you don't increase the field size limit, python won't be able to read transcripts.csv
maxInt = sys.maxsize

# while loop will decrease maxInt until no OverflowError occurs; we can avoid getting the error when trying to set csv field size to the largest possible int
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
    text = ""
    with open(csv_file, 'r') as file:
        data = csv.reader(file)
        count = 0
        for line in data:
            text += str(line) + ' '
            count += 1
            print(count, end='\r')
    return NRCLex(text)

# articles_object = csv_analyzer('data/articles.csv')

# # affect frequencies
# frequencies = open('outputs/articles_AFFECT_FREQUENCIES.txt', 'w')
# frequencies.write(str(articles_object.affect_frequencies))
# frequencies.close()

# # raw emotion scores
# raw_scores = open('outputs/articles_RAW_SCORES.txt', 'w')
# raw_scores.write(str(articles_object.raw_emotion_scores))
# raw_scores.close()

# # top emotions
# top_scores = open('outputs/articles_TOP_EMOTIONS.txt', 'w')
# top_scores.write(str(articles_object.top_emotions))
# top_scores.close()

transcripts_object = csv_analyzer('data/transcripts.csv')

# affect frequencies
frequencies = open('outputs/transcripts_AFFECT_FREQUENCIES.txt', 'w')
frequencies.write(str(transcripts_object.affect_frequencies))
frequencies.close()

# raw emotion scores
raw_scores = open('outputs/transcripts_RAW_SCORES.txt', 'w')
raw_scores.write(str(transcripts_object.raw_emotion_scores))
raw_scores.close()

# top emotions
top_scores = open('outputs/transcripts_TOP_EMOTIONS.txt', 'w')
top_scores.write(str(transcripts_object.top_emotions))
top_scores.close()