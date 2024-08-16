import spacy
import regex as re

def predict_entities(text, model_dir):
    nlp = spacy.load(model_dir)
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    email_entities = [ent for ent in entities if ent[1] == "EMAIL"]
    
    if not email_entities:
        # Regex pattern for email detection
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        entities.extend([(email, "EMAIL") for email in emails])
    
    return entities