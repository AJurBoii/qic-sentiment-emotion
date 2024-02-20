import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Determines the order in which data is plotted on the pie charts;
# Ensures that the chart for each corpus uses the same colors for the same emotions
label_order = ['anticipation', 'joy', 'positive', 'fear', 'trust', 'negative', 'sadness', 'disgust', 'surprise', 'anger']

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

''' Taking in command line arguments:
    FORMAT:
        python graphs.py [a/aggregate/g/graph] [file_name] [label for generated file/chart]
'''        
num_args = len(sys.argv)
if num_args < 4:
    print(f'3 arguments required. Only {num_args-1} provided.')
else:
    file_name = sys.argv[2]
    label = sys.argv[3]
    if str(sys.argv[1]) == 'aggregate' or str(sys.argv[1]) == 'a':
        aggregate(file_name, label)
        print("\nFile aggregated successfully")
    elif sys.argv[1] == 'graph' or sys.argv[1] == 'g':
        pie_chart(file_name, label)
        print("\nFile charted successfully")