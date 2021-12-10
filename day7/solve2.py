def costF(sub, target):
    ret=0
    A=min(sub, target)
    B=max(sub, target)
    for n in range(A, B):
        ret+=(B-n)
    return ret

def main():
    submarines=list()
    with open("input.txt", "r") as f:
        for line in f:
            for sub in line.split("\n")[0].split(","):
                submarines.append(int(sub))
    
    best1=2**32
    for point in range(0, max(submarines)):
        print((point*100/max(submarines)), end="\r")
        cost1=0
        for sub in submarines:
            n=abs(sub-point)
            cost1+=int(n*(n+1)/2.0)
        best1=best1 if best1<cost1 else cost1
    print()
    print(best1)

    best=2**32
    for point in range(0, max(submarines)):
        print((point*100/max(submarines)), end="\r")
        cost=0
        for sub in submarines:
            cost+=costF(point, sub)
        best=best if best<cost else cost
    print()
    print(best)
    

if __name__=="__main__":
    main()
