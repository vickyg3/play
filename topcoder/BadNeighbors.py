class BadNeighbors:
    def maxDonationsHelper(self, donations, i, first_included):
        if not self.memo.has_key((i, first_included)):
            if i == len(donations):
                return 0
            if i == len(donations) - 1:
                return  donations[i] if not first_included else 0
            # include current donation
            v1_first_included = first_included
            if i == 0:
                v1_first_included = True
            v1 = donations[i] + self.maxDonationsHelper(donations, i + 2, v1_first_included)
            # exclude current donation
            v2 = self.maxDonationsHelper(donations, i + 1, first_included)
            self.memo[(i, first_included)] = max((v1, v2))
        return self.memo[(i, first_included)]

    def maxDonations(self, donations):
        self.memo = {}
        self.orig_len = len(donations)
        return self.maxDonationsHelper(donations, 0, False)

if __name__ == "__main__":
    print BadNeighbors().maxDonations([10, 3, 2, 5, 7, 8])
    print BadNeighbors().maxDonations([11, 15])
    print BadNeighbors().maxDonations([7, 7, 7, 7, 7, 7, 7])
    print BadNeighbors().maxDonations([1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ])
    print BadNeighbors().maxDonations([94, 40, 49, 65, 21, 21, 106, 80, 92, 81,
        679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72,
        37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72])
