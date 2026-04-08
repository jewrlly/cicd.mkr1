def read_file(filepath):
    with open(filepath, "r", encoding = "utf-8") as f:
        return f.read()

def count_words(text):
    separators = [",", ":", ";", "\n"]
    for sep in separators:
        text = text.replace(sep, " ")
    words = [w for w in text.split(" ") if w.strip()]
    return len(words)
