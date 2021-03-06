# -*- coding: utf-8 -*-
"""01_텍스트분석.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qrgDMk3FJUBsupX7_YVs9w--ikzlhpkd

- 참고 : https://wikidocs.net/book/2155

# Bag Of Words

## 1.CountVectorizer
"""

from sklearn.feature_extraction.text import CountVectorizer
text = 'Nintendo Switch Sports brings that idea to a new wave of families. Snapping off the Joy-Con controllers, you hand one to another person and compete in one of six simple sports'

cvect = CountVectorizer()
cvect.get_params()

# Cvect 도 학습을 할 땐 리스트여야됨.
output = cvect.fit_transform([text])
output

output.toarray()

cvect.vocabulary_

"""### 불용어 제거"""

# 방법1. 불용어 자체제거
cvect = CountVectorizer(stop_words = ['in','to','that'])
print(cvect.fit_transform([text]).toarray())
print(cvect.vocabulary_)

"""- 방법2 : sklearn에서 사용하는 불용어 사용"""

# 방법2
cvect = CountVectorizer(stop_words = 'english')
print(cvect.fit_transform([text]).toarray())
print(cvect.vocabulary_)

"""- 방법3 : nltk 사용"""

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
sw = stopwords.words('english')
len(sw), type(sw)

cvect = CountVectorizer(stop_words = sw)
print(cvect.fit_transform([text]).toarray())
print(cvect.vocabulary_)

"""### 인덱스에 해당하는 단어 알려주는 함수 제작"""

voca = cvect.vocabulary_
for key, value in voca.items():
    print(key, value)

def get_word(index, voca):
    for key, value in voca.items():
        if value == index:
            return key

get_word(5, cvect.vocabulary_)

"""# N-gram
- 연속적인 n 개의 토큰으로 구성된 단어, 문자
- 1-gram(Unigram)
- 2-gram(Bigram)
- 3-gram(Trigram)
- BOW의 약점을 극복하기 위함이다. -> Bag of Bigram
- But, 단어 수가 기하급수적으로 늘어남
"""

text = ['I work at google.', 'I google at work']
cvect = CountVectorizer()
print(cvect.fit_transform(text).toarray())
print(cvect.vocabulary_)

cvect = CountVectorizer(ngram_range = (1, 2)) # Unigram, Bigram 허용
print(cvect.fit_transform(text).toarray())
print(cvect.vocabulary_)

"""# TF - IDF vectorizer
- 빈도수가 높은 것이 중요하지만, 너무 높은 것은 제외해야됨.
"""

text = ['The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research.',
        ' It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam.']

from sklearn.feature_extraction.text import TfidfVectorizer
tvec = TfidfVectorizer(stop_words = 'english')
print(tvec.fit_transform(text).toarray())

# 위의 결과를 보기 쉽게 만들기
cvec = CountVectorizer(stop_words='english')
print(cvec.fit_transform(text).toarray())
print(cvec.vocabulary_)

