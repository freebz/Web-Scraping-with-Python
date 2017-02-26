from nltk import bigrams
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
bigramsDist[("Sir", "Robin")]
