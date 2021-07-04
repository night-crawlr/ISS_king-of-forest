import pygame
import random
import math

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1000, 1000))
# creating icon and name of game
pygame.display.set_caption("King Of Forest")
icon = pygame.image.load('forest.png')
pygame.display.set_icon(icon)
# Start
Start_X = 470
Start_Y = 800
Start_font = pygame.font.Font('freesansbold.ttf', 32)

# End
End_X = 780
End_Y = 100
End_font = pygame.font.Font('freesansbold.ttf', 32)

# Level
Level_X = 100
Level_Y = 50
Level_font = pygame.font.Font('freesansbold.ttf', 32)
Level = 1
check_1 = [0]*4
check_2 = [0]*4
check_3 = [0]*4
check_4 = [0]*4
check_5 = [0]*4
check_6 = [0]*4
present_state = 0

# Score of Player1
Score_1_X = 275
Score_1_Y = 50
Score_1_font = pygame.font.Font('freesansbold.ttf', 32)
score1 = 0

# Score of Player2
Score_2_X = 500
Score_2_Y = 50
Score_2_font = pygame.font.Font('freesansbold.ttf', 32)
score2 = 0

# Collision
collision = [0]*40
final_collision1 = 0
final_collision2 = 0

# GAME OVER
Game_over_font = pygame.font.Font('freesansbold.ttf', 64)
Game_over_X = 270
Game_over_Y = 250

# Winner
Winner_font = pygame.font.Font('freesansbold.ttf', 64)

# PLAYER1
player_1_img = pygame.image.load('warrior.png')
player_1_X = Start_X
player_1_Y = Start_Y
player_1_X_Rchange = 0
player_1_X_Lchange = 0
player_1_Y_Uchange = 0
player_1_Y_Dchange = 0

# PLAYER2
player_2_img = pygame.image.load('hunter.png')
player_2_X = End_X
player_2_Y = End_Y
player_2_X_Rchange = 0
player_2_X_Lchange = 0
player_2_Y_Uchange = 0
player_2_Y_Dchange = 0

# PLAYER
player_img = player_1_img
player_X = player_1_X
player_Y = player_1_Y
player_X_Rchange = 0
player_X_Lchange = 0
player_Y_Uchange = 0
player_Y_Dchange = 0

# Initial State
initial_state = "PLAYER1"
other_state = "PLAYER2"
state1 = initial_state
state2 = other_state
state = state1

# Boundaries
X_L_boundary = 30
X_R_boundary = 910
Y_D_boundary = 900
Y_U_boundary = 90
no_times = 5

displace = 50
# Trees
# 1 st row
trees_1_img = []
trees_1_X = []
trees_1_Y = []
no_of_trees = 4
for i in range(no_of_trees):
    trees_1_img.append(pygame.image.load('tree__1_.png'))
    if i < 2:
        trees_1_X.append(random.randint(30, Start_X - displace))
    if i == 2:
        trees_1_X.append(random.randint(Start_X + displace, End_X - displace))
    if i > 2:
        trees_1_X.append(random.randint(End_X + displace, 910 - displace))
    trees_1_Y.append(90)

# 2 nd row
trees_2_img = []
trees_2_X = []
trees_2_Y = []
no_of_trees = 4
for i in range(no_of_trees):
    trees_2_img.append(pygame.image.load('tree__1_.png'))
    if i < 2:
        trees_2_X.append(random.randint(30, Start_X - displace))
    if i == 2:
        trees_2_X.append(random.randint(Start_X + displace, End_X - displace))
    if i > 2:
        trees_2_X.append(random.randint(End_X + displace, 910 - displace))

    trees_2_Y.append(265)
# 3 rd row
trees_3_img = []
trees_3_X = []
trees_3_Y = []
no_of_trees = 4
for i in range(no_of_trees):
    trees_3_img.append(pygame.image.load('tree__1_.png'))
    if i < 2:
        trees_3_X.append(random.randint(30, Start_X - displace))
    if i == 2:
        trees_3_X.append(random.randint(Start_X + displace, End_X - displace))
    if i > 2:
        trees_3_X.append(random.randint(End_X + displace, 910 - displace))
    trees_3_Y.append(440)
# 4 th row
trees_4_img = []
trees_4_X = []
trees_4_Y = []
no_of_trees = 4
for i in range(no_of_trees):
    trees_4_img.append(pygame.image.load('tree__1_.png'))
    if i < 2:
        trees_4_X.append(random.randint(30, Start_X - displace))
    if i == 2:
        trees_4_X.append(random.randint(Start_X + displace, End_X - displace))
    if i > 2:
        trees_4_X.append(random.randint(End_X + displace, 910 - displace))
    trees_4_Y.append(615)
# 5 th row
trees_5_img = []
trees_5_X = []
trees_5_Y = []
no_of_trees = 4
for i in range(no_of_trees):
    trees_5_img.append(pygame.image.load('tree__1_.png'))
    if i <= 2:
        trees_5_X.append(random.randint(30, Start_X - displace))
    # if i == 2:
    #   trees_5_X.append(random.randint(Start_X + displace, End_X - displace))
    if i > 2:
        trees_5_X.append(random.randint(End_X + displace, 910 - displace))
    trees_5_Y.append(790)

# Snakes
snakes_1_img = []
snakes_1_X = []
snakes_1_Y = []
snakes_1_X_change = []
no_of_snakes = 4
for i in range(no_of_snakes):
    snakes_1_img.append(pygame.image.load('snake.png'))
    snakes_1_X.append(170*i + 300)
    snakes_1_Y.append(700)
    snakes_1_X_change.append(0.5)
collision_snakes = 0

# Spiders
spiders_1_img = []
spiders_1_X = []
spiders_1_Y = []
spiders_1_X_change = []
no_of_spiders = 4
for i in range(no_of_spiders):
    spiders_1_img.append(pygame.image.load('spider.png'))
    spiders_1_X.append(170*i + 40)
    spiders_1_Y.append(530)
    spiders_1_X_change.append(0.5)
collision_spiders = 0

# Lions
lions_1_img = []
lions_1_X = []
lions_1_Y = []
lions_1_X_change = []
no_of_lions = 4
for i in range(no_of_lions):
    lions_1_img.append(pygame.image.load('lion.png'))
    lions_1_X.append(170*i + 400)
    lions_1_Y.append(355)
    lions_1_X_change.append(0.5)
collision_lions = 0

# Dinosaurs
dinosaurs_1_img = []
dinosaurs_1_X = []
dinosaurs_1_Y = []
dinosaurs_1_X_change = []
no_of_dinosaurs = 4
for i in range(no_of_dinosaurs):
    dinosaurs_1_img.append(pygame.image.load('dinosaur.png'))
    dinosaurs_1_X.append(170*i + 40)
    dinosaurs_1_Y.append(185)
    dinosaurs_1_X_change.append(0.5)
collision_dinosaurs = 0

# Game over + scores


def show_game_over():
    score_1 = Score_1_font.render("PLAYER1:" + str(score1), True, (255, 255, 255))
    score_2 = Score_2_font.render("PLAYER2:" + str(score2), True, (255, 255, 255))
    final = Game_over_font.render("GAMEOVER....", True, (255, 255, 255))
    if score1 > score2:
        winner = Winner_font.render("PLAYER1 won the game", True, (255, 255, 255))
    elif score2 > score1:
        winner = Winner_font.render("PLAYER2 won the game", True, (255, 255, 255))
    else:
        winner = Winner_font.render("GAME DRAW .....", True, (255, 255, 255))

    screen.blit(score_1, (Score_1_X + 75 + 30, Score_1_Y + 300))
    screen.blit(score_2, (Score_2_X - 150 + 30, Score_2_Y + 350))
    screen.blit(final, (Game_over_X, Game_over_Y))
    screen.blit(winner, (Game_over_X - 80, Game_over_Y + 300))

# Shows scores


def show_scores():
    global Level
    global present_state
    Level = int(present_state/2) + 1
    score_1 = Score_1_font.render("PLAYER1:" + str(score1), True, (255, 255, 255))
    score_2 = Score_2_font.render("PLAYER2:" + str(score2), True, (255, 255, 255))
    level = Level_font.render("LEVEL:" + str(Level), True, (255, 255, 255))
    screen.blit(score_1, (Score_1_X, Score_1_Y))
    screen.blit(score_2, (Score_2_X, Score_2_Y))
    screen.blit(level, (Level_X, Level_Y))

# Shows Start and End


def show_star_end_1():
    start = Start_font.render("START", True, (255, 255, 255))
    end = End_font.render("END", True, (255, 255, 255))
    screen.blit(start, (Start_X, Start_Y + 70))
    screen.blit(end, (End_X, End_Y - 50))


# player_1 makes display of player_1 on screen


def player(x, y):
    if state == "PLAYER1":
        screen.blit(player_1_img, (x, y))
    if state == "PLAYER2":
        screen.blit(player_2_img, (x, y))


# Snakes are displayed


def snake(x, y, k):
    screen.blit(snakes_1_img[k], (x, y))


# Spiders are displayed


def spider(x, y, k):
    screen.blit(spiders_1_img[k], (x, y))


# Lions are displayed


def lion(x, y, k):
    screen.blit(lions_1_img[k], (x, y))


# Dinosaurs are displayed


def dinosaur(x, y, k):
    screen.blit(dinosaurs_1_img[k], (x, y))


# trees are displayed


def tree_1(x, y, k):
    screen.blit(trees_1_img[k], (x, y))


def tree_2(x, y, k):
    screen.blit(trees_2_img[k], (x, y))


def tree_3(x, y, k):
    screen.blit(trees_3_img[k], (x, y))


def tree_4(x, y, k):
    screen.blit(trees_4_img[k], (x, y))


def tree_5(x, y, k):
    screen.blit(trees_5_img[k], (x, y))


def trees():
    for m in range(4):
        tree_1(trees_1_X[m], trees_1_Y[m], m)
    for m in range(4):
        tree_2(trees_2_X[m], trees_2_Y[m], m)
    for m in range(4):
        tree_3(trees_3_X[m], trees_3_Y[m], m)
    for m in range(4):
        tree_4(trees_4_X[m], trees_4_Y[m], m)
    for m in range(4):
        tree_5(trees_5_X[m], trees_5_Y[m], m)


# collision detection


def iscollision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    if distance < 50:
        return 1
    return 0
# changing state


def change_state():
    global present_state
    global state
    global player_X
    global player_Y
    global player_img
    global player_X_Lchange
    global player_X_Rchange
    global player_Y_Dchange
    global player_Y_Uchange
    present_state += 1
    if state == "PLAYER2":
        state = "PLAYER1"
        player_img = player_1_img
        player_X = player_1_X
        player_Y = player_1_Y
        player_X_Rchange = 0
        player_X_Lchange = 0
        player_Y_Uchange = 0
        player_Y_Dchange = 0
    else:
        state = "PLAYER2"
        player_img = player_2_img
        player_X = player_2_X
        player_Y = player_2_Y
        player_X_Rchange = 0
        player_X_Lchange = 0
        player_Y_Uchange = 0
        player_Y_Dchange = 0
    # for h in range(36):
    #    collision[h] = 0
    for a in range(4):
        check_1[a] = 0
        check_2[a] = 0
        check_3[a] = 0
        check_4[a] = 0
        check_5[a] = 0
        check_6[a] = 0
# GAME_OVER


functioning = True


def game_over():
    global functioning
    functioning1 = True
    while functioning1:
        screen.fill((0, 204, 0))
        show_game_over()
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                functioning1 = False
                functioning = False
        pygame.display.update()


if state == "PLAYER1":
    player_img = player_1_img
    player_X = player_1_X
    player_Y = player_1_Y
    player_X_Rchange = 0
    player_X_Lchange = 0
    player_Y_Uchange = 0
    player_Y_Dchange = 0
if state == "PLAYER2":
    player_img = player_2_img
    player_X = player_2_X
    player_Y = player_2_Y
    player_X_Rchange = 0
    player_X_Lchange = 0
    player_Y_Uchange = 0
    player_Y_Dchange = 0


# Game  Loop Begins

while functioning:

    if Level == 4:
        game_over()

    # Decide the player based on state

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            functioning = False
        # for checking of any key is pressed or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_X_Lchange = -0.8
            if event.key == pygame.K_RIGHT:
                player_X_Rchange = 0.8
            if event.key == pygame.K_UP:
                player_Y_Uchange = -0.8
            if event.key == pygame.K_DOWN:
                player_Y_Dchange = 0.8

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_X_Lchange = 0
            if event.key == pygame.K_RIGHT:
                player_X_Rchange = 0
            if event.key == pygame.K_UP:
                player_Y_Uchange = 0
            if event.key == pygame.K_DOWN:
                player_Y_Dchange = 0
    if functioning:
        screen.fill((0, 204, 0))
        Land = pygame.Surface((X_R_boundary - X_L_boundary, 75))
        Land.fill((102, 51, 0))
        i = 0
        for i in range(5):
            screen.blit(Land, (X_L_boundary, Y_U_boundary + i * 175))

        player_X += player_X_Rchange
        player_X += player_X_Lchange
        player_Y += player_Y_Uchange
        player_Y += player_Y_Dchange

        for i in range(4):
            snakes_1_X[i] += snakes_1_X_change[i] + Level/4
            spiders_1_X[i] += spiders_1_X_change[i] + Level/4
            lions_1_X[i] += lions_1_X_change[i] + Level/4
            dinosaurs_1_X[i] += dinosaurs_1_X_change[i] + Level/4

        if player_X <= X_L_boundary:
            player_X = X_L_boundary
        if player_X >= X_R_boundary:
            player_X = X_R_boundary
        if player_Y >= Y_D_boundary - 100:
            player_Y = Y_D_boundary - 100
        if player_Y <= Y_U_boundary:
            player_Y = Y_U_boundary
        player(player_X, player_Y)
        for i in range(4):

            if snakes_1_X[i] >= X_R_boundary - 50:
                snakes_1_X[i] = 13

            if spiders_1_X[i] >= X_R_boundary - 50:
                spiders_1_X[i] = 13

            if lions_1_X[i] >= X_R_boundary - 50:
                lions_1_X[i] = 13

            if dinosaurs_1_X[i] >= X_R_boundary - 50:
                dinosaurs_1_X[i] = 13
        for i in range(4):
            collision[i] = iscollision(snakes_1_X[i], snakes_1_Y[i], player_X, player_Y)
            collision_snakes += collision[i]
            final_collision1 += collision_snakes
        for i in range(4):
            collision[i + 4] = iscollision(spiders_1_X[i], spiders_1_Y[i], player_X, player_Y)
            collision_spiders += collision[i + 4]
            final_collision1 += collision_spiders
        for i in range(4):
            collision[i + 8] = iscollision(lions_1_X[i], lions_1_Y[i], player_X, player_Y)
            collision_lions += collision[i + 8]
            final_collision1 += collision_lions
        for i in range(4):
            collision[i + 12] = iscollision(dinosaurs_1_X[i], dinosaurs_1_Y[i], player_X, player_Y)
            collision_dinosaurs += collision[i + 12]
            final_collision1 += collision_dinosaurs
        for i in range(4):
            collision[i + 16] = iscollision(trees_1_X[i], trees_1_Y[i], player_X, player_Y)
            final_collision1 += collision[i + 16]
        for i in range(4):
            collision[i + 20] = iscollision(trees_2_X[i], trees_2_Y[i], player_X, player_Y)
            final_collision1 += collision[i + 20]
        for i in range(4):
            collision[i + 24] = iscollision(trees_3_X[i], trees_3_Y[i], player_X, player_Y)
            final_collision1 += collision[i + 24]
        for i in range(4):
            collision[i + 28] = iscollision(trees_4_X[i], trees_4_Y[i], player_X, player_Y)
            final_collision1 += collision[i + 28]
        for i in range(4):
            collision[i+36] = iscollision(trees_5_X[i], trees_5_Y[i], player_X, player_Y)
            final_collision1 += collision[i + 36]
        if state == "PLAYER1":
            collision_End = iscollision(End_X, End_Y, player_X, player_Y)
            if final_collision1 >= 1:
                change_state()
            else:
                if collision_End and check_1[3] == 0 and check_2[3] == 0 and check_3[3] == 0:
                    score1 += 10
                    if Level == 1:
                        check_1[3] = 1
                    elif Level == 2:
                        check_2[3] = 1
                    elif Level == 3:
                        check_3[3] = 1
                    change_state()
                elif player_Y < Y_U_boundary + 175 + 75 and check_1[2] == 0 and check_2[2] == 0 and check_3[2] == 0:
                    score1 += 10
                    if Level == 1:
                        check_1[2] = 1
                    elif Level == 2:
                        check_2[2] = 1
                    elif Level == 3:
                        check_3[2] = 1
                elif player_Y < Y_U_boundary + 350 + 75 and check_1[1] == 0 and check_2[1] == 0 and check_3[1] == 0:
                    score1 += 10
                    if Level == 1:
                        check_1[1] = 1
                    elif Level == 2:
                        check_2[1] = 1
                    elif Level == 3:
                        check_3[1] = 1
                elif player_Y < Y_U_boundary + 525 + 75 and check_1[0] == 0 and check_2[0] == 0 and check_3[0] == 0:
                    score1 += 10
                    if Level == 1:
                        check_1[0] = 1
                    elif Level == 2:
                        check_2[0] = 1
                    elif Level == 3:
                        check_3[0] = 1
        else:
            collision_Start = iscollision(Start_X, Start_Y, player_X, player_Y)
            if final_collision1 >= 1:
                change_state()
            else:
                if collision_Start and check_4[3] == 0 and check_5[3] == 0 and check_6[3] == 0:
                    score2 += 10
                    if Level == 1:
                        check_4[3] = 1
                    elif Level == 2:
                        check_5[3] = 1
                    elif Level == 3:
                        check_6[3] = 1
                    change_state()
                elif player_Y > Y_U_boundary + (1 * 175) and check_4[2] == 0 and check_5[2] == 0 and check_6[2] == 0:
                    score2 += 10
                    if Level == 1:
                        check_4[2] = 1
                    elif Level == 2:
                        check_5[2] = 1
                    elif Level == 3:
                        check_6[2] = 1
                elif player_Y > Y_U_boundary + (2 * 175) and check_4[1] == 0 and check_5[1] == 0 and check_6[1] == 0:
                    score2 += 10
                    if Level == 1:
                        check_4[1] = 1
                    elif Level == 2:
                        check_5[1] = 1
                    elif Level == 3:
                        check_6[1] = 1
                elif player_Y > Y_U_boundary + (3 * 175) and check_4[0] == 0 and check_5[0] == 0 and check_6[0] == 0:
                    score2 += 10
                    if Level == 1:
                        check_4[0] = 1
                    elif Level == 2:
                        check_5[0] = 1
                    elif Level == 3:
                        check_6[0] = 1
        for i in range(4):
            snake(snakes_1_X[i], snakes_1_Y[i], i)
            spider(spiders_1_X[i], spiders_1_Y[i], i)
            lion(lions_1_X[i], lions_1_Y[i], i)
            dinosaur(dinosaurs_1_X[i], dinosaurs_1_Y[i], i)
        trees()
        show_star_end_1()
        show_scores()
        final_collision1 = 0
        collision_snakes = 0
        collision_spiders = 0
        collision_dinosaurs = 0
        collision_lions = 0
    pygame.display.update()
