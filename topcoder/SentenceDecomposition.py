INT_MAX = 999999999

class SentenceDecomposition:
	def _cost(self, a, b):
		return sum([1 if a[i] != b[i] else 0 for i in range(len(a))])

	def _is_word(self, a, b):
		return sorted(a) == sorted(b)

	def _decompose_helper(self, sentence, validWords, k):
		if self.memo[k] == -1:
			if k == len(sentence):
				return 0
			min_cost = INT_MAX
			for word in validWords:
				potential_word = sentence[k:k + len(word)]
				if (self._is_word(word, potential_word)):
					cost = self._cost(word, potential_word) + self._decompose_helper(sentence, validWords, k + len(word))
					if cost < min_cost:
						min_cost = cost
			self.memo[k] = min_cost
		return self.memo[k]

	def decompose(self, sentence, validWords):
		self.memo = [-1] * (len(sentence) + 1)
		cost = self._decompose_helper(sentence, validWords, 0)
		return cost if cost < INT_MAX else -1

if __name__ == "__main__":
	print SentenceDecomposition().decompose("neotowheret", ["one", "two", "three", "there"])
	print SentenceDecomposition().decompose("abba", ["ab", "ac", "ad"])
	print SentenceDecomposition().decompose("thisismeaningless", ["this", "is", "meaningful"])
	print SentenceDecomposition().decompose("ommwreehisymkiml", ["we", "were", "here", "my", "is", "mom", "here", "si", "milk", "where", "si"])
	print SentenceDecomposition().decompose("ogodtsneeencs", ["go", "good", "do", "sentences", "tense", "scen"])
	print SentenceDecomposition().decompose("sepawaterords", ["separate","words"])