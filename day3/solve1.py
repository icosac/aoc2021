from math import ceil

def main():
    gamma=0
    epsilon=0
    values=list()
    n=0
    with open("input.txt", "r") as f:
        for line in f:
            n+=1
            line=line.split("\n")[0]
            for i in range(len(line)):
                try:
                    values[i]+=int(line[i])
                except Exception:
                    values.append(int(line[i]))
    gammaS=""
    epsilonS=""
    for value in values:
        if (value/n)<0.5:
            gammaS+="0"
            epsilonS+="1"
        else:
            gammaS+="1"
            epsilonS+="0"

    print(gammaS, epsilonS)
    gamma=int(gammaS, 2)
    epsilon=int(epsilonS, 2)
    print(gamma, epsilon, gamma*epsilon)


if __name__=="__main__":
    main()
