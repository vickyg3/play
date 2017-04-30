wclass SRMCards:
    def maxTurns(self, cards):
        cards = list(cards)
        cards.sort()
        i = 0
        cnt = 0
        while i < len(cards):
            if i + 1 < len(cards) and cards[i] + 1 == cards[i + 1]:
                i += 1
            cnt += 1
            i += 1
        return cnt

if __name__ == "__main__":
    print SRMCards().maxTurns([498, 499])
    print SRMCards().maxTurns([491, 492, 495, 497, 498, 499])
    print SRMCards().maxTurns([100, 200, 300, 400])
    print SRMCards().maxTurns([11, 12, 102, 13, 100, 101, 99, 9, 8, 1])
    print SRMCards().maxTurns([118, 321, 322, 119, 120, 320])
    print SRMCards().maxTurns([10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9])