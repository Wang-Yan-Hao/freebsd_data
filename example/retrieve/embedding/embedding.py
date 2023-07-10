import re
from typing import List, Optional

import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer

CHUNK_SIZE = 512  # Default target size of each text chunk in tokens, limit to your model input size
MIN_CHUNK_LENGTH_TO_EMBED = 50  # Discard chunks shorter than this, unit is token


# Utility
def init_tokenizer():
    global tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "thenlper/gte-base"
    )  # https://huggingface.co/docs/transformers/internal/tokenization_utils


def init_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Using device:", device)
    global model
    model = SentenceTransformer(
        "thenlper/gte-base", device=device
    )  # https://huggingface.co/intfloat/e5-base-v2


def get_embeddings(text: str) -> np.array:
    encoding = model.encode(
        [text], normalize_embeddings=True, batch_size=64
    )  # https://www.sbert.net/examples/applications/computing-embeddings/README.html
    return encoding


def store(path: str, list: List[str]):
    with open(path, "w") as file:
        for string in list:
            file.write(string + "\n")


def text_preprocessing(text: str) -> str:
    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)
    # Replace multiple newline characters with a single space
    text = re.sub(r"\n+", " ", text)
    return text


# Embedding
def create_document_chunks(doc_text: str, chunk_token_size: Optional[int]) -> List[str]:
    if not doc_text or doc_text.isspace():
        return []

    # Use the provided chunk token size or the default one
    chunk_size = chunk_token_size or CHUNK_SIZE

    init_tokenizer()

    doc_text = text_preprocessing(doc_text)

    tokens = tokenizer(
        doc_text, return_overflowing_tokens=True, padding=True, return_tensors="pt"
    )
    tokens = tokens.input_ids[0]
    tokens_list = []

    # Split the tokens into chunks of size 512 or less
    while len(tokens) > MIN_CHUNK_LENGTH_TO_EMBED:
        token = tokens[:chunk_size]
        tokens_list.append(token)
        tokens = tokens[chunk_size:]

    return tokens_list


def get_document_chunks(
    documents: List[str], document_paths: List[str], chunk_token_size: Optional[int]
):
    init_model()
    all_chunks: List[str] = []
    chunk_paths: List[str] = []

    # Loop over each document and create chunks
    for doc, path in zip(documents.document_paths):
        doc_chunks = create_document_chunks(doc, chunk_token_size)
        all_chunks.extend(doc_chunks)
        chunk_paths.extend([path] * len(doc_chunks))

    print(f"There are {len(all_chunks)} chunks in all of the documents")
    store("example/retrieve_plugin/chunk_paths.txt", chunk_paths)

    # Check if there are no chunks
    if not all_chunks:
        return

    # Get all the embeddings for the document chunks in batches, using get_embeddings
    embeddings_vector: List[np.array] = []
    embeddings_texts: List[str] = []

    for i, chunk in enumerate(all_chunks):
        if i % 10000 == 0:
            print(f"Current: {i} chunks")
        original_text = tokenizer.decode(chunk)
        embeddings_texts.append(original_text)
        batch_embeddings = get_embeddings(
            original_text
        )  # Get the embeddings for the batch texts
        embeddings_vector.append(
            batch_embeddings
        )  # Append the batch embeddings to the embeddings list

    # Store the embedding as a file
    np.save("example/retrieve_plugin/embedding.npy", embeddings_vector)
    store("example/retrieve_plugin/embedding_texts.txt", embeddings_texts)
