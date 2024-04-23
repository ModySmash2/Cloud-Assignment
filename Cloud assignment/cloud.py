import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')



file = open('paragraphs.txt')

paragragh =  file.read()

stop_words = set(stopwords.words('english'))
words = word_tokenize(paragragh.lower())

clean_words = []
for word in words:
    if word not in stop_words:
        clean_words.append(word)

frequency = {}

for word in clean_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, frequency in frequency.items():
        print(f"{word}: {frequency}")
        
file.close()