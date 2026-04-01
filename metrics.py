def calculate_similarity(a, b):
    a_words = set(a.lower().split())
    b_words = set(b.lower().split())

    common = a_words.intersection(b_words)
    return len(common)