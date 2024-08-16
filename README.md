
# PDF Name and Email Extractor

This project extracts names and email addresses from PDF files using Named Entity Recognition (NER).

## Requirements

- Python 3.7+
- spaCy
- PyMuPDF (fitz)
- regex

## Setup

1. Clone the repository:
git clone https://github.com/gumbbb/Golden-Owl-Intern.git
cd Golden-Owl-Intern
2. Install the required packages:
pip install spacy PyMuPDF regex
3. Download the spaCy English model:
python -m spacy download en_core_web_sm

## Usage

1. Train the NER model:
python train.py
2. Run the extractor:
python main.py /path/to/your/pdf/file.pdf /path/to/trained/model
## File Structure

- `train.py`: Script to train the NER model
- `pdf_extractor.py`: Module to extract text from PDF files
- `ner_model.py`: Module for NER prediction
- `main.py`: Main script to run the extraction process
- `GO_annotated_cleaned.json`: Training data for the NER model

## Notes

- The NER model is trained on the provided dataset and may need to be retrained or fine-tuned for optimal performance on different types of documents.
- Email extraction uses a regex pattern in addition to the NER model for improved accuracy.
