class BuyingCheap:
  def thirdBestPrice(self, prices):
    s = sorted(set(prices))
    return s[2] if len(s) >= 3 else -1

if __name__ == "__main__":
  print BuyingCheap().thirdBestPrice([10, 40, 50, 20, 70, 80, 30, 90, 60])
  print BuyingCheap().thirdBestPrice([10, 10, 10, 10, 20, 20, 30, 30, 40, 40])
  print BuyingCheap().thirdBestPrice([80, 90, 80, 90, 80])
  print BuyingCheap().thirdBestPrice([10])