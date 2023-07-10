import numpy as np
import torch

# from chatgpt import ask_gpt
from sentence_transformers import SentenceTransformer

# Load the vector file
vector_list = np.load("example/retrieve/embedding.npy")

# Number of top-k vectors to retrieve
TOP_K = 3


def convert_url(input_url):
    parts = input_url.split("/")

    if len(parts) >= 6 and parts[2] == "doc":
        if parts[3] == "website":
            # Construct the new URL by joining the relevant components
            new_url = "https://www.freebsd.org/" + "/".join(parts[4:-2])
        else:
            new_url = "https://docs.freebsd.org/en/" + "/".join(parts[4:-2])
    else:
        # Extract the last component and remove the file extension
        page_name = parts[-1].split(".")[0]
        new_url = f"https://man.freebsd.org/cgi/man.cgi?query={page_name}&apropos=0&sektion=0&manpath=FreeBSD+15.0-CURRENT&arch=default&format=html"

    return new_url


def init_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)
    return SentenceTransformer("thenlper/gte-base", device=device)


def load_text_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


# Calculate cosine similarity between two vectors
def cosine_similarity_vectorized(a, b):
    dot_product = np.dot(a, b[0])
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b[0])
    similarity = dot_product / (
        norm_a * norm_b
    )  # Cosine Similarity = (A dot B) / (||A|| * ||B||)
    return similarity


def query(question: str):
    question_vector = model.encode(question)

    similarities = []
    for vector in vector_list:
        similarity = cosine_similarity_vectorized(question_vector, vector)
        similarities.append(similarity)

    similarities = np.array(similarities)
    top_indices = np.argsort(similarities)[-TOP_K:][::-1]

    return_chunks = []  # list to return
    chunk_index = 1
    for i in top_indices:
        print(f"--- Top {chunk_index} Result ---")
        print(f"Chunk Text: {chunk_list[i]}")
        return_chunks.append(chunk_list[i])

        print(f"Chunk Location: {path_list[i]}")
        print(f"Possible Online URL: {convert_url(path_list[i])}\n")

        chunk_index += 1

    return return_chunks


# Initialize the model once
model = init_model()

# Load text files once
chunk_list = load_text_file("example/retrieve/embedding_texts.txt")
path_list = load_text_file("example/retrieve/chunk_paths.txt")

question_list = ["How to use the gunion command in FreeBSD?"]

for question in question_list:
    print("Current Question:", question)
    print("Related Chunk Texts:")
    related_chunks = query(question)
    # ask_gpt(question, related_chunks)
