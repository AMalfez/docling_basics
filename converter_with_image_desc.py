from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    granite_picture_description
)
from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter

pipline_options = PdfPipelineOptions()
pipline_options.do_picture_description = True
pipline_options.picture_description_options = granite_picture_description

path = './sample_data/Welcome_to_Word.docx'

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfPipelineOptions(pipline_options=pipline_options)
    }
)

output = './output/converter_with_image_description.md'

doc = converter.convert(path).document

with open(output, 'w', encoding='utf-8') as f:
    f.write(doc.export_to_markdown())