import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
import os

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
    plt.ylim(0, 0.5)


    plt.savefig('outputs/charts/three_corpus_comparison.png')

# Chart that includes control group
def four_corpora_chart():
    width = 0.20
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

    # control corpus
    control_bars = [i+width for i in transcript_bars]
    control_file = open('outputs/aggregated data/control.AGGREGATE.txt', 'r')
    control_content = control_file.readlines()
    control_dict = eval(control_content[3])
    control_frequencies = []
    control_file.close()
    
    # Collect values for emotion frequencies, in order of emotions list, for each corpus
    for emotion in emotions:
        article_frequencies.append(article_dict[emotion])
        quote_frequencies.append(quote_dict[emotion])
        transcript_frequencies.append(transcript_dict[emotion])
        control_frequencies.append(control_dict[emotion])


    plt.figure(figsize=(10,5))
    # Configure bars for each corpus
    plt.bar(article_bars, article_frequencies, width=width, label='Articles')
    plt.bar(quote_bars, quote_frequencies, width=width, label='Quotes')
    plt.bar(transcript_bars, transcript_frequencies, width=width, label='Transcripts')
    plt.bar(control_bars, control_frequencies, width=width, label="Control")
    
    # Chart labels
    plt.ylabel('Emotion distribution')
    plt.title('Emotion distribution by corpus')
    plt.xticks(x+width+(width/2), emotions)
    plt.legend(loc='upper left')
    plt.ylim(0, 0.5)


    plt.savefig('outputs/charts/four_corpus_comparison.png')

# Takes the differences in emotion distributions between two corpora as an average
def average_difference(source_one, source_two):
    file_one = open(f'outputs/aggregated data/{source_one}', 'r')
    temp = file_one.readlines()
    corpus_one = eval(temp[3])
    
    file_two = open(f'outputs/aggregated data/{source_two}', 'r')
    temp2 = file_two.readlines()
    corpus_two = eval(temp2[3])

    file_one.close()
    file_two.close()

    total = 0

    for emotion in emotions:
        diff = abs(corpus_one[emotion] - corpus_two[emotion])
        total += diff
    
    average = total / len(emotions)
    return average

def chart_matches(article_freq, transcript_freq):
    width = 0.3
    multiplier = 0

    article_bars = x

    transcript_bars = [i + width for i in article_bars]
    
    a_freq = []
    t_freq = []
    for emotion in emotions:
        a_freq.append(float(article_freq[emotion]))
        t_freq.append(float(transcript_freq[emotion]))

    plt.figure(figsize=(10,5))
    plt.bar(article_bars, a_freq, width=width, label='Article')
    plt.bar(transcript_bars, t_freq, width=width, label='Transcript')

    # Chart labels
    plt.ylabel('Emotion distribution')
    plt.title('Emotion distribution between matched article and transcript')
    plt.xticks(x+(width/2), emotions)
    plt.legend(loc='upper left')
    plt.ylim(0, 0.5)

    plt.savefig('outputs/matched articles transcripts/example_comparison.png')

def emotion_scatter_plot(filename, emotion):
    # Collect polarities of each match
    article_vectors = []
    transcript_vectors = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            temp = eval(row['article_frequency'])
            article_emotion = temp[emotion]
            article_vectors.append(article_emotion)

            temp = eval(row['transcript_frequency'])
            transcript_emotion = temp[emotion]
            transcript_vectors.append(transcript_emotion)
    x = np.array(article_vectors)
    y = np.array(transcript_vectors)

    slope, intercept = np.polyfit(x, y, 1)

    line_of_best_fit = slope * x + intercept
    # plot!!
    fig, ax = plt.subplots()
    ax.scatter(article_vectors, transcript_vectors)
    plt.plot(x, line_of_best_fit, color='red', label='Line of Best Fit')

    # labels
    plt.ylabel(f'\"{emotion}\" in transcript')
    plt.xlim(0, 0.40)
    plt.ylim(0, 0.40)
    plt.xlabel(f'\"{emotion}\" in article')
    plt.title(f'{emotion} vector between article/transcript matches')

    plt.savefig(f'outputs/matched articles transcripts/scatter plots/{emotion}.png')

# three_corpora_chart()

emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'positive')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'negative')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'anticipation')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'joy')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'fear')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'trust')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'sadness')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'disgust')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'surprise')
emotion_scatter_plot('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'anger')






if not os.path.isfile('outputs/aggregated data/distribution_differences.txt'):
    with open('outputs/aggregated data/distribution_differences.txt', 'w') as file:
        file.write('Average distribution differences between corpora:')
        file.write('\nArticles vs. Transcripts: ' + str(average_difference('articles.AGGREGATE.txt', 'transcripts.AGGREGATE.txt')))
        file.write('\nArticles vs. Quotes: ' + str(average_difference('articles.AGGREGATE.txt', 'quotes.AGGREGATE.txt')))
        file.write('\nArticles vs. Control: ' + str(average_difference('articles.AGGREGATE.txt', 'control.AGGREGATE.txt')))
        file.write('\nTranscripts vs. Quotes: ' + str(average_difference('transcripts.AGGREGATE.txt', 'quotes.AGGREGATE.txt')))
        file.write('\nTranscripts vs. Control: ' + str(average_difference('transcripts.AGGREGATE.txt', 'control.AGGREGATE.txt')))

# four_corpora_chart()
        
article_freq = {'fear': 0.10655737704918032, 'anger': 0.10655737704918032, 'trust': 0.1557377049180328, 'surprise': 0.05737704918032787, 'positive': 0.13934426229508196, 'negative': 0.16393442622950818, 'sadness': 0.08196721311475409, 'disgust': 0.03278688524590164, 'joy': 0.04918032786885246, 'anticipation': 0.10655737704918032}
transcript_freq = {'fear': 0.05286343612334802, 'anger': 0.06387665198237885, 'trust': 0.11674008810572688, 'surprise': 0.07488986784140969, 'positive': 0.21806167400881057, 'negative': 0.10352422907488987, 'sadness': 0.048458149779735685, 'disgust': 0.024229074889867842, 'joy': 0.1013215859030837, 'anticipation': 0.1960352422907489}

# chart_matches(article_freq, transcript_freq)
