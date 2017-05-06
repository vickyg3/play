class ErdosNumber:
  def calculateNumbers(self, publications):
    graph = {}
    for publication in publications:
      authors = publication.split(' ')
      for author in authors:
        if author not in graph:
          graph[author] = []
        graph[author].extend([co_author for co_author in authors if author != co_author])
    visited = {}
    for author in graph:
      graph[author] = list(set(graph[author]))
      visited[author] = False
    output = []
    queue = [("ERDOS", 0)]
    while queue:
      author, number = queue.pop(0)
      visited[author] = True
      output.append("%(author)s %(number)d" % locals())
      for co_author in graph[author]:
        if not visited[co_author] and co_author not in [x[0] for x in queue]:
          queue.append((co_author, number + 1))
    for author in visited:
      if not visited[author]:
        output.append(author)
    output.sort()
    return output

if __name__ == "__main__":
  print ErdosNumber().calculateNumbers(["ERDOS"])
  print ErdosNumber().calculateNumbers(["KLEITMAN LANDER", "ERDOS KLEITMAN"])
  print ErdosNumber().calculateNumbers(["ERDOS A", "A B", "B AA C"])
  print ErdosNumber().calculateNumbers(["ERDOS B", "A B C", "B A E", "D F"])
  print ErdosNumber().calculateNumbers(["ERDOS KLEITMAN", "CHUNG GODDARD KLEITMAN WAYNE", "WAYNE GODDARD KLEITMAN", "ALON KLEITMAN", "DEAN GODDARD WAYNE KLEITMAN STURTEVANT"])