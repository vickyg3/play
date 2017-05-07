class KLastNonZeroDigits:
  def getKDigits(self, N, K):
    fact = 1
    for i in range(2, N + 1):
      fact *= i
    while fact / 10 == fact / 10.0:
      fact /= 10
    return str(fact)[-K:]

  def getKDigits2(self, N, K):
    fives = N / 5
    # TODO: for N >= 25 count all multiples of 25, and so on for 125.
    twos = fives
    fact = 1
    for i in range(2, N + 1):
      if i % 2 == 0 and twos > 0:
        i /= 2
        twos -= 1
      if i % 5 == 0 and fives > 0:
        i /= 5
        fives -= 1
      fact *= i
      fact %= 10 ** K
    return fact

if __name__ == "__main__":
  print KLastNonZeroDigits().getKDigits2(10, 3)
  print KLastNonZeroDigits().getKDigits(10, 3)
  print KLastNonZeroDigits().getKDigits2(6, 1)
  print KLastNonZeroDigits().getKDigits(6, 1)
  print KLastNonZeroDigits().getKDigits2(6, 3)
  print KLastNonZeroDigits().getKDigits(6, 3)
  print KLastNonZeroDigits().getKDigits2(7, 2)
  print KLastNonZeroDigits().getKDigits(7, 2)
  print KLastNonZeroDigits().getKDigits2(20, 9)
  print KLastNonZeroDigits().getKDigits(20, 9)
  print KLastNonZeroDigits().getKDigits2(1, 1)
  print KLastNonZeroDigits().getKDigits(1, 1)