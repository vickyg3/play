class AdditionCycles:
    def _get_sum(self, n):
        return sum(map(int, str(n)))

    def _last_digit(self, n):
        return str(n % 10)

    def cycleLength(self, n):
        orig_n = n
        count = 0
        while True:
            count += 1
            n_sum = self._get_sum(n)
            new_n = self._last_digit(n) + self._last_digit(n_sum)
            if int(new_n) == orig_n:
                break
            n = int(new_n)
        return count

if __name__ == "__main__":
    print AdditionCycles().cycleLength(26)
    print AdditionCycles().cycleLength(55)
    print AdditionCycles().cycleLength(0)
    print AdditionCycles().cycleLength(71)
