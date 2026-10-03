from dotenv import load_dotenv
import os
import voyageai

load_dotenv()

api_key = os.getenv("VOYAGE_API_KEY") or os.getenv("VOYAGEAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "Set VOYAGE_API_KEY in .env before running this embedding example."
    )

client = voyageai.Client(api_key=api_key)
# Chunk by section
import re


def chunk_by_section(document_text):
    pattern = r"\n## "
    return re.split(pattern, document_text)
# Embedding Generation
def generate_embedding(text, model="voyage-3-large", input_type="query"):
    result = client.embed([text], model=model, input_type=input_type)

    return result.embeddings[0]
with open("report.md", "r") as f:
    text = f.read()

chunks = chunk_by_section(text)

print(generate_embedding(chunks[0]))