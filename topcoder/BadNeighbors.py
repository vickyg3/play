class BadNeighbors:
    def maxDonationsHelper(self, donations, first_included):
        if not self.memo.has_key((tuple(donations), first_included)):
            if len(donations) == 0:
                return 0
            if len(donations) == 1:
                return  donations[0] if not first_included else 0
            # include current donation
            v1_first_included = first_included
            if len(donations) == self.orig_len:
                v1_first_included = True
            v1 = donations[0] + self.maxDonationsHelper(donations[2:], v1_first_included)
            # exclude current donation
            v2 = self.maxDonationsHelper(donations[1:], first_included)
            self.memo[(tuple(donations), first_included)] = max((v1, v2))
        return self.memo[(tuple(donations), first_included)]

    def maxDonations(self, donations):
        self.memo = {}
        self.orig_len = len(donations)
        return self.maxDonationsHelper(donations, False)

if __name__ == "__main__":
    print BadNeighbors().maxDonations([10, 3, 2, 5, 7, 8])
    print BadNeighbors().maxDonations([11, 15])
    print BadNeighbors().maxDonations([7, 7, 7, 7, 7, 7, 7])
    print BadNeighbors().maxDonations([1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ])
    print BadNeighbors().maxDonations([94, 40, 49, 65, 21, 21, 106, 80, 92, 81,
        679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72,
        37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72])
