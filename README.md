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

## To-Do ##
- ~~Test for large inputs~~
  - ~~Transcripts tend to be longer than articles~~
- ~~Aggregate data~~
- ~~Graph results~~
- Find data for control group
  - Standard news articles, blogposts, etc.
- Draft questions for larger group analysis based on graph visualizations
