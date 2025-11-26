from docling.document_converter import DocumentConverter

source = "./sample_data/alfez_mansuri_resume.pdf"  # file path or URL
converter = DocumentConverter()

print("="*6)
print(" Converting pdf to markdown ")
print("="*6)

doc = converter.convert(source).document

print("\n")
print("="*6)
print(" Conversion done and exporting as markdown ")
print("="*6)

with open('output/simple_pdf_markdown.md', 'w', encoding='utf-8') as f:
    f.write(doc.export_to_markdown())

print("\n")
print("="*6)
print(" Exported ")
print("="*6)
