import re
from math import sqrt

def compute_x(x_min, x_max):
    values=list()
    c=-2*x_min
    n_1=int(-1+sqrt(-1-4*c)/2)
    n_2=int(-1-sqrt(-1-4*c)/2)
    if n_1*(n_1+1)/2>x_min and n_1*(n_1+1)/2<x_max:
        values.append(n_1)
    if n_2*(n_2+1)/2>x_min and n_2*(n_2+1)/2<x_max:
        values.append(n_2)





def main():
    area=dict()
    initial_pos={"x": 0, "y": 0}
    with open("input1.txt", "r") as f:
        for line in f:
            d=re.compile(r"target area: x=(?P<x1>-?\d+)..(?P<x2>-?\d+), y=(?P<y1>-?\d+)..(?P<y2>-?\d+).*").match(line).groupdict()
            area={
                "x_min": min(int(d["x1"]), int(d["x2"])),
                "x_max": max(int(d["x1"]), int(d["x2"])), 
                "y_min": min(int(d["y1"]), int(d["y2"])),
                "y_max": max(int(d["y1"]), int(d["y2"])),
            }    

    print(area)

if __name__=="__main__":
    main()