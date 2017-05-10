import sys
INT_MAX = 999999999999999999

class EmoticonsDiv2:
  def _printSmiles(self, smiles, k, clipboard):
    key = (k, clipboard)
    if not self.memo.has_key(key):
      try:
        if k == smiles:
          self.memo[key] = 1
        elif k > smiles:
          self.memo[key] = INT_MAX
        else:
          copyCount = self._printSmiles(smiles, k, k) if k != clipboard else INT_MAX
          pasteCount = self._printSmiles(smiles, k + clipboard, clipboard)
          self.memo[key] = min(copyCount, pasteCount) + 1
      except:
        sys.setrecursionlimit(self.limit)
        sys.exit(-1)
    return self.memo[key]

  def printSmiles(self, smiles):
    self.limit = sys.getrecursionlimit()
    sys.setrecursionlimit(10000);
    self.memo = {}
    retval = self._printSmiles(smiles, 1, 1)
    sys.setrecursionlimit(self.limit)
    return retval

if __name__ == "__main__":
  print EmoticonsDiv2().printSmiles(2)
  print EmoticonsDiv2().printSmiles(6)
  print EmoticonsDiv2().printSmiles(11)
  print EmoticonsDiv2().printSmiles(16)
  print EmoticonsDiv2().printSmiles(1000)