import sys

R = 0
G = 1
B = 2
mapping = {0: 'R', 1: 'G', 2: 'B'}
INT_MAX = sys.maxint

class ColorfulRoad:
  def _cost(self, i, j):
    return (j - i) * (j - i);

  def _min(self, road, i, target):
    if not self.memo.has_key(i):
      if i == len(road) - 1:
        return 0
      costs = []
      for j in range(i + 1, len(road)):
        if road[j] == mapping[target]:
          possible_cost = self._min(road, j, (target + 1) % 3)
          if possible_cost != -1:
            costs.append(self._cost(i, j) + possible_cost)
      self.memo[i] = min(costs) if costs else -1
    return self.memo[i]

  def getMin(self, road):
    self.memo = {}
    return self._min(road, 0, G)

if __name__ == "__main__":
  print ColorfulRoad().getMin("RGGGB")
  print ColorfulRoad().getMin("RGBRGBRGB")
  print ColorfulRoad().getMin("RBBGGGRR")
  print ColorfulRoad().getMin("RBRRBGGGBBBBR")
  print ColorfulRoad().getMin("RBRGBGBGGBGRGGG")