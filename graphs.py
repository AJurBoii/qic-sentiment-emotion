import matplotlib.pyplot as plt
import numpy as np
import os

article_affects = {'fear': 0.0674939280121633, 'anger': 0.06059309720816781, 'trust': 0.1541022584325241, 'surprise': 0.05005209066861874, 'positive': 0.23911783626456767, 'negative': 0.10756575649816863, 'sadness': 0.05715567533217143, 'disgust': 0.027095992878862076, 'joy': 0.09212697918142294, 'anticipation': 0.14469638552333328}
quotes_affects = {'fear': 0.05547474577153782, 'anger': 0.04809325553772946, 'trust': 0.15820065017022955, 'surprise': 0.061133359287242825, 'positive': 0.2512255783217078, 'negative': 0.08418291059043491, 'sadness': 0.04401766518960819, 'disgust': 0.02355540457102899, 'joy': 0.11576402440989984, 'anticipation': 0.1583524061505806}


'''
Input: text file where each line is a dictionary, where keys are emotions and values are
counts of that emotion
    i.e. articles_RAW_SCORES.txt

Output: text file:
    output_name_AGGREGATE.txt - two dictionaries, aggregate raw counts and aggregate 
    frequencies
'''
def aggregate(text_file, output_name):
    aggregated_counts = {}
    aggregated_frequencies = {}
    total = 0
    with open(text_file, 'r') as file:
        # skip first line
        next(file)
        for line in file:
            dict = eval(str(line))
            for key in dict.keys():
                if key in aggregated_counts:
                    aggregated_counts[key] += dict[key]
                else:
                    aggregated_counts[key] = dict[key]
                total += dict[key]
                aggregated_frequencies[key] = 0
        for key in aggregated_counts.keys():
            aggregated_frequencies[key] = aggregated_counts[key] / total
    with open(f'outputs/aggregated data/{output_name}.AGGREGATE.txt', 'w') as file:
        file.write('Aggregated raw counts:\n')
        file.write(str(aggregated_counts))
        file.write('\nAggregated frequencies:\n')
        file.write(str(aggregated_frequencies))

if (not os.path.isfile('outputs/aggregated data/articles.AGGREGATE.txt')):
    aggregate('outputs/articles_RAW_SCORES.txt', 'articles')
if (not os.path.isfile('outputs/aggregated data/quotes.AGGREGATE.txt')):
    aggregate('outputs/quotes_by_article_RAW_SCORES.txt', 'quotes')
if (not os.path.isfile('outputs/aggregated data/transcripts.AGGREGATE.txt')):
    aggregate('outputs/transcripts_RAW_SCORES.txt', 'transcripts')


'''
Input: text file of aggregated emotion vectors
Output: png of matplotlib pie chart
'''
def pie_chart(aggregate_file, chart_name):
    if (not os.path.isfile(f'outputs/charts/{chart_name.lower()}_affect.png')):
        file = open(aggregate_file, 'r')
        for i in range(3):
            next(file)
        frequencies = eval(next(file))
        print(frequencies)
        chart_labels = []
        data = []
        for key in frequencies.keys():
            chart_labels.append(key)
            data.append(frequencies[key])
        fig, ax = plt.subplots()
        ax.pie(data, labels=chart_labels, textprops={'size': 'smaller'}, autopct='%.2f')
        ax.set_title(f'{chart_name} Affect Frequencies')
        plt.savefig(f'outputs/charts/{chart_name.lower()}_affect.png')

pie_chart('outputs/aggregated data/articles.AGGREGATE.txt', 'Articles')
pie_chart('outputs/aggregated data/quotes.AGGREGATE.txt', 'Quotes')
pie_chart('outputs/aggregated data/transcripts.AGGREGATE.txt', 'Transcripts')