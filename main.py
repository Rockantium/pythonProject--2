# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def brute_force_solution(a, b, c, d, e, f):
  """Finds an integer solution for x and y in the range -10 to 10 for the system of linear equations ax + by = c and dx + ey = f.

  Args:
    a: The coefficient of x in the first equation.
    b: The coefficient of y in the first equation.
    c: The constant term in the first equation.
    d: The coefficient of x in the second equation.
    e: The coefficient of y in the second equation.
    f: The constant term in the second equation.

  Returns:
    The integer solution for x and y, or None if no solution is found.
  """

  for x in range(-10, 11):
    for y in range(-10, 11):
      if a * x + b * y == c and d * x + e * y == f:
        return x y

  return None


def main():
  """Prompts the user for the coefficients of the two linear equations and then prints the solution, if any."""

  a = int(input(""))
  b = int(input(""))
  c = int(input(""))
  d = int(input(""))
  e = int(input(""))
  f = int(input(""))

  solution = brute_force_solution(a, b, c, d, e, f)
  if solution is None:
    print("No solution")
  else:
    print(solution)


if __name__ == "__main__":
  main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
