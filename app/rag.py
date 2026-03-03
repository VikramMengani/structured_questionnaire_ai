import os
import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer

index = None
chunks = []
metadata = []
vectorizer = None


def split_text(text, chunk_size=500, overlap=50):
    result = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        result.append(text[start:end])
        start += chunk_size - overlap
    return result


def load_reference_docs(folder="references"):
    global index, chunks, metadata, vectorizer

    chunks = []
    metadata = []

    documents = []

    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                documents.append((file, f.read()))

    for filename, content in documents:
        split_chunks = split_text(content)
        for chunk in split_chunks:
            chunks.append(chunk)
            metadata.append(filename)

    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(chunks).toarray().astype("float32")

    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    return index, chunks, metadata, vectorizer