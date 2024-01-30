'''
Run this line in the command prompt b4 execution:

    python -m textblob.download_corpora

Doing so will ensure that the MissingCorpusError won't occur while running.

'''

from nrclex import NRCLex
import json

file = open('all_articles1.json')
data = json.load(file)

total = len(data)
current = 1

all_articles_text = ""
for article in data:
    all_articles_text += str(article['content'])
    print("\r" + str(current) + "/" + str(total), end='\r')
    current += 1

text_object = NRCLex(all_articles_text)

print("Printing affect dict to output...")

print(text_object.affect_dict)
file.close()

# file = open('sample.txt', 'r')
# text = file.read()
# text_object = NRCLex(text)

# print(text_object.affect_dict)
# file.close()