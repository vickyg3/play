import sys
INT_MAX = sys.maxint

class RGBStreet:
  def _rgb(self, houses, i, r_allowed, g_allowed, b_allowed):
    if not self.memo.has_key((i, r_allowed, g_allowed, b_allowed)):
      if i == len(houses):
        return 0
      r, g, b = map(int, houses[i].split(" "))
      r_cost = (r + self._rgb(houses, i + 1, False, True, True)) if r_allowed else INT_MAX
      g_cost = (g + self._rgb(houses, i + 1, True, False, True)) if g_allowed else INT_MAX
      b_cost = (b + self._rgb(houses, i + 1, True, True, False)) if b_allowed else INT_MAX
      self.memo[(i, r_allowed, g_allowed, b_allowed)] = min(r_cost, g_cost, b_cost)
    return self.memo[(i, r_allowed, g_allowed, b_allowed)]

  def estimateCost(self, houses):
    self.memo = {}
    return self._rgb(houses, 0, True, True, True)

if __name__ == "__main__":
  print RGBStreet().estimateCost(["1 100 100", "100 1 100", "100 100 1"])
  print RGBStreet().estimateCost(["1 100 100", "100 100 100", "1 100 100"])
  print RGBStreet().estimateCost(["26 40 83", "49 60 57", "13 89 99"])
  print RGBStreet().estimateCost(["30 19 5", "64 77 64", "15 19 97", "4 71 57", "90 86 84", "93 32 91"])
  print RGBStreet().estimateCost(["71 39 44", "32 83 55", "51 37 63", "89 29 100", "83 58 11", "65 13 15", "47 25 29", "60 66 19"])