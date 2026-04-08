def read_file(filepath):
    with open(filepath, "r", encoding = "utf-8") as f:
        return f.read()

def count_words(text):
    separators = [",", ":", ";", "\n"]
    for sep in separators:
        text = text.replace(sep, " ")
    words = [w for w in text.split(" ") if w.strip()]
    return len(words)

def count_sentences(text):
    count = 0
    i = 0
    while i < len(text):
        if text[i:i+3] == "...":
            count += 1
            i += 3
        elif text[i] in ".!?":
            count += 1
            i += 1
        else:
            i += 1

    return count
