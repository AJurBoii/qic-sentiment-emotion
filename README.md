# Overview #
This repository is a contribution to the 2024 Carleton College COMPS group, Quotes in Context (QIC).
QIC Members:
- Aaron Bronstone
- Kevin Bui
- Riaz Kelly
- Daniel Linder
- AJ LeSure (owner of this repo and author of this README!!)

Contained in this repository is code for Emotion Analysis and general Sentiment Analysis, meant to be run on data collected by the QIC group, and to be analyzed by the group.

The program (sentiment_analyzer.py) uses the NRCLex Python library. More info below.

## NRCLex ##
NRCLex (NRC Lexicon) is a Python library that measures the emotional affect from an input text. It's "emotion affect" dictionary contains ~27,000 words based on the National Research Council Canada (NRC)'s affect lexicon. The lexicon also includes the NLTK library's WordNet synonym sets.

Under the terms of use, any research project that uses NRCLex must cite this paper:

Crowdsourcing a Word-Emotion Association Lexicon, Saif Mohammad and Peter Turney, Computational Intelligence, 29 (3), 436-465, 2013
https://doi.org/10.1111/j.1467-8640.2012.00460.x

#### Limitations ####
- Doesn't handle negations very well ("not good," "not bad," etc.)
- Can't categorize words outside of the defined lexicon (key-based analysis)

## Data Collection ##
Data pertaining to sports media is categorized into two main corpora: articles and transcripts. (Quotes do not count as a separate corpus for the sake of data collection, as quotes are a subset of articles). Additionally, as a third corpus, we've collected data on standard news articles to act as a control group for emotion analysis. The source and collection method for each corpus is as follows:
#### Sports Articles ####
Perigon API
- Paid service that provides text data about various articles, blogposts, and other written media.
- API queries can be based on topic, source, authors, year published, etc.
  - We filtered our queries based on college sports from any source
 #### Sports Transcripts ####
 ASAP Sports
 - Website that hosts a sizeable collection of transcripts of post-game interviews, press conferences, etc. for a variety of college sports
 - We scraped the transcripts in the corpus through the use of a custom-made webpage crawler/scraper.
#### Standard News (Control Group) ####
"4000 CNN articles from 2023", by Pedro Araujo Ribeiro, Kaggle.com
[https://www.kaggle.com/datasets/pedroaribe/4000-cnn-articles-as-of-1062023/data]
- Dataset containing around 4,000 CNN articles
- A csv file where each row contains title, abstract, body text, keywords, and theme for a single article

## To-Do ##
- ~~Test for large inputs~~
  - ~~Transcripts tend to be longer than articles~~
- ~~Aggregate data~~
- ~~Graph results~~
- Find data for control group
  - Standard news articles, blogposts, etc.
- Draft questions for larger group analysis based on graph visualizations
