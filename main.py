from pdf_extractor import extract_text
from predict import predict_entities
import argparse

def main(pdf_path, model_path):
    # Extract text from PDF
    text = extract_text(pdf_path)

    # Predict entities
    entities = predict_entities(text, model_path)
    names = [entity for entity, label in entities if label == "NAME"]
    emails = [entity for entity, label in entities if label == "EMAIL"]

    print(f"NAME: {names[0]} | EMAIL: {emails[0]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract names and emails from PDF using NER")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("model_path", help="Path to the trained NER model")
    args = parser.parse_args()
    main(args.pdf_path, args.model_path)