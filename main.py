def read_file(filepath):
    with open(filepath, "r", encoding = "utf-8") as f:
        return f.read()