from docling.document_converter import DocumentConverter, AudioFormatOption
from docling.pipeline.asr_pipeline import AsrPipeline
from docling.datamodel import asr_model_specs
from docling.datamodel.pipeline_options import AsrPipelineOptions
from docling.datamodel.base_models import InputFormat
from pathlib import Path

audio_path = "./sample_data/harvard.wav"

print("Initializing Converter \n")

pipeline_options = AsrPipelineOptions()
pipeline_options.asr_options = asr_model_specs.WHISPER_TURBO

converter = DocumentConverter(
    format_options={
        InputFormat.AUDIO: AudioFormatOption(
            pipeline_cls=AsrPipeline,
            pipeline_options=pipeline_options,
        )
    }
)

print("Converting Audio... \n")
doc = converter.convert(audio_path).document


output = f"./output/{Path(audio_path).stem}.md"
with open(output,'w',encoding='utf-8') as f:
    f.write(doc.export_to_markdown())

print("Done and saved the transcript \n")



