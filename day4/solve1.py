xDim=5
yDim=5

class Board:
    def __init__(self, lsts):
        if len(lsts)==xDim:
            for lst in lsts:
                if len(lst)!=yDim:
                    raise NameError("Wrong y dimension", lst)
        else:
            raise NameError("Wrong x dimension", len(lsts))

        self.lsts=lsts
        self.board=self.lsts

    def checkBoard(self, value=False):
        retX=True
        retY=True

        for x in range(xDim):
            retx=True
            for y in range(yDim):
                if self.board[x][y]!=-1:
                    retX=False
                    break
            if retX:
                break

        for y in range(yDim):
            retY=True
            for x in range(xDim):
                if self.board[x][y]!=-1:
                    retY=False
                    break
            if retY:
                break

        return (retX | retY)

    def __str__(self):
        for x in range(xDim):
            for y in range(yDim):
                print(self.board[x][y], end="\t")
            print()


    def drawNumber(self, num):
        for x in range(xDim):
            for y in range(yDim):
                if self.board[x][y]==num:
                    self.board[x][y]=-1
                    if self.checkBoard(True):
                        return (True)
        return (False)
     
    def computeSum(self):
        sum=0
        for x in range(xDim):
            for y in range(yDim):
                if self.board[x][y]!=-1:
                    sum+=self.board[x][y]
        return sum

def main():
    boards=list()
    values=list()
    with open("input.txt", "r") as f:
        for line in f:
            if len(values)==0:
                values=[int(value) for value in line.split("\n")[0].split(",")]
            else:
                if line=="\n":
                    pass
                else:
                    boards.append([int(value) for value in line.split("\n")[0].split(" ") if value])

    new_boards=list()
    n=0
    board=list()
    for lst in boards:
        board.append(lst)
        if n%xDim==(xDim-1):
            new_boards.append(Board([x for x in board]))
            board.clear()
        n+=1
    
    boards=new_boards
    
    pos=-1
    num=-1
    for value in values:
        for board in boards:
            b=board.drawNumber(value)
            if b:
                pos=boards.index(board)
                num=value
                break
        if pos!=-1 and num!=-1:
            break
        
    print(pos, num, boards[pos].computeSum(), (boards[pos].computeSum()*num))
    print(boards[pos].board)


if __name__ == "__main__":
    main()
