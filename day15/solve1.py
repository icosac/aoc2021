from copy import deepcopy
from typing import Literal

sizeY=10
sizeX=10

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class Node:
    def __init__(self, coord, value) -> None:
        self.coord=coord
        self.value=value
        self.visited=False
        self.distance=2**32
        self.parent=None

    def __int__(self):
        return self.value

    def __str__(self):
        return "({}, {}) {} {}".format(self.coord[0], str(self.coord[1]), str(self.value), self.distance)

    def __eq__(self, other):
        return self.coord==other.coord

    def __lt__(self, other):
        return self.distance<other.distance
    
    def __gt__(self, other):
        return self.distance>other.distance

    def __le__(self, other):
        return self.distance<other.distance or self.distance==other.distance
    
    def __ge__(self, other):
        return self.distance<other.distance or self.distance==other.distance

def print_graph(graph, sol=list(), distances=False):
    for i in range(len(graph)):
        if graph[i] in sol:
            print(color.RED, end="")
        if distances:
            print(" {:2d} ".format(graph[i].distance), end="")
        else:
            print("{:d}".format(graph[i].value), end="")
        if graph[i] in sol:
            print(color.END, end="")
        if i%sizeY==sizeY-1:
            print()


def dijkstra(graph):
    visited=list()
    unvisited=deepcopy(graph)
    while len(unvisited)!=0:
        best=None
        for node in graph:
            if (not node.visited and 
                (best is None or node.distance<best.distance)):
                best=node

        pos=graph.index(best)

        #Update neighbors distances
        if pos>sizeY: #Above
            if not graph[pos-sizeY].visited:
                graph[pos-sizeY].distance=min(graph[pos-sizeY].distance, graph[pos-sizeY].value+best.distance)
        if (pos%sizeY)>0: #Left
            if not graph[pos-1].visited:
                graph[pos-1].distance=min(graph[pos-1].distance, graph[pos-1].value+best.distance)
        if (pos%sizeY)<sizeY-1: #Right
            if not graph[pos+1].visited:
                graph[pos+1].distance=min(graph[pos+1].distance, graph[pos+1].value+best.distance)
        if pos<(sizeY*(sizeX-1)): #Bottom
            if not graph[pos+sizeY].visited:
                graph[pos+sizeY].distance=min(graph[pos+sizeY].distance, graph[pos+sizeY].value+best.distance)

        visited.append(best)
        best.visited=True
        unvisited.remove(best)

def neighbors(node, graph):
    neighs=list()
    pos=node.coord[0]*sizeY+node.coord[1]
    if pos>sizeY: #Above
        neighs.append(graph[pos-sizeY])
    if (pos%sizeY)>0: #Left
        neighs.append(graph[pos-1])
    if (pos%sizeY)<sizeY-1: #Right
        neighs.append(graph[pos+1])
    if pos<(sizeY*(sizeX-1)): #Bottom
        neighs.append(graph[pos+sizeY])
    return neighs


def a_star(graph):
    open=[graph[0]]
    closed=list()
    best=min(open)
    while best!=graph[-1]:
        closed.append(best)
        for neighbor in neighbors(best, graph):
            cost=best.distance+neighbor.value
            if neighbor in open and cost<neighbor.distance:
                open.remove(neighbor)
            if neighbor in closed and cost<neighbor.distance:
                closed.remove(neighbor)
            if neighbor not in closed and neighbor not in open:
                neighbor.distance=cost
                open.append(neighbor)
                neighbor.parent=best
        open.remove(best)
        best=min(open)
    
    nodes=[graph[-1]]
    while nodes[-1]!=graph[0]:
        nodes.append(nodes[-1].parent)
        for n in nodes:
            print(n, end=" ")
        print()

    sum=0
    for n in reversed(nodes):
        print(n, end="")
        sum+=n.value
    print()
    sum-=graph[0].value
    print("Total cost: ", sum)


       
def find_shortest(graph):
    nodes=[graph[-1]]
    while nodes[-1].coord!=(0,0) and len(nodes)<len(graph):
        pos=graph.index(nodes[-1])
        neighbors=list()
        if pos>sizeY-1: #Above
            neighbors.append(graph[pos-sizeY])            
        if (pos%sizeY)>0: #Left
            neighbors.append(graph[pos-1])
        if (pos%sizeY)<sizeY-1: #Right
            neighbors.append(graph[pos+1])
        if pos<(sizeY*(sizeX-1)): #Bottom        
            neighbors.append(graph[pos+sizeY])
        best=min(neighbors)
        nodes.append(best)
 
    print("Solution: ", end="")
    for node in reversed(nodes):
        print(node.value, end=", ")
    print()

    print_graph(graph, nodes)

    sum=0
    for node in nodes[:-1]:
        sum+=node.value
    print("Final cost: ", sum)

def main():
    global sizeY
    global sizeX

    graph=list()
    with open("input.txt", "r") as f:
        i=0
        for line in f:
            j=0
            for value in line.split("\n")[0]:
                graph.append(Node((i,j), int(value)))
                j+=1
            sizeY=j
            i+=1
        sizeX=i
        
    graph[0].distance=0
    a_star(graph)
    # dijkstra(graph)
    # find_shortest(graph)

if __name__=="__main__":
    main()