def flatten(list_):
  out = []
  for item in list_:
    if isinstance(item, list):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

assert flatten([[4,5],[[1,2,3]],6]) == [4,5,1,2,3,6]

print(flatten([[4,5],[[1,2,3]],6]))
