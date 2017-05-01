class LuckyCycle:
  def _is_lucky(self, graph, path):
    #print 'path', path
    if len(path) < 3 or len(path) % 2 == 0:
      return False
    fours = 0
    sevens = 0
    for i in range(1, len(path)):
      #print 'i: %d value: %d' % (i, graph[path[i-1]][path[i]])
      if graph[path[i - 1]][path[i]] == 4:
        fours += 1
      else:
        sevens += 1
    #print 'fours: %(fours)d sevens: %(sevens)d' % locals()
    return fours == sevens

  def _cycle(self, graph, k):
    visited = [False] * (len(graph) + 1)
    queue = [(k, [])]
    #print 'k', k
    while queue:
      item, path = queue.pop(0)
      visited[item] = True
      path.append(item)
      if not graph[k][item]:
        graph[k][item] = 4
        graph[item][k] = 4
        #print 'trying 4'
        if self._is_lucky(graph, path + [k]):
          return (path[0], path[-1], 4)
        graph[k][item] = 7
        graph[item][k] = 7
        #print 'trying 7'
        if self._is_lucky(graph, path + [k]):
          return (path[0], path[-1], 7)
        graph[item][path[-1]] = 0
      # continue with traversal
      neigbors = [i for i, e in enumerate(graph[item]) if e != 0]
      for neighbor in neigbors:
        if not visited[neighbor] and neighbor not in [x[0] for x in queue]:
          queue.append((neighbor, path[:]))
      #print queue
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
  #print LuckyCycle().getEdge()
  #print LuckyCycle().getEdge()