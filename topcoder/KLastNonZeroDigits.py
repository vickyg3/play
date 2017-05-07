class KLastNonZeroDigits:
  def getKDigits(self, N, K):
    fact = 1
    for i in range(2, N + 1):
      fact *= i
    while fact / 10 == fact / 10.0:
      fact /= 10
    return str(fact)[-K:]

if __name__ == "__main__":
  print KLastNonZeroDigits().getKDigits(10, 3)
  print KLastNonZeroDigits().getKDigits(6, 1)
  print KLastNonZeroDigits().getKDigits(6, 3)
  print KLastNonZeroDigits().getKDigits(7, 2)
  print KLastNonZeroDigits().getKDigits(20, 9)
  print KLastNonZeroDigits().getKDigits(1, 1)