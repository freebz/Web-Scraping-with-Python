from nltk import FreqDist
fdist = FreqDist(text6)
fdist.most_common(10)

fdist["Grail"]
