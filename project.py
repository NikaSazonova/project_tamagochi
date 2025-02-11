import pygame
import os
import sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def exit():
    pygame.quit()
    sys.exit()


def start_menu():
    FPS = 60
    menu_text = ['«Главное меню»', 'Играть', 'Правила']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    text_coord = 110
    for line in menu_text:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                coor_in_menu = event.pos
                if 270 < coor_in_menu[1] < 350:
                    return 'Игра'
                elif 400 < coor_in_menu[1] < 470:
                    return 'Правила'
        pygame.display.flip()
        clock.tick(FPS)


def rules():
    FPS = 60
    rul = ['Правила']
    menu_bg = pygame.transform.scale(load_image('fon_menu.jpg'), (800, 650))
    screen.blit(menu_bg, (0, 0))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    text_coord = 110
    running = True
    for line in rul:
        string_rendered = font.render(line, True, (0, 0, 0))
        intro_rect = string_rendered.get_rect()
        text_coord += 50
        intro_rect.top = text_coord
        intro_rect.x = 50
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                main_screen()
        pygame.display.flip()
        clock.tick(FPS)


def main_screen():
    bg = load_image("cub.jpg")
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pass
        pygame.display.flip()
        screen.blit(bg, (0, 0))


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('calm.png')
        self.image_sleep = load_image('sleep.png')
        self.image_food = load_image('food.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 500
        self.speedx = 0
        self.speedy = 0

    def update(self, x1, y1):
        if 110 < x1 < 250 and 250 < y1 < 350:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 250 < x1 < 350 and 225 < y1 < 275:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 220 < x1 < 250 and 250 < y1 < 500:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 250 < x1 < 500 and 450 < y1 < 550:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 350 < x1 < 450 and 400 < y1 < 450:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 350 < x1 < 500 and 550 < y1 < 575:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 500 < x1 < 600 and 500 < y1 < 550:
            self.rect.centerx = x1
            self.rect.centery = y1
        elif 175 < x1 < 300 and 175 < y1 < 250 or \
                225 < x1 < 300 and 150 < y1 < 200:
            self.rect.centerx = x1
            self.rect.centery = y1


def main_play():
    FPS = 60
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    bg = load_image("cub.jpg")
    all_sprites = pygame.sprite.Group()
    player = Hero()
    all_sprites.add(player)

    pygame.mouse.set_visible(False)
    cursor_img = load_image('arrow.png')
    hand_cursor_img = load_image('hand.png')
    cursor_img_rect = cursor_img.get_rect()
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                all_sprites.update(x1, y1)
            all_sprites.draw(screen)
            cursor_img_rect.x, cursor_img_rect.y = pygame.mouse.get_pos()
            if 175 < cursor_img_rect.x < 300 and 175 < cursor_img_rect.y < 250 or \
                    225 < cursor_img_rect.x < 300 and 150 < cursor_img_rect.y < 200:
                screen.blit(hand_cursor_img, cursor_img_rect)
            elif 275 < cursor_img_rect.x < 350 and 350 < cursor_img_rect.y < 450:
                screen.blit(hand_cursor_img, cursor_img_rect)
            elif 450 < cursor_img_rect.x < 575 and 400 < cursor_img_rect.y < 475:
                screen.blit(hand_cursor_img, cursor_img_rect)
            else:
                screen.blit(cursor_img, cursor_img_rect)
            pygame.display.flip()
            screen.blit(bg, (0, 0))


if __name__ == '__main__':
    pygame.init()
    main_play()
    size = width, height = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Тамагочи')
    var = start_menu()
    if var == 'Игра':
        main_screen()
    elif var == 'Правила':
        rules()
    pygame.quit()