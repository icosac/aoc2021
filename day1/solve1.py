def main():
    with open("input1.txt", "r") as f:
        n1=0
        prev=1000000000000000000000
        for line in f:
            try:
                depth=int(line.split("\n")[0])
                if depth>prev:
                    n1+=1
                    print(str(depth)+"\tincreased")
                else:
                    print(str(depth)+"\tdecreased")
                prev=depth
            except Exception:
                pass

        print(n1)
                



if __name__=="__main__":
    main()
