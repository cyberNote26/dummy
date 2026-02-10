import faiss
import numpy as np
import pickle
import os

class VectorStore:
    def __init__(self, dimension, cache_file='cache.pkl'):
        self.dimension = dimension
        self.cache = {}
        self.cache_file = cache_file
        self.index = faiss.IndexFlatL2(dimension)

        # Load cache if it exists
        self.load_cache()

    def add_documents(self, documents):
        vectors = [self.encode(doc) for doc in documents]
        self.index.add(np.array(vectors).astype('float32'))

    def encode(self, document):
        # Dummy encoding - replace with actual document embedding logic
        return np.random.rand(self.dimension)

    def search(self, query_vector, k=5):
        distances, indices = self.index.search(np.array([query_vector]).astype('float32'), k)
        return distances, indices

    def save_cache(self):
        with open(self.cache_file, 'wb') as f:
            pickle.dump(self.cache, f)

    def load_cache(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'rb') as f:
                self.cache = pickle.load(f)

    def store_in_cache(self, key, value):
        self.cache[key] = value
        self.save_cache()

    def retrieve_from_cache(self, key):
        return self.cache.get(key, None)