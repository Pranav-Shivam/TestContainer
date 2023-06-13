# Import client library
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import numpy as np
import json

qdrant_client = QdrantClient(
            "https://1f961a12-7402-407e-a59f-4dc1c0abd56c.us-east-1-0.aws.cloud.qdrant.io", 
            prefer_grpc=True,
            api_key="B3CLTr0wLyoQdrnXxogSS89eQtQMFzY-6RIvQOdDzRHYaL4OR0pIMQ",
        )
qdrant_client.recreate_collection(
    collection_name='startups', 
    vectors_config=VectorParams(size=768, distance=Distance.COSINE),
)

json_path="./startups_demo.json"
fd = open(json_path)

# payload is now an iterator over startup data
payload = map(json.loads, fd)

# Here we load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if we don't want to load all data into RAM




np.save("startup_vectors.npy",allow_pickle=True)
vectors = np.load('./startup_vectors.npy',allow_pickle=True)


qdrant_client.upload_collection(
    collection_name='startups',
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)