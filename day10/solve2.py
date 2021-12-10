class Symbols:
    opening=["(", "[", "{", "<"]
    closing=[")", "]", "}", ">"]
    points =[3, 57, 1197, 25137]

def checkLine(line):
    if line[0] not in Symbols.opening:
        return Symbols.points[Symbols.closing.index(line[0])]
    shouldClose=list(line[0])
    for c in line[1:]:
        if c in Symbols.opening:
            shouldClose.append(c)
        else:
            index=Symbols.opening.index(shouldClose[-1])
            expected=Symbols.closing[index]
            if c!=expected:
                print(line, "Expected", expected, "but found", c, "instead.", Symbols.points[Symbols.closing.index(c)])
                return Symbols.points[Symbols.closing.index(c)]
            else:
                shouldClose=shouldClose[:-1]
    return 0
        

def correctLine(line):
    if line[0] not in Symbols.opening:
        return Symbols.points[Symbols.closing.index(line[0])]
    shouldClose=list(line[0])
    for c in line[1:]:
        if c in Symbols.opening:
            shouldClose.append(c)
        else:
            shouldClose=shouldClose[:-1]
    points=0
    for c in reversed(shouldClose):
        points*=5
        closing=Symbols.opening.index(c)+1
        points+=closing

    return points

def main():
    points=list()
    lines=list()
    with open("input.txt", "r") as f:
        for line in f:
            value=checkLine(line.split("\n")[0])
            if value==0:
                points.append(correctLine(line.split("\n")[0]))

    print(points)
    print(sorted(points)[int(len(points)/2)])

if __name__=="__main__":
    main()
