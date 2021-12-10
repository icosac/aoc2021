def main():
    submarines=list()
    with open("input.txt", "r") as f:
        for line in f:
            for sub in line.split("\n")[0].split(","):
                submarines.append(int(sub))
    
    best=2**32
    for point in range(0, max(submarines)):
        cost=0
        for sub in submarines:
            cost+=abs(point-sub)
        best=best if best<cost else cost

    print(best)

if __name__=="__main__":
    main()
