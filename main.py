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
default_img_size = (150,150)
weasel_OG_img = pygame.image.load('weasel_180.png')
weasel_img = pygame.transform.scale(weasel_OG_img, default_img_size)
radish_OG_img = pygame.image.load('radish_dish.png')
radish_img = pygame.transform.scale(radish_OG_img, default_img_size)


class Weasel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = weasel_img.convert_alpha()
        self.rect = self.image.get_rect(midbottom = ((0, SCREEN_HEIGHT - 100)))
        self.right_facing = True

    def move(self):
        if self.right_facing:
            self.rect.x +=4
        else: 
            self.rect.x -= 4
        if self.rect.right > SCREEN_WIDTH: self.right_facing = False 
        if self.rect.left < 0: self.right_facing = True


class Radish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = radish_img.convert_alpha()
        self.rect = self.image.get_rect(midbottom = ((100, SCREEN_HEIGHT - 100)))



# Create sprite groups
all_sprites = pygame.sprite.Group()

# Add the weasel & ra sprite to the group
weasel = Weasel()
radish = Radish()
all_sprites.add(weasel, radish)
print(radish.rect.y)
print(weasel.rect.y)
print(radish.rect.midbottom[1])
print(weasel.rect.midbottom[1])

# # Add radishes to the group in a 10x10 grid
# for i in range(GRID_SIZE):
#     for j in range(GRID_SIZE):
#         radish = Radish((i + 0.5) * RADISH_SIZE, SCREEN_HEIGHT - (j + 0.5) * RADISH_SIZE)
#         all_sprites.add(radish)

collision_detected = False #initialize collison flag
# Print dimensions of the weasel's & radish's rect
print("Weasel Rect Dimensions:", weasel.rect.width, "x", weasel.rect.height)
print("Radish Rect Dimensions:", radish.rect.width, "x", radish.rect.height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

# Check for collisions (trigger only once)
    if not collision_detected and weasel.rect.colliderect(radish.rect):
        print("Collision detected!")
        collision_detected = True  # Set the flag to True to avoid continuous collisions

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

