class Map:
    def __init__(self):
        self.map=[[0]]
        self.maxX=0
        self.maxY=0

    def add_line(self, x1, y1, x2, y2):
        self.maxX=x1+1 if x1>self.maxX else self.maxX
        self.maxX=x2+1 if x2>self.maxX else self.maxX
        self.maxY=y1+1 if y1>self.maxY else self.maxY
        self.maxY=y2+1 if y2>self.maxY else self.maxY

        self.enlarge()

        Ax=min(x1, x2)
        Bx=max(x1, x2)
        Ay=min(y1, y2)
        By=max(y1, y2)
        for x in range(Ax, Bx+1):
            for y in range(Ay, By+1):
                #print(x,y)
                self.map[x][y]+=1

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
                #print(x1, y1, x2, y2)
                M.add_line(x1, y1, x2, y2)
                #print(M)
            #minCoord[0]=x1 if x1<minCoord[-1] else minCoord[0]
            #minCoord[1]=y1 if y1<minCoord[1] else minCoord[1]
            #maxCoord[0]=x2 if x2>maxCoord[0] else maxCoord[0]
            #maxCoord[1]=y2 if y2>maxCoord[1] else maxCoord[1]

            #lines.append({"A" : (x1, y1), "B" : (x2, y2)})
    print(M.final_value())

if __name__=="__main__":
    main()
