def main():
    counter=0
    with open("input.txt", "r") as f:
        for line in f:
            values=line.split("\n")[0]
            left=values.split(" | ")[0]
            right=values.split(" | ")[1]
            for value in right.split(" "):
                if len(value)==2 or len(value)==4 or len(value)==3 or len(value)==7:
                    counter+=1
    print(counter)


if __name__=="__main__":
    main()
