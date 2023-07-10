# Retrieve plugin

This implementation utilizes an open-source embedded model ([gte-base](https://huggingface.co/thenlper/gte-base)) to convert the data into a set of vectors. These vectors are then saved as a file, allowing you to query the top `TOP_K` closest sentences to your question using Cosine Similarity. These retrieved sentences can serve as additional context for your questions, enhancing ChatGPT's ability to provide accurate answers.

You're free to switch out the embedded model or the algorithm used for calculating similarities. Just remember to consider the token limit of the model. We chose the gte-base model because it has shown strong performance on the [MTEB leaderboard](https://huggingface.co/thenlper/gte-base).

This project draws inspiration from the [chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) and achieves similar functionality. However, unlike the plugin, we do not utilize an online vector database. We made this choice because we believe the data is meant solely for your use, and it isn't too extensive in size. Nevertheless, it's worth noting that this project can be easily extended to include a vector database if you needed.

```
CHUNK_SIZE = 512
MIN_CHUNK_LENGTH_TO_EMBED = 50 
```

## Installation

```
$ pip install -r requirements.txt
```

## Usage

Execute `query/query.py` to retrieve relevant sentences related to your queries. This script utilizes `main.py` to obtain embedding vectors.

For those using the ChatGPT API, there is a version called `query/chatgpt.py` that works with it. However, it is essential to provide your OpenAI key as an environment variable (`OPENAIKEY`)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)