def main():
    hor=0
    dep=0
    with open("input.txt", "r") as f:
        for line in f:
            try:
                (move, value)=line.split("\n")[0].split(" ")
                if move=="forward":
                    hor+=int(value)
                elif move=="down":
                    dep+=int(value)
                elif move=="up":
                    dep-=int(value)
                else:
                    print("Wrong value")
            except Exception:
                print(line)

    print(hor, dep, hor*dep)

if __name__=="__main__":
    main()
