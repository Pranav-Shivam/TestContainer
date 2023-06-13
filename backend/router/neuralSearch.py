from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens', device='cpu')
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(
            "https://1f961a12-7402-407e-a59f-4dc1c0abd56c.us-east-1-0.aws.cloud.qdrant.io", 
            prefer_grpc=True,
            api_key="B3CLTr0wLyoQdrnXxogSS89eQtQMFzY-6RIvQOdDzRHYaL4OR0pIMQ",
        )
    
    def search(self, text):
        # Convert text query into vector
        vector = self.model.encode(text).tolist()

        # Use `vector` for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,  # We don't want any filters for now
            limit=6  # 5 the most closest results is enough
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function we are interested in payload only
        payloads = [hit.payload for hit in search_result]
        return payloads
