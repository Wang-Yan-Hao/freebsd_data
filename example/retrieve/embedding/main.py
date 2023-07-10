import os
import time

from embedding import get_document_chunks

# Clean Data location
folder_path = "./data/"

# Use a list comprehension to get the list of .txt files
fils_paths = [
    os.path.join(root, file)
    for root, _, files in os.walk(folder_path)
    for file in files
    if file.endswith(".txt")
]

print(f"There are {len(fils_paths)} files")

documents = []  # Store all the document content
document_paths = []  # Store the path of the document

# Read all documents
for file_path in fils_paths:
    with open(file_path, "r") as file:
        content = file.read()
        documents.append(content)
        document_paths.append(file_path)

# Start measuring time
start_time = time.time()

CHUNK_SIZE = 512  # The target size of each text chunk in tokens, limited to your model input size
get_document_chunks(documents, document_paths, CHUNK_SIZE)

# Calculate elapsed time
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken for tokenization and inference: {elapsed_time:.4f} seconds")
