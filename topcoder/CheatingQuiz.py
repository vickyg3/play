from collections import defaultdict

class CheatingQuiz:
  def howMany(self, answers):
    counts = defaultdict(int)
    for answer in answers:
      counts[answer] += 1
    result = []
    for answer in answers:
      result.append(len(counts))
      if counts[answer] == 1:
        del counts[answer]
      else:
        counts[answer] -= 1
    return result

if __name__ == "__main__":
  print CheatingQuiz().howMany("AAAAA")
  print CheatingQuiz().howMany("AAABBB")
  print CheatingQuiz().howMany("CAAAAAC")
  print CheatingQuiz().howMany("BBCA")
  print CheatingQuiz().howMany("BACACABCBBBBCAAAAACCCABBCAA")