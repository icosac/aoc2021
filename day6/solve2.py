def main():
    fishes=list()
    days=10
    
    with open("input2.txt", "r") as f:
        for line in f:
            for fish in line.split("\n")[0].split(","):
                fishes.append(int(fish))
    
    for i in range(1, days):
        for j in range(len(fishes)):
            if fishes[j]>0:
                fishes[j]-=1
            else:
                fishes[j]=6
                fishes.append(8)
        print(i, len(fishes))

    tot_fishes=len(fishes)
    for fish in fishes:
        remaining_days=days-fish
        created_fishes=int(remaining_days/6)
        for i in range(created_fishes):
            remaining_days-=8
            created_fishes+=(remaining_days/6)



if __name__=="__main__":
    main()
