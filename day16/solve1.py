#!/usr/bin/env python3

from typing import Literal


class Packet:
    def __init__(self, string) -> None:
        self.version=int(string[:3], base=2)
        if int(string[3:6], base=2):
            self.literal=True
        else:
            self.literal=False
        
        self.content=list()
        self.ID=-1
        if self.literal:
            self.content=[""]
            self.literal_parse(string[6:])
        else:
            self.ID=int(string[6])
            if self.ID==0:
                pack_len=int(string[7, 22], base=2)
                string=string[22:]



    def literal_parse(self, string):
        goon=True
        i=0
        while goon:
            if string[i:i+5].startswith("0"):
                goon=False
            self.content[-1]+=string[i+1:i+5]
            print(string[i+1:i+5])
            i+=5
        



    def __str__(self) -> str:
        ret="v: "+str(self.version)+" t: "
        if self.literal:
            ret+="4 "
        else:
            ret+="0 "
        ret+="c: "+self.content
        return ret

def main():
    string=""
    value=0
    with open("input1.txt", "r") as f:
        for line in f:
            value=int(line.split("\n")[0], 16)
    
    print("{:x}".format(value))
    string=f"{value:b}"
    print(string)
    print(Packet(string))
#    convert_to_bit(string)
            
    
if __name__=="__main__":
    main()
