import matplotlib.pyplot as plt
from math import log2 as log
import numpy as np

def main():
    fishes=list()
    days=np.arange(1, 144, 6)
    
    with open("input.txt", "r") as f:
        for line in f:
            for fish in line.split("\n")[0].split(","):
                fishes.append(int(fish))
    
    print(fishes)
    setFishes=list()
    for fish in fishes:
        if fish not in setFishes:
            setFishes.append(fish)
    print(setFishes)

    setFishes=[0]
    newFishes=dict()
    fishperday=list()
    for day in days:
        for fish in setFishes:
            newFishes[str(fish)]=0
            compFishes=[fish]
            for i in range(1, day+1):
                for j in range(len(compFishes)):
                    if compFishes[j]>0:
                        compFishes[j]-=1
                    else:
                        compFishes[j]=6
                        compFishes.append(8)
                #print((setFishes.index(fish)+i)*100/(len(setFishes)+256))
            
            newFishes[str(fish)]=len(compFishes)
            fishperday.append(len(compFishes))
        print(day, newFishes)

    plt.scatter(days, [value for value in fishperday])
    plt.show()

    tot=0
    for fish in fishes:
        tot+=newFishes[str(fish)]

    print(tot)



if __name__=="__main__":
    main()
