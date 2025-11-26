def run(text):
    
    # Remove leading/trailing spaces
    text = text.strip()

    # Character count (including spaces)
    char_count = len(text)

    # Character count (excluding spaces)
    char_no_space = len(text.replace(" ", ""))

    # Word count
    words = text.split()
    word_count = len(words)

    # Sentence count (split by . ? !)
    import re
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip() != ""]
    sentence_count = len(sentences)

    # Average word length
    avg_word_len = sum(len(word) for word in words) / word_count if word_count > 0 else 0

    # Average sentence length (in words)
    avg_sentence_len = word_count / sentence_count if sentence_count > 0 else 0

    print("\n--- TEXT STATISTICS ---")
    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (without spaces): {char_no_space}")
    print(f"Word count: {word_count}")
    print(f"Sentence count: {sentence_count}")
    print(f"Average word length: {round(avg_word_len, 2)}")
    print(f"Average sentence length: {round(avg_sentence_len, 2)}")
    

text = 'Hello there! How are you? I am fine.'
run(text)
