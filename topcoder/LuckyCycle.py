class LuckyCycle:
  def _is_lucky(self, fours, sevens):
    if fours < 2 and sevens < 2:
      return 0
    if fours + 1 == sevens:
      return 4
    if sevens + 1 == fours:
      return 7
    return 0

  def _cycle(self, graph, k):
    visited = [False] * (len(graph) + 1)
    queue = [(k, None, 0, 0)]
    while queue:
      item, last_node, fours, sevens = queue.pop(0)
      visited[item] = True
      if last_node:
        current_weight = graph[last_node][item]
        if current_weight == 4:
          fours += 1
        else:
          sevens += 1
      new_weight = self._is_lucky(fours, sevens)
      if new_weight:
        return (k, item, new_weight)
      # continue the traversal
      neigbors = [i for i, e in enumerate(graph[item]) if e != 0]
      for neighbor in neigbors:
        if not visited[neighbor] and neighbor not in [x[0] for x in queue]:
          queue.append((neighbor, item, fours, sevens))
    return None

  def getEdge(self, edge1, edge2, weight):
    graph = [[0] * (len(edge1) + 2) for i in range(len(edge2) + 2)]
    for i in range(len(edge1)):
      graph[edge1[i]][edge2[i]] = weight[i]
      graph[edge2[i]][edge1[i]] = weight[i]
    for k in range(1, len(edge1) + 2):
      retval = self._cycle(graph, k)
      if retval:
        return retval
    return ()

if __name__ == "__main__":
  print LuckyCycle().getEdge([1], [2], [4])
  print LuckyCycle().getEdge([1, 3, 2, 4], [2, 2, 4, 5], [4, 7, 4, 7])
  print LuckyCycle().getEdge([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [4, 4, 4, 4, 4, 4, 7, 7, 7, 7, 7, 7])
  print LuckyCycle().getEdge([1, 2, 3, 5, 6], [2, 3, 4, 3, 5], [4, 7, 7, 7, 7])