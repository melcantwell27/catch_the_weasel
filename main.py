#pygame setup
import pygame
pygame.init()
import random

# Define some constants for screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# GRID_SIZE = 10
# RADISH_SIZE = SCREEN_WIDTH // GRID_SIZE

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# pygame.display.set_caption("Whea Za Weasel Game")
test_font = pygame.font.Font(None, 100)

#timer to keep track of radish randomly generating
spawn_timer = pygame.time.get_ticks()

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
        self.speed_x = 4
        self.speed_y = 20

    def move(self):
        if self.right_facing:
            self.rect.x += self.speed_x
        else: 
            self.rect.x -= self.speed_x
        if self.rect.right > SCREEN_WIDTH: self.right_facing = False 
        if self.rect.left < 0: self.right_facing = True


class Radish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = radish_img.convert_alpha()
        self.rect = self.image.get_rect(midbottom = ((900, SCREEN_HEIGHT - 100)))

def generate_random_radish():
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    return Radish(x, y)

# Create sprite groups
all_sprites = pygame.sprite.Group()
radish_group = pygame.sprite.Group()

# Add the weasel & ra sprite to the group
weasel = Weasel()
radish = Radish()
all_sprites.add(weasel, radish)
radish_group.add(radish)

collision_detected = False #initialize collison flag

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                weasel.rect.y -= weasel.speed_y #Move up
            elif event.key == pygame.K_DOWN:
                weasel.rect.y += weasel.speed_y #Move down!! 

    current_time = pygame.time.get_ticks()
    if current_time - spawn_timer > 2000:
        # Generate and add a new random radish
        radish = generate_random_radish()
        all_sprites.add(radish)
        radish_group.add(radish)
        spawn_timer = current_time  # Reset the timer

    all_sprites.update()
# Check for collisions (trigger only once)
    if not collision_detected and weasel.rect.colliderect(radish.rect):
        print("Collision detected!")
        collision_detected = True  # Set the flag to True to avoid continuous collisions
        radish.kill()
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

