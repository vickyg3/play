class BinaryCardinality:
    def _cardinality(self, n):
        ones = 0
        while n:
            if n & 1:
                ones += 1
            n >>= 1
        return ones

    def _sort(self, a, b):
        if self._cardinality(a) == self._cardinality(b):
            return -1 if a < b else 1
        return -1 if self._cardinality(a) < self._cardinality(b) else 1

    def arrange(self, numbers):
        return sorted(numbers, cmp=self._sort)

if __name__ == "__main__":
    print BinaryCardinality().arrange([4])
    print BinaryCardinality().arrange([31,15,7,3,2])
    print BinaryCardinality().arrange([10,9,8,7,6,5,4,3,2,1])
    print BinaryCardinality().arrange([811385,340578,980086,545001,774872,855585,13848,863414,419523,190151,784903,127461])