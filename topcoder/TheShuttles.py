import math
import sys

class TheShuttles:
  def _cost(self, baseCost, seatCost, n):
    return baseCost + seatCost * n

  def getLeastCost(self, cnt, baseCost, seatCost):
    cnt = sorted(cnt)
    min_cost = sys.maxint
    for num_seats in range(1, cnt[-1] + 1):
      cost = 0
      for c in cnt:
        cost += self._cost(baseCost, seatCost, num_seats) * int(math.ceil(float(c)/num_seats))
      if cost < min_cost:
        min_cost = cost
    return min_cost

if __name__ == "__main__":
  print TheShuttles().getLeastCost([9], 30, 5)
  print TheShuttles().getLeastCost([9, 4], 30, 5)
  print TheShuttles().getLeastCost([9, 4], 10, 5)
  print TheShuttles().getLeastCost([51, 1, 77, 14, 17, 10, 80], 32, 40)
  print TheShuttles().getLeastCost([5, 6], 1, 100)
