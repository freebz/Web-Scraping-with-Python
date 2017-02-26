from nltk import ngrams
fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
fourgramsDist[("father", "smelt", "of", "elderberries")]
