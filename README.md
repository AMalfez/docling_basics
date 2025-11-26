# **Docling Basics --- Extract, Convert & Chunk Documents Easily 📄➡️🧠**

Learn the essentials of **Docling**, an open-source library for
converting and extracting content from multiple document formats ---
PDF, Word, PPTX, Markdown, and even **audio**!

This project is a hands-on playground where I explored:

-   Converting files → Markdown\
-   Running ASR on audio files\
-   Using Docling's **HybridChunker**\
-   Enabling *Image Description* inside documents\
-   Batch-processing multi-format files

------------------------------------------------------------------------

## 🚀 **Features**

✔️ Convert PDFs, DOCX, PPTX, and Markdown → `.md`\
✔️ Extract audio transcripts using **Whisper Turbo**\
✔️ Use **HybridChunker** for semantic + token-aware chunking\
✔️ Add **image descriptions** during PDF conversion\
✔️ Clean and beginner-friendly scripts for each feature\
✔️ Output saved neatly inside the `output/` directory

------------------------------------------------------------------------

## 📁 **Project Structure**

    docling-basics/
    │
    ├── sample_data/              # Sample PDF/DOCX/PPTX/Audio files
    ├── output/                   # Converted markdown outputs (ignored in git)
    ├── venv/                     # Virtual environment (ignored in git)
    │
    ├── audio.py                  # Audio → Markdown transcript
    ├── simple_pdf.py             # PDF → Markdown conversion
    ├── multi_formats.py          # Convert multiple file types
    ├── converter_with_image_desc.py  # PDF conversion + image captions
    ├── chunker.py                # HybridChunker example
    │
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🔧 **Installation**

``` bash
git clone https://github.com/<your-username>/docling-basics
cd docling-basics

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

------------------------------------------------------------------------

## 📌 **Examples**

### **1. Convert Audio → Markdown**

`audio.py` uses **Docling ASR Pipeline** with Whisper Turbo.

------------------------------------------------------------------------

### **2. Convert a PDF**

``` bash
python simple_pdf.py
```

------------------------------------------------------------------------

### **3. Convert Multiple Formats at Once**

``` bash
python multi_formats.py
```

------------------------------------------------------------------------

### **4. PDF → Markdown + Image Descriptions**

Enables image captioning using Granite Picture Description.

------------------------------------------------------------------------

### **5. Document Chunking using HybridChunker**

Used for semantic + token-aware chunking, ideal for RAG pipelines.

------------------------------------------------------------------------

## 📦 **Requirements**

    docling
    hf_xet
    openai-whisper
    transformers

------------------------------------------------------------------------

## 📚 **What I Learned**

-   How Docling handles multi-format conversion under the hood\
-   How tokenization affects chunking\
-   Why **HybridChunker** is better for embeddings\
-   How ASR pipelines work with Whisper Turbo\
-   Adding structured metadata + captions to documents

------------------------------------------------------------------------

## 🔗 **Docling Documentation**

https://docling-project.github.io/docling/

------------------------------------------------------------------------

## 🙌 **Contributions**

PRs and suggestions are welcome.

------------------------------------------------------------------------

## ⭐ If you found this useful, consider starring the repo!
