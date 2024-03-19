def max_words_in_sentence(sentences):
    max_words = 0
    for sentence in sentences:
        words = sentence.split()
        max_words = max(max_words, len(words))
    return max_words

sentences = ["Hello world", "This is a sentence", "Python is awesome"]
print("Maximum number of words in a single sentence:", max_words_in_sentence(sentences))

