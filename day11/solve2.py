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


class Map:
    def __init__(self):
        self.map = [[-2 ** 32], [-2 ** 32]]

    def add_line(self, line):
        self.map.insert(-1, [-2 ** 32])
        for v in line:
            self.map[-2].append(int(v))
        self.map[-2].append(-2 ** 32)
        self.resize(len(line))

    def resize(self, n):
        self.map[0] = [-2 ** 32 for i in range(n + 2)]
        self.map[-1] = [-2 ** 32 for i in range(n + 2)]
        for i in range(len(self.map)):
            if len(self.map[i]) != (n + 2):
                raise Exception("Wrong dimension", i, len(self.map[i]), n+2)

    def flash(self, octo_list, x, y):
        for octoX in range(x - 1, x + 2):
            for octoY in range(y - 1, y + 2):
                if (octoX, octoY) not in octo_list:
                    try:
                        self.map[octoX][octoY] += 1
                    except Exception as E:
                        print(E, octoX, octoY, self)
                    if self.map[octoX][octoY] > 9:
                        octo_list.append((octoX, octoY))
                        self.flash(octo_list, octoX, octoY)

    def map_flash(self):
        to_flash = list()
        # First, the energy level of each octopus increases by 1
        for octoX in range(1, len(self.map) - 1):
            for octoY in range(1, len(self.map[octoX]) - 1):
                self.map[octoX][octoY] += 1

        # Then, any octopus with an energy level greater than 9 flashes
        for octoX in range(1, len(self.map) - 1):
            for octoY in range(1, len(self.map[octoX]) - 1):
                if self.map[octoX][octoY] > 9 and (octoX, octoY) not in to_flash:
                    to_flash.append((octoX, octoY))
                    self.flash(to_flash, octoX, octoY)

        for (x, y) in to_flash:
            self.map[x][y] = 0

        return to_flash

    def __str__(self):
        ret = "\n"
        for octoLine in self.map:
            for octo in octoLine:
                if octo < -1 :
                    pass
                    #ret += "B"
                elif octo==0:
                    ret += color.RED+str(octo)+color.END
                else:
                    ret += str(octo)
            ret += "\n"

        return ret

    def all_flashing(self):
        self.map_flash()

        for octoLine in self.map[1:-2]:
            for octo in octoLine[1:-2]:
                if octo!=0:
                    return False
        return True


def main():
    steps=0
    octoMap = Map()
    with open("input.txt", "r") as f:
        for line in f:
            octoMap.add_line(line=line.split("\n")[0])
    while(True):
        if octoMap.all_flashing():
            print(steps+1)
            break
        steps+=1

    print(octoMap)


if __name__ == "__main__":
    main()
