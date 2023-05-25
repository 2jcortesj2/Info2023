import pygame
import random

# Datos principales 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CIRCLE_SPEED = 1

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clases
class Circle:
    def __init__(self):
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice(["R", "L"])
    def move(self):
        x, y = self.positions[0]
        if self.direction[0] == "R":
            x += CIRCLE_SPEED
        elif self.direction[0] == "L":
            x -= CIRCLE_SPEED
        elif self.direction[0] == "S":
            x = x
        self.positions.insert(0, (x, y))
        self.positions.pop()
    def draw(self, surface):
        for position in self.positions:
            pygame.draw.circle(surface, GREEN, (position[0], position[1]), 20)

class Stop:
    pass

class Reflex:
    pass

class User:
    pass

# PYGAME
pygame.init()

screen = pygame.display.set_mode( [SCREEN_WIDTH, SCREEN_HEIGHT] )
pygame.display.set_caption("Circulo")

clock = pygame.time.Clock()


circle = Circle()
run = True
game_over = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        # Usando el teclado
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                circle.direction = "S" # Para que pare en la posicion en que este cuando presione la tecla
                circle = Circle()
                game_over = False

    if game_over == False:
        # Mover el circulo 
        circle.move()

        if circle.positions[0][0] < 0 or circle.positions[0][0] > SCREEN_WIDTH - 10:
            game_over = True
        for position in circle.positions[1:]:
            if circle.positions[0] == position:
                game_over = True

    # Dibujos de la pantalla
    screen.fill(WHITE)
    circle.draw(screen)
    square = pygame.Surface([100, 100])
    screen.blit(square, (100, 225))
    

    # Actualizar la pantalla 
    pygame.display.update()
    clock.tick(60)

pygame.quit()