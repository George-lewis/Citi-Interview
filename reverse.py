# --- written post-interview ---
def reverse2_(text: str, delim: list[str]):
  if not delim:
    return text
  d, *rest = delim
  return d.join(reversed([reverse2_(line, rest) for line in text.split(d)]))

def reverse2(text: str):
  return reverse2_(text, ["\b", "\n", " "])

# ------------------------------

def reverse_words(line: str):
  return " ".join(reversed(list(line.split(" "))))

def reverse_lines(lines: str):
  return "\n".join(reversed(list(reverse_words(line) for line in lines.split("\n"))))

def reverse(book: str):
  return "\b".join(reversed(list(reverse_lines(lines) for lines in book.split("\b"))))

book = "the brown fox jumped over the fence\nthe brown bear fell down the hill\n\bThe big lion chased the deer\nThe monkey ate the bananas\n\b"

print(reverse(book))
print(reverse2(book))
