import pygame
import random
import sys

from pygame.font import FontType
from pygame.ftfont import Font

from logic import*
from data import *
from database import get_best, cur, insert_result
import json
import os

GAMERS_DB = get_best()


def draw_top_gamers():
    font_top = pygame.font.SysFont("simsum", 30 )
    font_gamer = pygame.font.SysFont("simsum", 24)
    text_head = font_top.render("Best tries: ", True, COLOR_TEXT)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s1 = "{0}{1}-{2}".format(index + 1, name, score)
        text_gamer = font_gamer.render(s1, True, COLOR_TEXT)
        screen.blit(text_gamer, (250, 30 + 25*index))


def Draw_Interface(score):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("comicsanssms", 70)
    font_score = pygame.font.SysFont("comicsanssms", 48)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render("{0}".format(score), True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    mas_print(mas)
    draw_top_gamers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render('{0}'.format(value), True, BLACK)
            w = column * SIZE_BLOCKS + (column + 1) * MARGIN
            h = row * SIZE_BLOCKS + (row + 1) * MARGIN + SIZE_BLOCKS
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCKS, SIZE_BLOCKS))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCKS - font_w) / 2
                text_y = h + (SIZE_BLOCKS - font_h) / 2
                screen.blit(text, (text_x, text_y))



def init_const():
    global score, mas
    score = 0
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

mas  = None
score = None
USERNAME = None

path = os.getcwd()
if 'data.txt' in os.listdir():
    with open('data.txt') as file:
        data = json.load(file)
        mas  = data['mas']
        score = data['score']
        USERNAME = data['user']
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_const()

TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

def draw_intro():
    img = pygame.image.load("2048_logo.svg.png")
    font = pygame.font.SysFont("stxingkai", 40)
    text_welcome = font.render("Welcome!", True, WHITE)
    name = 'INPUT YOUR NAME..'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'INPUT YOUR NAME..':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) >= 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break
        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img, [200, 200]), [10, 10])
        screen.blit(text_welcome, (220, 80))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)
    print(USERNAME)

def draw_game_over():
    global USERNAME, mas, score, GAMERS_DB
    img = pygame.image.load("2048_logo.svg.png")
    font_game_end = pygame.font.SysFont("simsum", 70)
    text_game_end = font_game_end.render("The end", True, WHITE)
    text_score = font_game_end.render('Your score is: {0}'.format(score), True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = "YOU WIN"
    else:
        text = 'Record {0}'.format(best_score)
    text_record = font_game_end.render(text, True, WHITE)
    insert_result(USERNAME, score)
    GAMERS_DB = get_best()
    make_desigion = False
    while not make_desigion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # restart with name
                    make_desigion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    # restart new gamer
                    USERNAME = None
                    make_desigion = True
                    init_const()
        screen.fill(BLACK)
        screen.blit(text_game_end, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img, [200, 200]), [10, 10])
        pygame.display.update()
    screen.fill(BLACK)

def save_game():
    data = {
        'user':USERNAME,
        'score':score,
        'mas':mas
    }
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def game_loop():
    global score, mas
    Draw_Interface(score)
    pygame.display.update()
    is_btn_click = False
    while zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta_l, delta_r, delta_d, delta_up = 0, 0, 0, 0
                if event.key == pygame.K_LEFT:
                    mas, delta_l, is_mas_move = move_left(mas)
                    is_btn_click = True
                elif event.key == pygame.K_RIGHT:
                    mas, delta_r = move_right(mas)
                    is_btn_click = True
                elif event.key == pygame.K_UP:
                    mas, delta_up = move_up(mas)
                    is_btn_click = True
                elif event.key == pygame.K_DOWN:
                    mas, delta_d = move_down(mas)
                    is_mas_move = True
                score += (delta_l + delta_r + delta_d + delta_up)
                if zero_in_mas(mas) and is_btn_click:
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                    print("Заполнен элемент номер: {0}".format(random_num))
                    is_btn_click = False
                Draw_Interface(score)
                pygame.display.update()

        print(USERNAME)


while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_game_over()