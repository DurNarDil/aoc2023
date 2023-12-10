class Card:
    def __init__(self, wholeLine) -> None:
        self.line = wholeLine
        self.winningLine = self.splitLine(wholeLine)[0]
        self.numbersLine = self.splitLine(wholeLine)[1]
        self.winningNumbers = self.splitNumbers(self.winningLine)
        self.cardNumbers = self.splitNumbers(self.numbersLine)
        self.winners = self.countWinners()
        self.points = self.calcPoints()

    def splitLine(self, wholeLine) -> list[str]:
        wholeLine = wholeLine[8:]
        return wholeLine.split('|')
    
    def splitNumbers(self, line) -> list[str]:
        return line.split()
    
    def countWinners(self) -> int:
        count = 0
        for number in self.winningNumbers:
            if number in self.cardNumbers:
                count += 1
        return count
    
    def calcPoints(self) -> int:
        if self.winners == 0:
            return 0
        return 2 ** (self.winners -1)

input='''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

