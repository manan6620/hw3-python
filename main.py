# Author: Manan Patel mxp5787@psu.edu
def run():
  number=int(input("Enter an int: "))
  s = digit_sum(number)
  print(f"sum of digits of {number} is {s}.")


def digit_sum(number):
  if (number<10):
    return number
  else:
    return number%10 + digit_sum(number//10)


if __name__ == "__main__":
  run()