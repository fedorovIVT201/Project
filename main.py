import pygame
import random

WIDTH = 1000
HEIGHT = 750
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

bg_img = pygame.image.load('bg.png')
bg_sky = pygame.image.load('bg_skye.png')
bg_clouds = pygame.image.load('bg_clouds.png')
bg_forest = pygame.image.load('bg_forest.png')
bg_sun = pygame.image.load('bg_sun.png')
bg_mountains = pygame.image.load('bg_mountains.png')
bg_tree = pygame.image.load('bg_tree.png')
player_img_default = pygame.image.load('p1_jump(right).png')
player_img_left = pygame.image.load('p1_jump(left).png')
bg = pygame.transform.scale(bg_img, (1000, 750))
bg_change_next = False
lvl = 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img_default
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2.3)
        self.speedx = 0

    def update(self):
        global lvl
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.image = player_img_left
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.image = player_img_default
            self.speedx = 8
        if keystate[pygame.K_LEFT] and keystate[pygame.K_LSHIFT]:
            self.image = player_img_left
            self.speedx = -12
        if keystate[pygame.K_RIGHT] and keystate[pygame.K_LSHIFT]:
            self.image = player_img_default
            self.speedx = 12
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.center = (40, HEIGHT / 2.3)
            lvl += 1
        if self.rect.left < 0:
            self.rect.center = (970, HEIGHT / 2.3)
            lvl -= 1


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


# Спрайты
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

bg_move = 0
bg_sky_move = 0  # 0
bg_clouds_move = 0  # 4
bg_forest_move = 0  # 2
bg_sun_move = 0  # 5
bg_mountains_move = 0  # 3
bg_tree_move = 0  # 1

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False)
    # if hits:
    #     running = False
    # Отрисовка
    # background
    # screen.blit(bg_sky,(0,0))
    screen.blit(bg_sky, (0, 0))

    # screen.blit(bg_sun, (bg_sun_move, 0))
    # screen.blit(bg_clouds, (bg_clouds_move, 0))
    # screen.blit(bg_mountains, (bg_mountains_move, 0))
    # screen.blit(bg_forest, (bg_forest_move, 0))
    # screen.blit(bg_tree, (bg_tree_move, 0))

    # screen.blit(bg_sun, (1000 + bg_sun_move, 0))
    # screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
    # screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
    # screen.blit(bg_forest, (1000 + bg_forest_move, 0))
    # screen.blit(bg_tree, (1000 + bg_tree_move, 0))

    # if bg_change_next:
    #     screen.blit(bg_clouds, (bg_clouds_move, 0))
    #     screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))

    if lvl == 0:
        screen.blit(bg_sun, (bg_sun_move, 0))
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
    if lvl == 1:
        screen.blit(bg_sun, (bg_sun_move, 0))
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_tree, (bg_tree_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
    if lvl == 2:
        screen.blit(bg_sun, (bg_sun_move, 0))
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_tree, (bg_tree_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
        screen.blit(bg_clouds, (bg_clouds_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
    if lvl == 3:
        screen.blit(bg_sun, (bg_sun_move, 0))
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_forest, (bg_forest_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
    if lvl == 4:
        screen.blit(bg_sun, (bg_sun_move, 0))
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_clouds, (bg_clouds_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
        screen.blit(bg_forest, (bg_forest_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
    if lvl == 5:
        screen.blit(bg_sun, (bg_sun_move, 0))
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_mountains, (bg_mountains_move, 0))
        screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
        screen.blit(bg_forest, (bg_forest_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
    if bg_sun_move == -1000:
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
        screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
        bg_sun_move = 0
    if bg_clouds_move == -1000:
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
        screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
        bg_clouds_move = 0
    if bg_mountains_move == -1000:
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
        screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
        bg_mountains_move = 0
    if bg_forest_move == -1000:
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
        screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
        bg_forest_move = 0
    if bg_tree_move == -1000:
        screen.blit(bg_sun, (1000 + bg_sun_move, 0))
        screen.blit(bg_clouds, (1000 + bg_clouds_move, 0))
        screen.blit(bg_mountains, (1000 + bg_mountains_move, 0))
        screen.blit(bg_forest, (1000 + bg_forest_move, 0))
        screen.blit(bg_tree, (1000 + bg_tree_move, 0))
        bg_tree_move = 0

    bg_tree_move -= 1
    if bg_move % 2 == 0:
        bg_sun_move -= 1
    if bg_move % 3 == 0:
        bg_forest_move -= 1
    if bg_move % 4 == 0:
        bg_mountains_move -= 1
    if bg_move % 5 == 0:
        bg_clouds_move -= 1
    bg_move -= 1

    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
