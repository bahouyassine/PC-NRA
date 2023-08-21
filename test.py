import spacy

# Load pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Text to analyze
text = "Check out the new gaming PC with Ryzen 5 7600X and RTX 4060Ti. It has 16 GB RAM and a 1TB SSD."

# Process the text with the NER model
doc = nlp(text)

# Print recognized entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)
