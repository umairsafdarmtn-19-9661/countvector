from sklearn.feature_extraction.text import CountVectorizer

# list of text documents
text = ["MY NAME IS UMAIR AND UMAIR NAME IS USE FOR BOY"]

vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)

print(vectorizer.vocabulary_)

# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(vector.toarray())