class Map:
    def __init__(self):
        self.map=[[0]]
        self.maxX=0
        self.maxY=0

    def add_line(self, x1, y1, x2, y2, diagonal=False):
        self.maxX=x1+1 if self.maxX<x1+1 else self.maxX
        self.maxX=x2+1 if self.maxX<x2+1 else self.maxX
        self.maxY=y1+1 if self.maxY<y1+1 else self.maxY
        self.maxY=y2+1 if self.maxY<y2+1 else self.maxY

        self.enlarge()

        if not(diagonal):
            Ax=min(x1, x2)
            Bx=max(x1, x2)
            Ay=min(y1, y2)
            By=max(y1, y2)
            for x in range(Ax, Bx+1):
                for y in range(Ay, By+1):
                    #print(x,y)
                    try:
                        self.map[x][y]+=1
                    except Exception as e:
                        print(e, x, y, 
                              "\nFrom: (", x1, y1, ") to: (", x2, y2, ")", 
                              "\nmax: (", self.maxX, self.maxY, ")", 
                              "\nlen: (", len(self.map), len(self.map[0]), ")",
                              "\nDiagonal: ", diagonal
                              )
        else:
            if x1>x2:
                Ax=x2
                Ay=y2
                Bx=x1
                By=y1
            else:
                Ax=x1
                Ay=y1
                Bx=x2
                By=y2
            y=Ay
            for x in range(Ax, Bx+1):
                try:
                    self.map[x][y]+=1
                except Exception as e:
                    print(e, x, y, 
                          "\nFrom: (", x1, y1, ") to: (", x2, y2, ")", 
                          "\nmax: (", self.maxX, self.maxY, ")", 
                          "\nlen: (", len(self.map), len(self.map[0]), ")",
                          "\nDiagonal: ", diagonal
                          )
                y=y+1 if By>Ay else y-1


    def enlarge(self):
        if len(self.map)!=self.maxX:
            for i in range(self.maxX-len(self.map)):
                self.map.append(list())
                for j in range(self.maxY):
                    self.map[-1].append(0)

        for x in self.map:
            for i in range(self.maxY-len(x)):
                x.append(0)

    def __str__(self):
        ret=""
        for y in range(self.maxY):
            for x in range(self.maxX):
                if self.map[x][y]==0:
                    ret+="."
                else:
                    ret+=str(self.map[x][y])
            ret+="\n"
        return ret
    
    def final_value(self):
        ret=0
        for x in self.map:
            for y in x:
                if y>1:
                    ret+=1
        return ret


minCoord=[1**32,2**32]
maxCoord=[0,0]
lines=list()
def main():
    M=Map()
    with open("input.txt", "r") as f:
        for values in f:
            initialPoint=values.split(" -> ")[0]
            finalPoint=values.split(" -> ")[1]
            x1=int(initialPoint.split(',')[0])
            y1=int(initialPoint.split(',')[1])
            x2=int(finalPoint.split(',')[0])
            y2=int(finalPoint.split(',')[1])
            if x1==x2 or y1==y2:
                M.add_line(x1, y1, x2, y2)
            else:
                M.add_line(x1, y1, x2, y2, True)
    if M.maxX<20:
        print(M)
    print(M.final_value())

if __name__=="__main__":
    main()
