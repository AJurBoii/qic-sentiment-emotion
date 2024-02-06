import matplotlib.pyplot as plt
import numpy as np

article_affects = {'fear': 0.0674939280121633, 'anger': 0.06059309720816781, 'trust': 0.1541022584325241, 'surprise': 0.05005209066861874, 'positive': 0.23911783626456767, 'negative': 0.10756575649816863, 'sadness': 0.05715567533217143, 'disgust': 0.027095992878862076, 'joy': 0.09212697918142294, 'anticipation': 0.14469638552333328}
quotes_affects = {'fear': 0.05547474577153782, 'anger': 0.04809325553772946, 'trust': 0.15820065017022955, 'surprise': 0.061133359287242825, 'positive': 0.2512255783217078, 'negative': 0.08418291059043491, 'sadness': 0.04401766518960819, 'disgust': 0.02355540457102899, 'joy': 0.11576402440989984, 'anticipation': 0.1583524061505806}

sum = 0

x = []
y = []
article_affect_labels = []
quote_affect_labels = []

for key in article_affects.keys():
    sum += article_affects[key]
    x.append(article_affects[key])
    article_affect_labels.append(str(key))

for key in quotes_affects.keys():
    y.append(quotes_affects[key])
    quote_affect_labels.append(str(key))

print(sum)

colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, labels=article_affect_labels, textprops={'size': 'smaller'})
ax.set_title('Article Affect Frequencies')

plt.savefig('article_affect.png')