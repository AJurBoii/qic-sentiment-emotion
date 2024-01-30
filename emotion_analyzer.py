'''
Run this line in the command prompt b4 execution:

    python -m textblob.download_corpora

Doing so will ensure that the MissingCorpusError won't occur while running.

'''

from nrclex import NRCLex
import json

def analyzer(file):
    data = json.load(file)
    total = len(data)
    current = 1
    text = ""
    for article in data:
        text += str(article['content'])
        print("\r" + str(current) + "/" + str(total), end='\r')
        current += 1
    return NRCLex(text)

# Must input an NRCLex object, which you can get from running analyzer function above
def affect_count(nrclex_object):
    affect_dictionary = nrclex_object.affect_dict
    counts = {}
    for keys in affect_dictionary.keys:
        for emotion in affect_dictionary[keys]:
            # will do something
            pass