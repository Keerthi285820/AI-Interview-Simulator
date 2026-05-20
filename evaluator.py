from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer('all-MiniLM-L6-v2')
def evaluate_answer (user_answer, expected_answer):
    user_embedding = model.encode([user_answer])
    expected_embedding = model.encode([expected_answer])
    similarity = cosine_similarity(
        user_embedding,
        expected_embedding
    )[0][0]
    score = round(similarity * 100, 2)
    return score