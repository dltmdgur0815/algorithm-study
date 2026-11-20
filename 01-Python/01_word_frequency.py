import re

def word_frequency(text):
    counts = {}
    for word in re.findall(r"[^\W\d_]+", text.casefold()):
        counts[word] = counts.get(word, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))
