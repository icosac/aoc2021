class Paper:
  def __init__(self) -> None:
      self.sheet=[["."]]
      self.maxX=1
      self.maxY=1
  
  def __str__(self) -> str:
      ret=""
      for row in self.sheet:
        for x in row:
          ret+=str(x)
        ret+="\n"

      return ret

  def add_point(self, line):
    y=int(line.split(",")[0])
    x=int(line.split(",")[1])
    self.up_size(x+1, y+1)
    try:
      self.sheet[x][y]="#"
    except Exception as E:
      print(E, self, self.maxX, self.maxY, x, y)


  def up_size(self, x, y):
    self.maxX=x if x>self.maxX else self.maxX
    self.maxY=y if y>self.maxY else self.maxY
    
    for line in self.sheet:
      for i in range(len(line), self.maxY):
        line.append(".")
    
    for i in range(len(self.sheet), self.maxX):
      self.sheet.append(["." for x in range(self.maxY)])

  def down_size(self, x=-1, y=-1):
    if x!=-1: #folding upwards
      self.sheet=self.sheet[:x]
    
    if y!=-1: #folding left
      for i in range(len(self.sheet)):
        self.sheet[i]=self.sheet[i][:y]   

  def fold(self, direction, where):
    #Check that no point is on the folding line
    if direction==0: #y -> up
      for v in range(len(self.sheet[where])):
        if self.sheet[where][v]!=".":
          raise Exception("Folding line is not empty")
        else:
          self.sheet[where][v]="-"

    else: #direction==1 x: -> left
      for row in self.sheet:
        if row[where]!=".":
          raise Exception("Folding line is not empty")
        else:
          row[where]="-"
        
    if direction==0: #y -> up
      for x in range(0, where): #I know, but it's not my fault if they have inverted the x and y :shrug
        for y in range(len(self.sheet[x])):
          if self.sheet[x][y]==".":
            try:
              self.sheet[x][y]=self.sheet[len(self.sheet)-x-1][y]
            except Exception as E:
              print(E, self, len(self.sheet)-x-1, y)
    
      self.down_size(x=where)

    else: #x -> left
      for x in range(0, len(self.sheet)):
        for y in range(where):
          if self.sheet[x][y]==".":
            try:
              self.sheet[x][y]=self.sheet[x][len(self.sheet[x])-y-1]
            except Exception as E:
              print(E, self, x, len(self.sheet[x])-y-1)
      
      self.down_size(y=where)

  def count_dots(self):
    counter=0
    for x in self.sheet:
      for v in x:
        if v=="#":
          counter+=1
    return counter


def main():
  instructions=Paper()
  with open("input.txt", "r") as f:
    for line in f:
      if not(line=="\n"):
        if not(line.startswith("fold")):
          instructions.add_point(line.split("\n")[0])
        else:
          direction=0 if "y=" in line.split("\n")[0] else 1
          where=int(line.split("\n")[0].split("=")[1])
          instructions.fold(direction, where)          

  print(instructions)
  print(instructions.count_dots())

if __name__=="__main__":
  main()