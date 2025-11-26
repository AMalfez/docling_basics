from docling.chunking import HybridChunker
from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer
from transformers import AutoTokenizer

path = './sample_data/alfez_mansuri_resume.pdf'  # file path or URL

converter = DocumentConverter()
document = converter.convert(path).document  # type of document is DoclingDocument


EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
MAX_TOKENS = 64  # set to a small number for illustrative purposes

tokenizer = HuggingFaceTokenizer(
    tokenizer=AutoTokenizer.from_pretrained(EMBED_MODEL_ID),
    max_tokens=MAX_TOKENS,  # optional, by default derived from `tokenizer` for HF case
)

chunker = HybridChunker(tokenizer=tokenizer)  # for token aware chunking with semantic splitting
chunk = chunker.chunk(dl_doc=document)

for i, c in enumerate(chunk):
    print(f"--- Chunk {i+1} ---")
    print(f"chunk.text, {tokenizer.count_tokens(c.text)} tokens:\n{f'{c.text[:300]}…'!r}")  # Print first 300 characters of each chunk
    enriched_text = chunker.contextualize(chunk=c)
    print(f"chunker.contextualize(chunk), {tokenizer.count_tokens(enriched_text)} tokens:\n{f'{enriched_text[:300]}…'!r}")  # metadata enriched text, Ideal for feeding into embedding models
    print("\n")