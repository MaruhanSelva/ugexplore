import random


def hammer_cells(size, x, y):
    """
    Hammer strike. Clears out a cross pattern. 
    """
    cells = []
    cell = size * x + y
    cells.append(cell)

    # Horizontal
    if 0 < y and y < size - 1:
        cell_new = cell + 1
        cells.append(cell_new)


        cell_new = cell - 1
        cells.append(cell_new)

    elif y == 0:
        cell_new = cell + 1
        cells.append(cell_new)

    else:
        cell_new = cell - 1
        cells.append(cell_new)


    # Vertical
    if 0 < x and x < size - 1:
        cell_new = cell - size
        cells.append(cell_new)
        
        cell_new = cell + size
        cells.append(cell_new)

    elif x == 0:
        cell_new = cell + size
        cells.append(cell_new)

    else:
        cell_new = cell - size
        cells.append(cell_new)
    
    return cells



class MiningBoard:

    def __init__(self, size):
        
        self.size = size
        self.l1 = []
        self.l2 = []
        self.l3 = []
        self.treasures = []
        self.damage = 0

        for i in range(size * size):
            self.l1.append(0)
            self.l2.append(1)
            self.l3.append(random.randint(0, 1))
        
    def randomize_top(self):
        for i in range(self.size * self.size):
            self.l3[i] = random.randint(0, 1)

    def get_treasures(self):
        return self.treasures
    
    def get_dmg(self):
        return self.damage
        
    def place_treasure(self, treasure):
        if treasure > (self.size * self.size):
            nums = self.size * self.size
            print("Choose a treasure amount that is less than " + str(nums))
        else:
            for i in range(treasure):
                num = random.randint(0, self.size * self.size - 1)
                while self.l1[num] != 0:
                    num = random.randint(0, self.size * self.size - 1)
                self.l1[num] = 3
                self.treasures.append(num)
    
    def clear_treasure(self):
        for i in range(len(self.treasures)):
            self.l1[i] = 0
    
    def hammer(self, x, y):
        if x > self.size - 1 or y > self.size - 1:
            print("FAILED, OUT OF BOUNDS")
        else:
            self.damage += 10
            cells = hammer_cells(self.size, x, y)
            self.l3[cells[0]] = 0
            self.l2[cells[0]] = 0

            for i in range(len(cells)):
                if (self.l3[cells[i]] == 0):
                    self.l2[cells[i]] = 0
                else:
                    self.l3[cells[i]] = 0


    def chisel(self, x, y):
        if x > self.size or y > self.size:
            print("FAILED, OUT OF BOUNDS")
        else:
            self.damage += 5
            cell = self.size * x + y
            if (self.l3[cell] == 0):
                self.l2[cell] = 0
            else:
                self.l3[cell] = 0

    def getoutermostcell(self, x, y):
        cell = self.size * x + y
        if self.l3[cell] == 1:
            return 3
        elif self.l2[cell] == 1:
            return 2
        else:
            return 1
