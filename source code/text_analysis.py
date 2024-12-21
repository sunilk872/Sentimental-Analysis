from transformers import pipeline
classifier = pipeline('sentiment-analysis')
classifier('We are happy to show the result. ')