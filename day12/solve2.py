from copy import deepcopy

class Node:
    def __init__(self, name:str):
        self.name=name
        # start=0, end=-1, small=2, big=-2
        if self.name=="start":
            self.dim=0
        elif self.name=="end":
            self.dim=-2
        elif self.name.islower():
            self.dim=2
        else:
            self.dim=-2
        self.neighbors=list()
        self.children=list()
        self.parents=list()

    def __eq__(self, other):
        if self.name==other.name:
            return True
        else:
            return False

    def addNeighbor(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)
            self.children.append(node)
            self.parents.append(node)
        else:
            raise Exception(node, "already present in neighbors:", self.neighbors)

    def __str__(self):
        ret=self.name+": "
        for node in self.neighbors:
            ret+="("+node.name+", "+str(node.dim)+"), "
        return ret

def printNodes(lst, string=""):
    print(string, end='')
    for node in lst:
        print(node.name, end=", ")
    print()

def valid(path):
    for i in range(len(path)):
        if (path[i].islower() and path[i] in path[i+1:]
                or path[i]==Node("start")):
            return False
    return True

class Graph:
    def __init__(self, nodes):
        self.nodes=nodes

    def __str__(self):
        ret=""
        for node in self.nodes:
            ret+=str(node)
            ret+="\n"
        return ret

    def find_paths(self, node, used=False):
        paths=[]
        print(node, used)
        if node==Node("end"):
            return [[self.nodes[self.nodes.index(Node("end"))]]]
        else:
            for nd in node.neighbors:
                if nd!=Node("start"):
                    nd.dim -= 1
                    if not used:
                        used=True
                    else:
                        if nd.dim==1:
                            nd.dim+=1
                            continue
                    below_paths=self.find_paths(nd, used)
                    try:
                        for path in below_paths:
                            paths.append([node]+path)
                    except Exception as E:
                        print(E, path, type(path), below_paths)
                    nd.dim+=1
                    used=False

            # print("paths:", len(paths))
            # for path in paths:
            #     printNodes(path)
            # print("end!!!")
            return paths


def main():
    graph=list()
    with open("input1.txt", "r") as f:
        for line in f:
            A=Node(line.split("\n")[0].split("-")[0])
            B=Node(line.split("\n")[0].split("-")[1])

            # Check if node is in graph
            if B not in graph:
                graph.append(B)
            if A not in graph:
                graph.append(A)
            # Now I have a reference to the node in the graph
            A = graph[graph.index(A)]
            B = graph[graph.index(B)]
            A.addNeighbor(B)
            B.addNeighbor(A)
    graph=Graph(graph)

    print(graph)
    print(len(graph.find_paths(graph.nodes[graph.nodes.index(Node("start"))])))




if __name__ == '__main__':
    main()


