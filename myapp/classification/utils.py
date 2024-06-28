# myapp/utils.py

from transformers import pipeline

# Load the model and tokenizer using a pipeline
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline('sentiment-analysis',model=model_name)  # You can change 'sentiment-analysis' to your specific task

def classify_text(text):
    return classifier(text)
