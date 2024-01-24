#pygame setup
import pygame
pygame.init()

# Define some constants for screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# GRID_SIZE = 10
# RADISH_SIZE = SCREEN_WIDTH // GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# pygame.display.set_caption("Whea Za Weasel Game")
test_font = pygame.font.Font(None, 100)

garden_surface = pygame.image.load('radish_garden.jpg')
text_surface = test_font.render('Whea Za Weasel Game',True, 'Red')

class Weasel(pygame.sprite.Sprite):
    def __init__(self, x_pos = 0):
        super().__init__()
        self.image = pygame.image.load('weasel_180.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = ((x_pos, SCREEN_HEIGHT - 100)))
        self.right_facing = True

    def move(self):
        if self.right_facing:
            self.rect.x +=4
        else: 
            self.rect.x -= 4
        if self.rect.right > SCREEN_WIDTH: self.right_facing = False 
        if self.rect.left < 0: self.right_facing = True

    # def check_collison_wit_radishes(self, radishes_groups)



class Radish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('radish_3.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))


# Create sprite groups
all_sprites = pygame.sprite.Group()

# Add the weasel & ra sprite to the group
weasel = Weasel()
radish = Radish(300,1000)
all_sprites.add(weasel, radish)
print(radish.rect.y)
print(weasel.rect.y)

# # Add radishes to the group in a 10x10 grid
# for i in range(GRID_SIZE):
#     for j in range(GRID_SIZE):
#         radish = Radish((i + 0.5) * RADISH_SIZE, SCREEN_HEIGHT - (j + 0.5) * RADISH_SIZE)
#         all_sprites.add(radish)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #Draw
    screen.blit(garden_surface, (0,0))
    screen.blit(text_surface, (200,300))
    weasel.move()
    all_sprites.draw(screen)

    # Update game logic here

    # Draw game elements here

    pygame.display.flip()
    clock.tick(60) # limits FPS to 60

pygame.quit()

