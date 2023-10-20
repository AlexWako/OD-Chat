import tensorflow as tf
from tensorflow.keras.models import Sequential

def sort(model, tokenizer, text):
    result = model.predict(text)
    return result