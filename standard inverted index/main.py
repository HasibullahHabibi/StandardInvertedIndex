import os
from indexer import InvertedIndex
from btree import BTree

# -------------------------------
# Path to documents folder
# -------------------------------
DOCS_PATH = "docs/"

def load_documents(path):
    docs = {}
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            file_path = os.path.join(path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    print("Loading documents...")
    documents = load_documents(DOCS_PATH)

    print("Building inverted index...\n")
    idx = InvertedIndex()

    for doc_id, text in documents.items():
        idx.add_document(doc_id, text)

    idx.display()

    print("\nBuilding B-Tree Dictionary...\n")
    btree = BTree(t=3)

    for term in idx.index.keys():
        btree.insert(term)

    print("\nB-Tree Structure:")
    btree.print_tree()

    # Example Search
    print("\nSearch term: 'machine'")
    result = btree.search("machine")
    if result:
        print("Found in B-Tree:", result)
    else:
        print("Not found.")
