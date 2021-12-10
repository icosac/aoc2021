class Symbols:
    opening=["(", "[", "<", "{"]
    closing=[")", "]", ">", "}"]
    points =[3, 57, 25137, 1197]

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
        


def main():
    points=0
    lines=list()
    with open("input.txt", "r") as f:
        for line in f:
            points+=checkLine(line.split("\n")[0])

    print(points)

if __name__=="__main__":
    main()
