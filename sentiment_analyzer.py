'''
Run this line in the command prompt b4 execution:

    python -m textblob.download_corpora

Doing so will ensure that the MissingCorpusError won't occur while running.

'''

from nrclex import NRCLex
import json

# file = open('all_articles1.json')
# data = json.load(file)

# text_object = NRCLex(data[0]['content'])
# print(text_object.affect_dict)
# file.close()

file = open('sample.txt', 'r')
text = file.read()
text_object = NRCLex(text)

print(text_object.affect_dict)
file.close()