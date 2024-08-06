#!/usr/bin/python3

"""
pascal_triangle
"""

def pascal_triangle(n):
  """
   returns a list of lists of integers representing the Pascal’s triangle of n
   """

  if n <= 0:
    return []
  triangle = [[1]]
  if n == 1:
    return triangle
  triangle.append([1, 1])
  if n == 2:
    return triangle
  while(len(triangle) < n):
    triangleLen = len(triangle)
    expectedRowLen = triangleLen + 1
    row = []
    prevRow = triangle[triangleLen - 1]
    for i in range(expectedRowLen):
      if i == 0 or i == expectedRowLen - 1:
        # means it's the edge of the row
        row.append(1)
      else:
        # add the 2 col(i - 1 & n) in the prev row to get curr val
        currVal = prevRow[i - 1] + prevRow[i]
        row.append(currVal)
    triangle.append(row)
  return triangle
