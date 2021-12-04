class Board:
    def __init__(self, grid):
        self.grid = grid
        self.size = len(grid)
        self.marked = []
        self.completed = False

    def isCompleted(self):
        xCount = [0] * self.size
        yCount = [0] * self.size
        xyCount = 0
        yxCount = 0

        for x in range(self.size):
            for y in range(self.size):
                if self.grid[x][y] in self.marked:
                    xCount[x] += 1
                    yCount[y] += 1

                    if (y == x):
                        xyCount += 1
                    
                    if (x + y == self.size - 1):
                        yxCount
        
        return xyCount == self.size or yxCount == self.size or self.size in xCount or self.size in yCount

    def draw(self, num):
        if not num in self.marked:
            self.marked.append(num)

        return self.isCompleted()

    def getVal(self):
        result = 0

        for row in self.grid:
            for val in row:
                if not val in self.marked:
                    result += int(val)
        
        return result


def main():
    file = open("input.txt")

    lines = file.readlines()
    
    draws = lines.pop(0).strip().split(',')

    lines.pop(0)

    result = 0

    boards = []

    currentInfo = []
    for line in lines:
        line = line.strip()

        if line == '':
            boards.append(Board(currentInfo))
            currentInfo = []
            continue
            
        row = line.split(' ')

        while '' in row:
            row.remove('')

        currentInfo.append(row)

    loser = None
    winningDraw = None

    for draw in draws:
        for board in boards.copy():
            
            if board.draw(draw) and len(boards) != 1:
                boards.remove(board)
        
        if len(boards) == 1 and boards[0].isCompleted():
            loser = boards[0]
            winningDraw = draw
            break

    result = int(winningDraw) * int(loser.getVal())
    

    out = open("output-part2.txt", "w")
    out.write(str(result))
    file.close()
    out.close()


if (__name__ == "__main__"):
    main()
