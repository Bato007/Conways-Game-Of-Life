import pygame
width, height = 100, 100
figures = 0

class Life(object):
    def __init__(self, screen, initial=None):
        self.screen = screen
        self.alive = initial
        self.modx = width 
        self.mody = height
        for cell in initial: self.giveLife(cell[0], cell[1])
        self.die = []
        self.birth = []
        self.check = []

    def kill(self, x, y):
        self.screen.set_at((x, y), (0, 0, 0))
        try: self.alive.pop(self.alive.index((x, y)))
        except: pass

    def giveLife(self, x, y):
        self.screen.set_at((x, y), (255, 255, 255))
        try: 
            if ((x, y) not in self.alive):
                self.alive.append((x, y))
        except: pass

        self.screen.set_at((x, y), (255, 255, 255))

    def __checkLives__(self, x, y):
        neighbors = -1
        for i in range(x-1, (x+2)%self.modx):
            for j in range(y-1, (y+2)%self.mody):
                try:
                    if self.screen.get_at((i, j))[0] == 255: neighbors += 1
                    elif (i, j) not in self.check: self.check.append((i, j))
                except: pass
        if neighbors < 2 or neighbors > 3:
            self.die.append((x, y))

    def __checkBorns__(self, x, y):
        neighbors = 0
        
        for i in range(x-1, (x+2)%self.modx):
            for j in range(y-1, (y+2)%self.mody):
                try:
                    if neighbors > 3: return
                    if (self.screen.get_at((i, j))[0] == 255): neighbors += 1
                except: pass
                        
        if neighbors == 3 and ((x, y) not in self.birth): self.birth.append((x, y))

    def turn(self):
        for cell in self.alive: 
            self.__checkLives__(cell[0], cell[1])
        for cell in self.check:
            self.__checkBorns__(cell[0], cell[1])
        self.check = []
        for cell in self.die: 
            self.kill(cell[0], cell[1])
        self.die = []
        for cell in self.birth: 
            self.giveLife(cell[0], cell[1])
        self.birth = []
        # print(self.die, self.birth)

def boat(x, y):
    return [
        (x, y), 
        ((x+1)%width, y),
        (x, (y+1)%height),
        ((x+1)%width, (y+2)%height),
        ((x+2)%width, (y+1)%height),
    ]

def snake(x, y):
    return [
        (x, y),
        ((x+2)%width, y),
        ((x+3)%width, y),
        (x, (y+1)%height),
        ((x+1)%width, (y+1)%height),
        ((x+3)%width, (y+1)%height),
    ]

def ship(x, y):
    return [
        (x, y),
        ((x+1)%width, y),
        (x, (y+1)%height),
        ((x+2)%width, (y+1)%height),
        ((x+1)%width, (y+2)%height),
        ((x+2)%width, (y+2)%height),
    ]

def aircraftCarrier(x, y):
    return [
        (x, y),
        ((x+1)%width, y),
        (x, (y+1)%height),
        ((x+3)%width, (y+1)%height),
        ((x+2)%width, (y+2)%height),
        ((x+3)%width, (y+2)%height),
    ]

def movement(x, y):
    return [
        ((x+1)%width, y),
        ((x+2)%width, (y+1)%height),
        (x, (y+2)%height),
        ((x+1)%width, (y+2)%height),
        ((x+2)%width, (y+2)%height),
        ((x+3)%width, (y+4)%height),
        ((x+4)%width, (y+4)%height),
        ((x+3)%width, (y+5)%height),
        ((x+4)%width, (y+6)%height),
        ((x+5)%width, (y+6)%height),
        ((x+6)%width, (y+6)%height),
        ((x+6)%width, (y+7)%height)
    ]

def ring(x, y):
    return [
        (x, y),
        ((x+1)%width, y),
        ((x+2)%width, y),
        ((x+4)%width, y),
        ((x+5)%width, y),
        ((x+6)%width, y),

        (x, (y+1)%height),
        ((x+2)%width, (y+1)%height),
        ((x+4)%width, (y+1)%height),
        ((x+6)%width, (y+1)%height),

        (x, (y+2)%height),
        ((x+1)%width, (y+2)%height),
        ((x+2)%width, (y+2)%height),
        ((x+4)%width, (y+2)%height),
        ((x+5)%width, (y+2)%height),
        ((x+6)%width, (y+2)%height)
    ]

def flower(x, y):
    return [
        (x, (y-4)%height),
        (x, (y-3)%height),
        (x, (y-2)%height),

        ((x-4)%width, y),
        ((x-3)%width, y),
        ((x-2)%width, y),
        ((x+2)%width, y),
        ((x+3)%width, y),
        ((x+4)%width, y),

        (x, (y+4)%height),
        (x, (y+3)%height),
        (x, (y+2)%height),
    ]

def glider(x, y):
    return [
        ((x+2)%width, y),
        (x, (y+1)%height),
        ((x+2)%width, (y+1)%height),
        ((x+1)%width, (y+2)%height),
        ((x+2)%width, (y+2)%height),
    ]

def canoe(x, y):
    return [
        ((x+3)%width, y),
        ((x+4)%width, y),
        ((x+4)%width, (y+1)%height),
        ((x+3)%width, (y+2)%height),
        (x, (y+3)%height),
        ((x+2)%width, (y+3)%height),
        (x, (y+4)%height),
        ((x+1)%width, (y+4)%height)
    ]

def cloverleaf(x, y):
    return [
        ((x+3)%width, y),
        ((x+5)%width, y),
        ((x+1)%width, (y+1)%height),
        ((x+2)%width, (y+1)%height),
        ((x+3)%width, (y+1)%height),
        ((x+5)%width, (y+1)%height),
        ((x+6)%width, (y+1)%height),
        ((x+7)%width, (y+1)%height),
        (x, (y+2)%height),
        ((x+4)%width, (y+2)%height),
        ((x+8)%width, (y+2)%height),
        (x, (y+3)%height),
        ((x+2)%width, (y+3)%height),
        ((x+6)%width, (y+3)%height),
        ((x+8)%width, (y+3)%height),
        ((x+1)%width, (y+4)%height),
        ((x+2)%width, (y+4)%height),
        ((x+4)%width, (y+4)%height),
        ((x+6)%width, (y+4)%height),
        ((x+7)%width, (y+4)%height),

        ((x+1)%width, (y+6)%height),
        ((x+2)%width, (y+6)%height),
        ((x+4)%width, (y+6)%height),
        ((x+6)%width, (y+6)%height),
        ((x+7)%width, (y+6)%height),
        (x, (y+7)%height),
        ((x+2)%width, (y+7)%height),
        ((x+6)%width, (y+7)%height),
        ((x+8)%width, (y+7)%height),
        (x, (y+8)%height),
        ((x+4)%width, (y+8)%height),
        ((x+8)%width, (y+8)%height),
        ((x+1)%width, (y+9)%height),
        ((x+2)%width, (y+9)%height),
        ((x+3)%width, (y+9)%height),
        ((x+5)%width, (y+9)%height),
        ((x+6)%width, (y+9)%height),
        ((x+7)%width, (y+9)%height),
        ((x+3)%width, (y+10)%height),
        ((x+5)%width, (y+10)%height),
    ]

figures = [
    boat(84, 42),
    snake(32, 64),
    snake(64, 23),
    ship(21, 21),
    ship(42, 32),
    aircraftCarrier(53, 89),
    movement(10, 55),
    ring(50, 50),
    ring(80, 20),
    ring(26, 60),
    flower(75, 75),
    flower(10, 30),
    flower(90, 90),
    flower(3, 70),
    glider(10, 10),
    glider(20, 20),
    glider(10, 80),
    glider(70, 70),
    glider(30, 90),
    canoe(90, 10),
    cloverleaf(15, 15),
    cloverleaf(90, 50),
    cloverleaf(15, 80)
]

pygame.init()
screen = pygame.display.set_mode((width, height))

cells = []
for figure in figures:
    for cell in figure:
        cells.append(cell)

r = Life(screen, cells)
cont = 0
while cont < 500:
    pygame.time.delay(10)
    r.turn()
    cont += 1
    pygame.display.flip()