from math import log2

class Node:
    def __init__(self, value, distance) -> None:
        self.value=value
        self.distance=distance

    def priority(self):
        return self.distance
    
    def __str__(self):
        return "({}, {})".format(self.value, self.distance)

class PriorityQueue:
    def __init__(self, lst=list()) -> None:
        self.elements=lst
    
    def __len__(self):
        return len(self.elements)

    def push(self, element):
        prev_len=len(self)
        found=False

        # If list is empty
        if len(self.elements)==0: 
            self.elements.append(element)
            found=True
        # If the element priority is as big or bigger than the last element in queue, add it
        if not(found) and (element.priority()>self.elements[-1].priority() or element.priority()==self.elements[-1].priority()):
            self.elements.append(element)
            found=True
        # If the element priority is as big or smaller than the first element in queue, insert it
        if not(found) and (element.priority()<self.elements[0].priority() or element.priority()==self.elements[0].priority()):
            self.elements.insert(0, element) #if element>self.elements[0], then the first if is true and is dealt there
            found=True
        # If the list is just two elements [A, B], there is one other case to consider, that is A<C<B 
        if not(found) and len(self.elements)%2==0:
            if element.priority()>self.elements[0] and element.priority()<self.elements[1]:
                self.elements.insert(1, element)
                found=True
        
        pos=int(len(self.elements)/2)
        incr=pos
        print("inserting {} in <{}> {}".format(element, self, found))
        while not(found) and incr!=0:
            incr=int(incr/2)
            print("Checking pos {} len {} el {} queue <{}>".format(pos, len(self), element, self))
            if self.elements[pos].priority()==element.priority():
                self.elements.insert(pos, element)
                found=True
            elif (self.elements[pos].priority()<element.priority() and
                    self.elements[pos+1].priority()>element.priority()):
                self.elements.insert(pos+1, element)
                found=True
            elif (self.elements[pos].priority()>element.priority() and
                    self.elements[pos+1].priority()<element.priority()):
                pos+=incr
            else:
                pos-=incr

        print()
        if len(self.elements)!=(prev_len+1):
            raise Exception("Push did not push anything")

    def pop(self):
        if len(self)>0:
            element=self.elements[0]
            self.elements=self.elements[1:]
            return element
        else:
            raise Exception("PriorityQueue is empty")

    def __str__(self):
        ret=""
        for element in self.elements:
            ret+=str(element)+", "
        return ret

    def __iter__(self):
        yield self.elements

    def find(self, element):
        if len(self)==0:
            return -1
            
        # if self.elements[0]==element:
        #     return 0
        # elif self.elements[-1]==element:
        #     return len(self)-1

        found=False
        pos=int(len(self)/2)
        incr=pos
        try:
            while incr!=0:
                if pos<len(self):
                    if self.elements[pos]==element:
                        return pos
                    elif self.elements[pos]<element:
                        pos+=incr
                    else:
                        pos-=incr
                    incr=int(incr/2)
                else:
                    pos-=incr
                    incr=int(incr/2)
            if self.elements[pos]==element:
                return pos
            else:
                return -1
        except Exception as E:
            print(E, pos, len(self))
            raise E

    def remove(self, element):
        pos=self.find(element)
        if pos==-1:
            raise Exception("Value not in queue {}".format(pos))
        elif pos==0:
            self.elements=self.elements[1:]
        elif pos==len(self)-1:
            self.elements=self.elements[:-1]
        else:
            self.elements=self.elements[:pos]+self.elements[pos+1:]

    def __contains__(self, element):
        return self.find(element)!=-1


a=PriorityQueue()
for i in range(0, 10):
    if i%2==0:
        a.push(Node(i, i+1))
        print(i, i+1)
    else:
        a.push(Node(i, i-10+1))
        print(i, i-10+1)
print(a)
