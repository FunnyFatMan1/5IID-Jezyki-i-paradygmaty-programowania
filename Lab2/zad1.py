import re
from collections import Counter

def text_analysis(text):
    # Zliczanie akapitów, zdań i słów
    paragraphs = text.split('\n\n')
    sentences = re.split(r'[.!?]', text)
    words = re.findall(r'\b\w+\b', text)

    paragraph_count = len(paragraphs)
    sentence_count = len([s for s in sentences if s.strip()])
    word_count = len(words)

    # Najczęściej występujące słowa (bez stop words)
    stop_words = {"a", "the", "an", "and", "or", "is", "it", "to", "of", "in"}
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    most_common_words = Counter(filtered_words).most_common(5)

    # Transformacja słów zaczynających się na "a" lub "A"
    transformed_words = [word[::-1] if word.lower().startswith('a') else word for word in words]

    return {
        "paragraph_count": paragraph_count,
        "sentence_count": sentence_count,
        "word_count": word_count,
        "most_common_words": most_common_words,
        "transformed_text": " ".join(transformed_words),
    }