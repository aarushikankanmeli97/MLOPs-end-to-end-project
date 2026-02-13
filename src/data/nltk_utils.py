import nltk
from nltk.corpus import stopwords as _stopwords


def get_stopwords(lang: str = 'english'):
    """Return stopwords for `lang`, download resource if missing."""
    try:
        return set(_stopwords.words(lang))
    except LookupError:
        nltk.download('stopwords', quiet=True)
        return set(_stopwords.words(lang))
