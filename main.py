#pygame setup
import pygame
pygame.init()
# pygame.mixer.init(driver='alsa')
import random

# Define constants for screen dimensions & set display
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#timer, duration
start_time = pygame.time.get_ticks()
game_duration_seconds = 27
initial_timer_seconds = game_duration_seconds
end_time = start_time + game_duration_seconds * 1000  # convert seconds to milliseconds
clock = pygame.time.Clock()


#load up & size background garden, weasel, & radish images
garden_surface = pygame.image.load('garden_of.png')
default_img_size = (150,150)
weasel_OG_img = pygame.image.load('weasel_180.png')
weasel_img = pygame.transform.scale(weasel_OG_img, default_img_size)
radish_OG_img = pygame.image.load('radish_dish.png')
radish_img = pygame.transform.scale(radish_OG_img, default_img_size)
radish_count = 0 #initalize radish count

#setting the rad_wav1 variable as the sound of the input .wav file
rad_wave1 = pygame.mixer.Sound('rad_wave1.wav')

# rad_waves = ['rad_wave1.wav', 'rad_wave2.wav']
# Load .wav files
# rad_waves = [
#     pygame.mixer.Sound(f'rad_wav{i}.wav') for i in range(1, 9)
# ]


class Weasel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = weasel_img.convert_alpha()
        self.rect = self.image.get_rect(midbottom = ((0, SCREEN_HEIGHT - 100)))
        self.right_facing = True
        self.speed_x = 8 + (radish_count^3)
        self.speed_y = 30 + 30*radish_count^2

    def move(self):
        #setting the x speed as + if the weasel is right-facing, and - if left-facing
        if self.right_facing:
            self.rect.x += self.speed_x
        else: 
            self.rect.x -= self.speed_x
        #if the weasel goes beyond the width of the screen, turn 'em round
        if self.rect.right > SCREEN_WIDTH: self.right_facing = False 
        if self.rect.left < 0: self.right_facing = True


class Radish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = radish_img.convert_alpha()
        #randomly sets radish (width, height) position
        radish_position = (random.randint(150, SCREEN_WIDTH), random.randint(250, SCREEN_HEIGHT))
        self.rect = self.image.get_rect(midbottom = radish_position)

# Create sprite groups
all_sprites = pygame.sprite.Group()
radish_group = pygame.sprite.Group()

# create weasel & radish instances & add them to sprites & radish groups
weasel = Weasel()
radish = Radish()
all_sprites.add(weasel, radish)
radish_group.add(radish)

collision_detected = False #initialize collison flag
#setting font of the "time running out font"
font = pygame.font.Font(None, 36)
warning_font = pygame.font.Font(None, 100)


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
        rad_wave1.play()
        # Play a random .wav file from rad_waves
        # random_wave = random.choice(rad_waves)
        # print(random_wave)
        # random_wave.play()
         # Update radish_count text
        radish.kill()
        radish_group.empty()
        radish = Radish()
        radish_group.add(radish)
        all_sprites.add(radish)

        # Check game duration
    current_time = pygame.time.get_ticks()
    elapsed_time_seconds = (current_time - start_time) / 1000  # convert milliseconds to seconds

    #Draw
    screen.blit(garden_surface, (0,0))

    #as time winds down ... show warning text & radish count in center screen
    if game_duration_seconds - elapsed_time_seconds <= 4:
            # Render the text surface
        warning_text = warning_font.render("Time's running out!", True, (255, 0, 0))  # red color
        screen.blit(warning_text, (290, 350))
        radish_count_text = font.render(f'Radish Count: {radish_count}', True, (0, 0, 255))
        screen.blit(radish_count_text, (490, 450))

    #as game over, close screen
    if elapsed_time_seconds >= game_duration_seconds:
        running = False
    weasel.move()
    all_sprites.draw(screen)

    #radish
    radish_count_text = font.render(f'Radish Count: {radish_count}', True, (0, 0, 0))
    screen.blit(radish_count_text, (1075, 40))  
   

    pygame.display.flip()
    clock.tick(60) # limits FPS to 60

# pygame.quit()

