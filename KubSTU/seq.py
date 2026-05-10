data = open("ancient_note.txt", encoding="utf-8").read()

chars = set(c for c in data if ord(c) > 127)
print(chars)
