from copy import deepcopy 

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Map:
    def __init__(self):
        self.map=[[2**32],[2**32]]

    def addLine(self, line):
        self.map.insert(-1, [2**32])
        for v in line:
            self.map[len(self.map)-2].append(int(v))
        self.map[len(self.map)-2].append(2**32)



    def resize(self, n):
        self.map[0]=[2**32 for i in range(n+2)]
        self.map[-1]=[2**32 for i in range(n+2)]
        for i in range(len(self.map)):
            if len(self.map[i])!=(n+2):
                raise Exception("Wrong dimension", i)     

    def findLowPoints(self):
        ret=list()
        for x in range(1, len(self.map)-1):
            for y in range(1, len(self.map[x])-1):
                try:
                    if (self.map[x][y]<self.map[x+1][y] and
                            self.map[x][y]<self.map[x][y-1] and
                            self.map[x][y]<self.map[x][y+1] and
                            self.map[x][y]<self.map[x-1][y]):
                        ret.append({"V": self.map[x][y], "C": (x, y)})
                except Exception as E:
                    print(E, x, y)
        return ret

    def _notExplored(self, lst):
        for x in range(len(lst)):
            if lst[x]!=4:
                return x
        return -1

    def findBasins(self):
        newM=deepcopy(self.map)
        basins=list()
        for low in self.findLowPoints():
            basin=[(low["V"], low["C"])]
            explored=[0]
            while (pos:=self._notExplored(explored)) != -1:
                #print(pos, basin)
                check=None
                x=basin[pos][1][0]
                y=basin[pos][1][1]
                newM[x][y]=9
                if explored[pos]==0: #Go left
                    y-=1
                    while newM[x][y]!=9 and newM[x][y]!=2**32:
                        basin.append((newM[x][y], (x, y)))
                        newM[x][y]=9
                        explored.append(0)
                        if len(explored)!=len(basin):
                            raise Exception("Different lengths between explored and basin", len(explored), len(basin))
                        y-=1
                elif explored[pos]==1: #Go up
                    x-=1
                    while newM[x][y]!=9 and newM[x][y]!=2**32:
                        basin.append((newM[x][y], (x, y)))
                        newM[x][y]=9
                        explored.append(0)
                        if len(explored)!=len(basin):
                            raise Exception("Different lengths between explored and basin", len(explored), len(basin))
                        x-=1
                    
                elif explored[pos]==2: #Go right
                    y+=1
                    while newM[x][y]!=9 and newM[x][y]!=2**32:
                        basin.append((newM[x][y], (x, y)))
                        newM[x][y]=9
                        explored.append(0)
                        if len(explored)!=len(basin):
                            raise Exception("Different lengths between explored and basin", len(explored), len(basin))
                        y+=1

                elif explored[pos]==3:
                    x+=1
                    while newM[x][y]!=9 and newM[x][y]!=2**32:
                        basin.append((newM[x][y], (x, y)))
                        newM[x][y]=9
                        explored.append(0)
                        if len(explored)!=len(basin):
                            raise Exception("Different lengths between explored and basin", len(explored), len(basin))
                        x+=1
                explored[pos]+=1
            
            basins.append(basin)
        biggest=list()
        ret=list()
        for basin in basins:
            for point in basin:
                ret.append(point[1])
            biggest.append((len(basin), basins.index(basin)))
        biggest.sort(key=lambda big: big[0])
    
        print("bigest: ", biggest[-1], biggest[-2], biggest[-3], (biggest[-1][0]*biggest[-2][0]*biggest[-3][0]))

        return ret


    def __str__(self, b=False):
        ret=""
        if not b:
            for line in self.map:
                for v in line:
                    if v!=2**32:
                        ret+=str(v)
                ret+="\n"
            ret+="\n"
        
        if b:
            points=self.findBasins()
            for x in range(1, len(self.map)-1):
                for y in range(1, len(self.map[x])-1):
                    if (x,y) in points:
                        ret+=(color.RED+str(self.map[x][y])+color.END)
                    else:
                        ret+=str(self.map[x][y])
                ret+="\n"
            ret+="\n"

        return ret


def main():
    M=Map()
    with open("input.txt", "r") as f:
        for line in f:
            M.resize(len(line.split("\n")[0]))
            M.addLine(line.split("\n")[0])

    print(M)
    fin=0
    for d in M.findLowPoints():
        fin+=(d["V"]+1)
    print(fin)

    print(M.__str__(True))



if __name__=="__main__":
    main()
