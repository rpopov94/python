import random
import pygame
import copy

def mas_print(mas):
    print('#' * 10)
    for row in mas:
        print(*row)
    print('#' * 10)


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_empty_list(mas):
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def zero_in_mas(mas):
    for i in mas:
        if 0 in i:
            return True
    return False


#mas_print(mas)
#print(get_empty_list(mas))


def move_left(mas):
    #save first station mas
    origin = copy.deepcopy(mas)
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j + 1)
                mas[i].append(0)
    return mas, delta, not origin == mas

def move_right(mas):
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row)!=4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j]*=2
                delta += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0, 0)
    return mas, delta

def move_up(mas):
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                delta += mas[i][j]
                column[i] *= 2
                column.pop(i+1)
                column.append(0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta

def move_down(mas):
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.insert(0,0)
        for i in range(3, 0, -1):
            if column[i] == column[i-1] and column[i] != 0:
                delta += mas[i][j]
                column[i] *= 2
                column.pop(i-1)
                column.insert(0,0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta

def can_move(mas):
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] or mas[i][j] == mas[i+1][j]:
                return True
    return mas[3][3] == mas[2][3] or mas[3][3] == mas[3][2]