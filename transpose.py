# matrix, list of lists of numbers
# transpose the matrix

# written after interview
def transpose_3(matrix):
  return list(zip(*matrix))

def transpose_2(matrix):
  return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def transpose(matrix: list[list]) -> list[list]:
  m = len(matrix)
  n = len(matrix[0])

  matrix_ = [[0] * m for _ in range(n)]

  for i, row in enumerate(matrix):
    for j, a in enumerate(row):
      matrix_[j][i] = a

  return matrix_

M = [
  [1, 2, 3, 4],
  [4, 5, 6, 7],
  [7, 8, 9, 10]
]

M_T = [
  [1, 4, 7],
  [2, 5, 8],
  [3, 6, 9],
  [4, 7, 10]
]

assert transpose(M) == M_T
assert transpose_2(M) == M_T

# returns a list of tuples -- written post-interview
assert transpose_3(M) == [tuple(row) for row in M_T]
