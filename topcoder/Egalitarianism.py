INT_MAX = 999999999999

class Egalitarianism:
	def maxDifference(self, isFriend, d):
		graph = []
		for person in isFriend:
			graph.append([1 if x == 'Y' else INT_MAX for x in person])
		n = len(isFriend)
		for i in range(n):
			for j in range(n):
				for k in range(n):
					graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
		max_depth = 0
		for i in range(n):
			for j in range(i):
				if graph[i][j] >= INT_MAX: # disconnected graph
					return -1
				max_depth = max(max_depth, graph[i][j])
		return max_depth * d

if __name__ == "__main__":
	print Egalitarianism().maxDifference(["NYN", "YNY", "NYN"], 10)
	print Egalitarianism().maxDifference(["NN", "NN"], 1)
	print Egalitarianism().maxDifference(["NNYNNN", "NNYNNN", "YYNYNN", "NNYNYY", "NNNYNN", "NNNYNN"], 1000)
	print Egalitarianism().maxDifference(["NNYN", "NNNY", "YNNN", "NYNN"], 584)
	print Egalitarianism().maxDifference(["NYNYYYN", "YNNYYYN", "NNNNYNN", "YYNNYYN", "YYYYNNN", "YYNYNNY", "NNNNNYN"], 5)
	print Egalitarianism().maxDifference(["NYYNNNNYYYYNNNN", "YNNNYNNNNNNYYNN", "YNNYNYNNNNYNNNN", "NNYNNYNNNNNNNNN", "NYNNNNYNNYNNNNN", "NNYYNNYNNYNNNYN", "NNNNYYNNYNNNNNN", "YNNNNNNNNNYNNNN", "YNNNNNYNNNNNYNN", "YNNNYYNNNNNNNNY", "YNYNNNNYNNNNNNN", "NYNNNNNNNNNNNNY", "NYNNNNNNYNNNNYN", "NNNNNYNNNNNNYNN", "NNNNNNNNNYNYNNN"], 747)
	print Egalitarianism().maxDifference(["NY", "YN"], 0)