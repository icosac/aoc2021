def main():
    fishes=list()
    with open("input.txt", "r") as f:
        for line in f:
            for fish in line.split("\n")[0].split(","):
                fishes.append(int(fish))

    for i in range(1, 81):
        for j in range(len(fishes)):
            if fishes[j]>0:
                fishes[j]-=1
            else:
                fishes[j]=6
                fishes.append(8)
    print(len(fishes))


if __name__=="__main__":
    main()
