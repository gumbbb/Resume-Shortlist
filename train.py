import spacy
from spacy.tokens import DocBin
from spacy.training import Example
import json

def load_data(train_data_path):
    with open(train_data_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("annotations", [])

def create_training_data(annotations):
    nlp = spacy.blank("en")
    doc_bin = DocBin()

    for item in annotations:
        text, annot = item
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is not None:
                ents.append(span)
        doc.ents = ents
        doc_bin.add(doc)
    
    return doc_bin

def train_model(train_data_path, output_dir, iterations=20):
    annotations = load_data(train_data_path)
    doc_bin = create_training_data(annotations)
    
    # Save training data
    doc_bin.to_disk("train.spacy")
    
    # Initialize model
    nlp = spacy.blank("en")

    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")
    
    # Add labels
    for item in annotations:
        _, annot = item
        for _, _, label in annot.get("entities", []):
            ner.add_label(label)
    
    optimizer = nlp.begin_training()

    for itn in range(iterations):
        losses = {}
        examples = []
        for doc in doc_bin.get_docs(nlp.vocab):
            examples.append(Example.from_dict(doc, {"entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]}))
        
        batches = spacy.util.minibatch(examples, size=4)
        for batch in batches:
            nlp.update(batch, drop=0.3, losses=losses)
        print(f"Iteration {itn}, Losses: {losses}")
    
    nlp.to_disk(output_dir)
    print(f"Model saved to {output_dir}")

if __name__ == "__main__":
    train_data_path = "path/GO_annotated_cleaned.json"
    output_dir = "trained_model"
    train_model(train_data_path, output_dir)