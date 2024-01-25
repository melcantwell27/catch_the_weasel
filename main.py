#pygame setup
import pygame
pygame.init()
import random

# Define some constants for screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

garden_surface = pygame.image.load('garden_of.png')
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
        radish_position = (random.randint(150, SCREEN_WIDTH), random.randint(150, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(midbottom = radish_position)

# Create sprite groups
all_sprites = pygame.sprite.Group()
radish_group = pygame.sprite.Group()

# Add the weasel & ra sprite to the group
weasel = Weasel()
radish = Radish()
all_sprites.add(weasel, radish)
radish_group.add(radish)

collision_detected = False #initialize collison flag
radish_count = 0 #initalize radish count

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

    # Check if any radishes have collided with the weasel
    if pygame.sprite.spritecollideany(weasel, radish_group):
        print("Collision detected!")
        collision_detected = True  # Set the flag to True to avoid continuous collisions 
        radish_count += 1
        print(radish_count)
        radish.kill()
        radish_group.empty()
        radish = Radish()
        radish_group.add(radish)
        all_sprites.add(radish)

    # all_sprites.update()

    #Draw
    screen.blit(garden_surface, (0,0))
    weasel.move()
    all_sprites.draw(screen)
    # print(all_sprites)

    # Update game logic here

    # Draw game elements here

    pygame.display.flip()
    clock.tick(60) # limits FPS to 60

pygame.quit()

