# 8.3.2 NLTK를 사용한 통계적 분석

from nltk import word_tokenize
from nltk import Text

tokens = word_tokenize("Here is some not very interesting text")
text = Text(tokens)
