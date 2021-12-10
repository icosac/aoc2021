class Display:
    def __init__(self):
        self.display=[["a", "b", "c", "d", "e", "f", "g"] for x in range(0, 7)]
    
    def check(self, string, value):
        if value==0:
            pass
        elif value==1:
            pass
        elif value==2: 
            pass
        elif value==3: 
            pass
        elif value==4: 
            pass
        elif value==5: 
            pass
        elif value==6: 
            pass
        elif value==7: 
            pass
        elif value==8:
            pass
        elif value==9:
            pass

    def guessV(self, strings):
        

        

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
