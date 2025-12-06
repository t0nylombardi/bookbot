def count_words(text):
    words = text.split()
    return len(words)


def count_unique_chars(text):
    words = text.lower().split()
    unique_chars = {}
    for word in words:
        for char in word:
            unique_chars[char] = unique_chars.get(char, 0) + 1

    return sorted(unique_chars.items(), key=lambda item: item[1], reverse=True)
