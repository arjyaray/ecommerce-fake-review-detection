import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# # Download required NLTK resources (only first time)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')


stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    """
    Basic text cleaning:
    - Lowercase
    - Remove URLs
    - Remove numbers
    - Remove punctuation
    """
    text = text.lower()
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.strip()
    return text


def tokenize_text(text):
    """
    Tokenize text into words
    """
    return word_tokenize(text)


def remove_stopwords(tokens):
    """
    Remove English stopwords
    """
    return [word for word in tokens if word not in stop_words]


def lemmatize_tokens(tokens):
    """
    Lemmatize tokens to base form
    """
    return [lemmatizer.lemmatize(word) for word in tokens]


def preprocess_text(text):
    """
    Full preprocessing pipeline
    """
    text = clean_text(text)
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    return " ".join(tokens)
