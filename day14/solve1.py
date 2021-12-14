def main():
    steps=10

    template=""
    rules=dict()
    with open("input.txt", "r") as f:
        for line in f:
            if line!="\n":
                if "->" not in line:
                    template=line.split("\n")[0]
                else:
                    rules[line.split("\n")[0].split(" -> ")[0]]=line.split("\n")[0].split(" -> ")[1]
    
    print(template, rules)

    for step in range(steps):
        i=0
        while i < len(template)-1:
            try:
                insert=rules[template[i]+template[i+1]]
                template=template[:i+1]+insert+template[i+1:]
                i+=2
            except Exception as E:
                pass
        
        print(template)
    
    counters=dict()
    for c in template:
        try:
            counters[c]+=1
        except Exception as E:
            counters[c]=1

    min=2**32
    max=0
    for key in counters.keys():
        value=counters[key]
        print(key, value)
        if value<min:
            min=value
        if value>max:
            max=value
    print(max-min)




if __name__=="__main__":
    main()