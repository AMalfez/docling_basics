from docling.document_converter import DocumentConverter
from pathlib import Path

converter = DocumentConverter()

documents = [
    './sample_data/alfez_mansuri_resume.pdf',
    './sample_data/Basic_presentation.pptx',
    './sample_data/tweeter_post_generator.md',
    './sample_data/Welcome_to_Word.docx'
]


print(f"Converting documents to markdown\n")

for doc in documents:
    output = f"./output/{Path(doc).stem}.md"
    d = converter.convert(doc).document
    with open(output,'w',encoding='utf-8') as f:
        f.write(d.export_to_markdown())

print("Done")


