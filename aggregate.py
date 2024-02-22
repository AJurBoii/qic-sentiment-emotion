from nrclex import NRCLex
import matplotlib.pyplot as plt
from statistics import median
import numpy as np
import os
import sys
import csv

# Determines the order in which data is plotted on the pie charts;
# Ensures that the chart for each corpus uses the same colors for the same emotions
emotions = ['positive', 'negative', 'anticipation', 'joy', 'fear', 'trust', 'sadness', 'disgust', 'surprise', 'anger']

'''
Input: text file where each line is a dictionary, where keys are emotions and values are
counts of that emotion
    i.e. articles_RAW_SCORES.txt

Output: text file:
    [output_name].AGGREGATE.txt - two dictionaries, aggregate raw counts and aggregate 
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

    
'''
    input: raw_matched_trans.csv, a csv file where each row contains
    an article and a transcript that have been matched to each other based on the
    presence of the same quote in both texts

    output: MATCHED_art_trans.AFFECT_FREQUENCIES.csv, a csv file with 4 columns:
    article emotions, transcript emotions, emotion differences, average emotion difference

'''
def matched_analysis(text_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        output = open('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv', 'w', newline='')
        fieldnames = ['article_frequency', 'transcript_frequency', 'emotion_differences', 'average_difference']
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            article_object = NRCLex(row['raw_article'])
            transcript_object = NRCLex(row['raw_transcript'])

            article_freq = article_object.affect_frequencies
            transcript_freq = transcript_object.affect_frequencies

            # delete faulty 'anticip' value from frequency dict
            del article_freq['anticip']
            del transcript_freq['anticip']

            differences = {}
            total = 0
            for emotion in emotions:
                diff = abs(article_freq[emotion] - transcript_freq[emotion])
                total += diff
                differences[emotion] = diff
            average = total / len(emotions)

            row_to_write = {'article_frequency': article_freq, 'transcript_frequency': transcript_freq, 'emotion_differences': differences, 'average_difference': average}
            writer.writerow(row_to_write)

'''
    input: csv file with 4 columns, where one column contains average difference of
    emotion distributions between an article and a transcript document

    output: top_bottom_five_matches.txt, the values of the top and bottom 5 average
    differences
'''
def top_bottom(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # first loop: collect averages to sort
        all_averages = []
        for row in reader:
            all_averages.append(float(row['average_difference']))

        # sort in both ascending (bottom 5) and descending (top 5) order
            
        outfile = open('outputs/matched articles transcripts/top_bottom_matches.txt', 'w')

        all_averages.sort()
        outfile.write(f'Ascending:\n{str(all_averages)}\n')

        all_averages.sort(reverse=True)
        outfile.write(f'Descending:\n{str(all_averages)}')

        outfile.close()

def average_matched_difference(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        sum = 0
        num_rows = 0

        reader = csv.DictReader(file)
        for row in reader:
            sum += float(row['average_difference'])
            num_rows += 1
    return sum/num_rows

def mean_difference(filename):
    differences = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            differences.append(float(row['average_difference']))
    
    return median(differences)
        



''' Taking in command line arguments:
    FORMAT:
        python graphs.py [a/aggregate/g/graph] [file_name] [label for generated file/chart]
'''    
num_args = len(sys.argv)
if num_args < 3:
    # matched_analysis('data/raw_matched_art_trans.csv')
    top_bottom('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv')
    # with open('outputs/matched articles transcripts/average_difference.AGGREGATE.txt', 'w') as file:
    #     file.write(str(average_matched_difference('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv')))
    # print(mean_difference('outputs/matched articles transcripts/MATCHED_art_trans.AFFECT_FREQUENCIES.csv'))

else:
    file_name = sys.argv[1]
    label = sys.argv[2]
    aggregate(file_name, label)
    print("\nFile aggregated successfully")