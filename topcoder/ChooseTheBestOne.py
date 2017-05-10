class ChooseTheBestOne:
  def countNumber(self, N):
    people = [i + 1 for i in range(N)]
    turn = 1
    offset = 0
    while len(people) > 1:
      turn_count = turn ** 3
      people_left = len(people)
      person_eliminated = people[(offset + turn_count - 1) % len(people)]
      offset = people.index(person_eliminated)
      del people[offset]
      offset %= len(people)
      turn += 1
    return people[0]

if __name__ == "__main__":
  print ChooseTheBestOne().countNumber(3)
  print ChooseTheBestOne().countNumber(6)
  print ChooseTheBestOne().countNumber(10)
  print ChooseTheBestOne().countNumber(1234)