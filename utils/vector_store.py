import numpy as np

class VectorStore:
    def __init__(self):
        self.vectors = []
        self.texts = []

    def add(self, vectors, texts):
        self.vectors.extend(vectors)
        self.texts.extend(texts)

    def search(self, query_vector, top_k=3):
        scores = []

        for i, vec in enumerate(self.vectors):
            sim = self.cosine_similarity(query_vector, vec)
            scores.append((sim, self.texts[i]))

        scores.sort(reverse=True, key=lambda x: x[0])
        return [item[1] for item in scores[:top_k]]

    @staticmethod
    def cosine_similarity(a, b):
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
