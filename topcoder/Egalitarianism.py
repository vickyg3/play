import sys
INT_MAX = sys.maxint

class Egalitarianism:
    def maxDifference(self, isFriend, d):
        graph = []
        for person in isFriend:
            graph.append([i for i, x in enumerate(person) if x == 'Y'])
        max_shortest = -1
        n = len(isFriend)
        # for each node, find shortest path to all other nodes
        for i in range(n):
            shortest = [INT_MAX] * n
            visited = [False] * n
            # perform bfs starting from i
            queue = [(i, 0)]
            while queue:
                item, distance = queue.pop(0)
                visited[item] = True
                shortest[item] = distance
                for neigbor in graph[item]:
                    if not visited[neigbor] and neigbor not in [x[0] for x in queue]:
                        queue.append((neigbor, distance + 1))
            if False in visited: # disconnected graph
                return -1
            shortest.append(max_shortest)
            max_shortest = max(shortest)
        return max_shortest * d

if __name__ == "__main__":
    print Egalitarianism().maxDifference(["NYN", "YNY", "NYN"], 10)
    print Egalitarianism().maxDifference(["NN", "NN"], 1)
    print Egalitarianism().maxDifference(["NNYNNN", "NNYNNN", "YYNYNN", "NNYNYY", "NNNYNN", "NNNYNN"], 1000)
    print Egalitarianism().maxDifference(["NNYN", "NNNY", "YNNN", "NYNN"], 584)
    print Egalitarianism().maxDifference(["NYNYYYN", "YNNYYYN", "NNNNYNN", "YYNNYYN", "YYYYNNN", "YYNYNNY", "NNNNNYN"], 5)
    print Egalitarianism().maxDifference(["NYYNNNNYYYYNNNN", "YNNNYNNNNNNYYNN", "YNNYNYNNNNYNNNN", "NNYNNYNNNNNNNNN", "NYNNNNYNNYNNNNN", "NNYYNNYNNYNNNYN", "NNNNYYNNYNNNNNN", "YNNNNNNNNNYNNNN", "YNNNNNYNNNNNYNN", "YNNNYYNNNNNNNNY", "YNYNNNNYNNNNNNN", "NYNNNNNNNNNNNNY", "NYNNNNNNYNNNNYN", "NNNNNYNNNNNNYNN", "NNNNNNNNNYNYNNN"], 747)
    print Egalitarianism().maxDifference(["NY", "YN"], 0)