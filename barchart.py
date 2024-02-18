import matplotlib.pyplot as plt
import numpy as np
import sys

emotions = ['positive', 'negative', 'anticipation', 'joy', 'fear', 'trust', 'sadness', 'disgust', 'surprise', 'anger']
x = np.arange(len(emotions))

# Initial aggregate comparison chart (three corpora)
def three_corpora_chart():
    width = 0.25
    multiplier = 0

    # articles corpus
    article_bars = x
    article_file = open('outputs/aggregated data/articles.AGGREGATE.txt', 'r')
    article_content = article_file.readlines()
    article_dict = eval(article_content[3])
    article_frequencies = []
    article_file.close()

    # quotes corpus
    quote_bars = [i+width for i in article_bars]
    quote_file = open('outputs/aggregated data/quotes.AGGREGATE.txt', 'r')
    quote_content = quote_file.readlines()
    quote_dict = eval(quote_content[3])
    quote_frequencies = []
    quote_file.close()
    
    # transcripts corpus
    transcript_bars = [i+width for i in quote_bars]
    transcript_file = open('outputs/aggregated data/transcripts.AGGREGATE.txt', 'r')
    transcript_content = transcript_file.readlines()
    transcript_dict = eval(transcript_content[3])
    transcript_frequencies = []
    transcript_file.close()
    
    # Collect values for emotion frequencies, in order of emotions list, for each corpus
    for emotion in emotions:
        article_frequencies.append(article_dict[emotion])
        quote_frequencies.append(quote_dict[emotion])
        transcript_frequencies.append(transcript_dict[emotion])


    plt.figure(figsize=(10,5))
    # Configure bars for each corpus
    plt.bar(article_bars, article_frequencies, width=width, label='Articles')
    plt.bar(quote_bars, quote_frequencies, width=width, label='Quotes')
    plt.bar(transcript_bars, transcript_frequencies, width=width, label='Transcripts')
    
    # Chart labels
    plt.ylabel('Emotion frequency')
    plt.title('Emotion frequencies by corpus')
    plt.xticks(x+width+(width/2), emotions)
    plt.legend(loc='upper left')
    plt.ylim(0, 1)


    plt.savefig('outputs/charts/three_corpus_comparison.png')


three_corpora_chart()