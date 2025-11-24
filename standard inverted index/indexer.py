import os
from utils import preprocess, tokenize

class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        clean = preprocess(text)
        tokens = tokenize(clean)

        for token in tokens:
            if token not in self.index:
                self.index[token] = {}

            if doc_id not in self.index[token]:
                self.index[token][doc_id] = 0

            self.index[token][doc_id] += 1

    def display(self):
        for term, postings in sorted(self.index.items()):
            print(f"{term} → {postings}")
