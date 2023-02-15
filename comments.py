with open("thing.c", "r") as file:
  data = file.read()

segments = [0]
start = None
for i, ch in enumerate(data):
  if i == len(data) - 1:
    break

  if ch == "/" and data[i + 1] == "*":
    start = i
  if start is not None and ch == "*" and data[i + 1] == "/":
    segments.append(start)
    segments.append(i + 2)
    start = None

segments.append(len(data))

#  0      2       4       6       8       10
# [0, 22, 30, 33, 42, 55, 71, 79, 90, 99, 124, 126]

new = ""
for i in range(0, len(segments), 2):
  new += data[segments[i]:segments[i+1]]

print(segments)
print(new)
