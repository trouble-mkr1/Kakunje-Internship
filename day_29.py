# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize


# text = "python is a high-level, object-oriented programming languag. It is easy"

# nltk.download('punkt')
# nltk.download('punkt_tab')

# words = word_tokenize(text)
# print("word tokens are: ", words)

# sentence = sent_tokenize(text)
# print("sentence tokens are: ", sentence)

# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# words = ["happily", "happier", "playing", "player"]
# for word in words:
#     print(word, "->", ps.stem(word))
# print()

# from nltk.stem import SnowballStemmer
# ss = SnowballStemmer('english')
# for word in words:
#     print(word, "->", ss.stem(word))
# print()

# from nltk.stem import LancasterStemmer
# ls = LancasterStemmer()
# for word in words:
#     print(word, "->", ls.stem(word))
# sentence = "The boys are playing happily in the playground"
# words = word_tokenize(sentence)
# for w in words:
#     print(w, "->", ls.stem(w))

# from nltk.stem import WordNetLemmatizer
# l = WordNetLemmatizer()
# words = ["runs", "happily", "studies", "better"]
# for w in words:
#     print(w, "->", l.lemmatize(w))
# print(l.lemmatize("running", pos = "v")) # pos is parts of speech, v is verb
# print(l.lemmatize("better", pos = "a")) # a is adjective, "better" is converted to "a" and printed
# from nltk import pos_tag
# sentence = "The boys are playing happily in the playground"
# words = word_tokenize(sentence)
# pos = pos_tag(words)
# print(pos)

# from nltk.corpus import stopwords
# text =  "The boys are playing happily in the playground"
# words = word_tokenize(text)
# stop_words = set(stopwords.words("english"))
# print(stop_words)
# filtered_words = []
# for w in words:
#     if w.lower() not in stop_words:
#         filtered_words.append(w)
# print(filtered_words)

#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# def message():
#     print("Button clicked")

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("My first pyQt Window")
# window.resize(300, 200)

# label = QLabel("Hello from PyQt", window)
# label.move(100, 50)

# button = QPushButton("Click me", window)
# button.move(100, 80)

# msg = QLabel("", window)
# msg.move(100, 110)
# button.clicked.connect(message)
# window.show()
# sys.exit(app.exec_())



# def message():
#     msg.setText("hellooo")

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("My first pyQt Window")
# window.resize(300, 200)

# label = QLabel("Hello from PyQt", window)
# button = QPushButton("Click me", window)
# msg = QLabel("", window)

# layout = QVBoxLayout()
# layout.addWidget(label)
# layout.addWidget(button)
# layout.addWidget(msg)
# window.setLayout(layout)
# button.clicked.connect(message)
# window.show()
# sys.exit(app.exec_())


print("=======================================================")
print("=======================================================")
print("=======================================================")
print("=======================================================")


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# def message():
#     msg.setText("Hello Student!")

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("Task 1")
# window.resize(300, 200)

# button = QPushButton("Click me", window)
# msg = QLabel("", window)

# layout = QVBoxLayout()
# layout.addWidget(button)
# layout.addWidget(msg)
# window.setLayout(layout)
# button.clicked.connect(message)
# window.show()
# sys.exit(app.exec_())

print("=======================================================")

import nltk
print("part 1: Sentence Tokenization\n")
from nltk.tokenize import sent_tokenize

text = "Online shopping has become very convenient today. Customers expect fast delivery and good product quality."

sentence = sent_tokenize(text)
print("sentence tokens are: ", sentence)

print("=======================================================")
print("part 2: Word Tokenization\n")

from nltk.tokenize import word_tokenize

words = word_tokenize(text)
print("word tokens are: ", words)

print("=======================================================")
print("part 3:  Stemming\n")

from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["delivery", "delivering", "delivered", "customers", "shopping", "quality"]
w = []
for i in words:
    w.append(ps.stem(i))
print("Original words: ")
print(words)
print()
print("Stemmed words: ")
print(w)

print("=======================================================")
print("part 4:  Parts of Speech (POS Tagging)\n")

from nltk import pos_tag
words = word_tokenize(sentence[0])
pos = pos_tag(words)
print(pos)

print("\n=======================================================")
print("Part 5: Stopword Removal\n")

from nltk.corpus import stopwords

words = word_tokenize(sentence[0])
stop_words = set(stopwords.words("english"))
filtered_words = []
for w in words:
    if w.lower() not in stop_words:
        filtered_words.append(w)
print("Original words: ")
print(words)
print()
print("Filtered words(Stopwords Removed): ")
print(filtered_words)