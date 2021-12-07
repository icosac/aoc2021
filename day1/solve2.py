def main():
    #Create array for part1
    depths=list()
    with open("input1.txt", "r") as f:
        for line in f:
            depth=int(line.split("\n")[0])
            depths.append(depth)
    
    print(len(depths))
    sumA=list()
    n=0
    i=0
    for depthID in range(len(depths)-2):
        sumA.append(depths[depthID]+depths[depthID+1]+depths[depthID+2])
    #Part1 again
    n=0
    prev=1000000000000000000000
    for sumD in sumA:
        if sumD>prev:
            n+=1
            print(str(sumD)+"\tincreased")
        else:
            print(str(sumD)+"\tdecreased")
        prev=sumD

    print(n)


if __name__=="__main__":
    main()
