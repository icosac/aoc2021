class Map:
    def __init__(self):
        self.map=list()

    def addLine(self, line):
        self.map.append(list())
        for v in line:
            self.map[-1].append(int(v))

    def findLowPoints(self):
        ret=list()
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if x==0:
                    if y==0:
                        if (self.map[x][y]<self.map[x+1][y] and
                                self.map[x][y]<self.map[x][y+1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                    elif y==len(self.map[x])-1:
                        if (self.map[x][y]<self.map[x+1][y] and
                                self.map[x][y]<self.map[x][y-1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                    else:
                        if (self.map[x][y]<self.map[x+1][y] and
                                self.map[x][y]<self.map[x][y-1] and
                                self.map[x][y]<self.map[x][y+1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                elif x==len(self.map)-1:
                    if y==0:
                        if (self.map[x][y]<self.map[x-1][y] and
                                self.map[x][y]<self.map[x][y+1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                    elif y==len(self.map[x])-1:
                        if (self.map[x][y]<self.map[x-1][y] and
                                self.map[x][y]<self.map[x][y-1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                    else:
                        if (self.map[x][y]<self.map[x-1][y] and
                                self.map[x][y]<self.map[x][y-1] and
                                self.map[x][y]<self.map[x][y+1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                else:
                    if y==0:
                        if (self.map[x][y]<self.map[x+1][y] and
                                self.map[x][y]<self.map[x][y+1] and
                                self.map[x][y]<self.map[x-1][y]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                    elif y==len(self.map[x])-1:
                        if (self.map[x][y]<self.map[x-1][y] and
                                self.map[x][y]<self.map[x+1][y] and
                                self.map[x][y]<self.map[x][y-1]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
                    else: 
                        if (self.map[x][y]<self.map[x+1][y] and
                                self.map[x][y]<self.map[x][y-1] and
                                self.map[x][y]<self.map[x][y+1] and
                                self.map[x][y]<self.map[x-1][y]):
                            ret.append({"V": self.map[x][y], "C": (x, y)})
        return ret


    def __str__(self):
        ret=""
        for line in self.map:
            for v in line:
                ret+=str(v)
            ret+="\n"
        return ret


def main():
    M=Map()
    with open("input.txt", "r") as f:
        for line in f:
            M.addLine(line.split("\n")[0])

    print(M)
    fin=0
    for d in M.findLowPoints():
        print(d)
        fin+=(d["V"]+1)
    print(fin)





if __name__=="__main__":
    main()
