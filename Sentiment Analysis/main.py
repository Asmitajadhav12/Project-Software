import string
from collections import Counter

import nltk
from nltk.langnames import iso639code_retired
from nltk.tokenize import word_tokenize #with nltk
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer #to analyze +ve or -ve sentiments
import matplotlib.pyplot as plt
text = open('read.txt', encoding ='utf-8').read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
#print(cleaned_text)
#with nltk
tokenized_words = nltk.word_tokenize(cleaned_text,"english")
#without nltk
# tokenized_words = cleaned_text.split()#tokenization - to split sentences into words
#print(tokenized_words)

#with nltk
final_words = []#creating empty list for final words
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)
#print(final_words)

#without nltk
"""stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []#creating empty list for final words
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
#print(final_words)
"""


"""nlp emotion algorithm
1 Check if the word in the final word list is also present in emotion.txt
open the emotion file
Loop through each line and clear it
Extract the word and emotion using split

2 If word is present . Add the emotion to emotion_list
3 Finally count each emotion in the emotion list"""
emotions_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line =line.replace("\n",'').replace(",",'').replace("'",'').strip()
        # print(clear_line)
        word, emotion = clear_line.split(':')
        #(print("Word :"+word+"Emotion :"+emotion )

        if word in final_words:
            emotions_list.append(emotion)
#print(emotions_list)
#use of counter
w = Counter(emotions_list)
print(w)

#to analyze +ve or -ve sentiments
def sentiment_analyser(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
        print("Negative Sentiment")
    elif pos > neg:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentiment_analyser(cleaned_text)

#plotting the emotions on the graph
#possible because of matplotlib
fig , ax = plt.subplots()#created  subplot that has fig and axis
ax.bar(w.keys(),w.values())#keys are the emotions, values are the no. of times it occurs
fig.autofmt_xdate()#automatic update x and y axis to make sure they fit properly without overlapping
plt.savefig('graph.png')#saving the result as graph.png
plt.show()#show the image

