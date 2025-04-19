import numpy as np
import math

def main():
  x_values = np.linspace(0, 2, 1000)

  print("x\t\tsin(x)")
  print("-" * 25)

  for x in x_values:
    print(f"{x:.5f}\t{math.sin(x):.5f}")

main()
