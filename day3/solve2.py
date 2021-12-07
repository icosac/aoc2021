def mostCommonBit(lst, pos):
    bit=0
    for value in lst:
        bit+=int(value[pos])

    if (bit/len(lst))<0.5:
        bit=0
    else:
        bit=1

    lst1=list()
    lst2=list()
    for value in lst:
        if int(value[pos])==bit:
            lst1.append(value)
        else:
            lst2.append(value)


    return (lst1, lst2, bit)


def main():
    values=list()
    firstBit=0
    with open("input.txt", "r") as f:
        for line in f:
            values.append(line.split("\n")[0])
            firstBit+=int(values[-1][0])

    co2=list()
    o2=list()
    if (firstBit/len(values))<0.5:
        firstBit=0
    else:
        firstBit=1

    for value in values:
        if int(value[0])==firstBit:
            o2.append(value)
        else:
            co2.append(value)

    lenS=len(o2[0])
    for i in range(1, lenS):
        o2, _, _=mostCommonBit(o2, i)
        if len(o2)==1:
            break

    lenS=len(co2[0])
    for i in range(1, lenS):
        _, co2, _=mostCommonBit(co2, i)
        if len(co2)==1:
            break

    print(o2[0], co2[0], (int(o2[0], 2)*int(co2[0], 2)))





if __name__=="__main__":
    main()
