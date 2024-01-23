#pygame setup
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Catch the Weasel Game")
pygame.display.set_caption("Catch the Weasel Game")
test_font = pygame.font.Font(None, 100)

garden_surface = pygame.image.load('radish_garden.jpg')
text_surface = test_font.render('where the weasel',True, 'Red')

class Weasel():
    surface = pygame.image.load('weasel_180.png').convert_alpha()
    x_pos = 0
    right_facing = True

    def __init__(self, x_pos = 0):
        self.x_pos = x_pos
        self.surface = pygame.image.load('weasel_180.png').convert_alpha()
        self.rect = self.surface.get_rect(midbottom = ((self.x_pos,0)))

    def move(self):
        if self.right_facing:
            self.x_pos +=4
        else: 
            self.x_pos -= 4
        if self.x_pos > 1280: self.right_facing = False 
        if self.x_pos < -100: self.right_facing = True


weasel = Weasel()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(garden_surface, (0,0))
    screen.blit(text_surface, (600,300))
    screen.blit(weasel.surface, (weasel.x_pos, 300))
    weasel.move()
    print(weasel.rect.topleft)

    # Update game logic here

    # Draw game elements here

    pygame.display.flip()
    clock.tick(60) # limits FPS to 60

pygame.quit()

