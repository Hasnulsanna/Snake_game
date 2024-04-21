# import random
# import pygame
# import sys
# from pygame.locals import *
# from settingsSnakeFun import *

# MEDIUM_OBSTACLES = [(10, 10), (15, 15), (20, 20),(5,5),(7,20),(7,21),(25,15),(26,15),(23,10),(22,11),(4,15),(5,16),(22,5)]
# HARD_OBSTACLES = [(5, 5),(5, 6),(5, 7),(6, 5),(7, 5),(10, 11),(10, 12),(10, 13), (10, 10), (11, 10),(12, 10),(13, 10),(15, 15), (15, 16),(15, 17),(15, 18),(20, 5), (21, 5),(22, 5),(23, 5),(5, 19),(5, 18),(5, 27),(5, 20),(6, 20),(7, 20),(20, 20),(21, 20),(25, 13),(25, 12),(25, 14),(25, 11),(20,3),(21,3),(22,3),(23,3)]


# def set_speed(selected_level):
#     if selected_level == "EASY":
#         return 3
#     elif selected_level == "MEDIUM":
#         return 5
#     elif selected_level == "HARD":
#         return 6
	
# def main(SCREEN):
#     global CLOCK, FONT, level, FPS
#     pygame.init()
#     CLOCK = pygame.time.Clock()
#     FONT = pygame.font.Font('freesansbold.ttf', 18)
#     pygame.display.set_caption('Snake Game')

#     level = showLevelSelection(SCREEN)  # Determine level first
#     FPS = set_speed(level)  # Set FPS based on the chosen level
#     showStartScreen(SCREEN, FPS)  # Pass FPS as a parameter
#     while True:
#         pygame.mixer.music.play(-1, 0.0)
#         runGame()
#         pygame.mixer.music.stop()
#         showGameOverScreen()

# # The rest of your code remains unchanged



# def showLevelSelection(screen):
#     # Add interface for level selection
#     while True:
#         screen.fill(BGCOLOR)
#         drawLevelSelection(screen)
#         pygame.display.update()
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 terminate()
#             elif event.type == KEYDOWN:
#                 if event.key == K_1:
#                     return "EASY"
#                 elif event.key == K_2:
#                     return "MEDIUM"
#                 elif event.key == K_3:
#                     return "HARD"


# def drawLevelSelection(screen):
#     # Draw level selection options
#     font = pygame.font.Font('freesansbold.ttf', 36)
#     titlefont = pygame.font.Font('freesansbold.ttf', 50)
#     # text0 = titlefont.render('PYGLIDE.', True, DARKGREEN)
#     # textRect0 = text0.get_rect()
#     # textRect0.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 7)
#     text1 = font.render('Select Level:', True, BLACK)
#     textRect1 = text1.get_rect()
#     textRect1.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 3)
#     text2 = font.render('1. Easy', True, BLACK)
#     textRect2 = text2.get_rect()
#     textRect2.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)
#     text3 = font.render('2. Medium', True, BLACK)
#     textRect3 = text3.get_rect()
#     textRect3.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2 + 50)
#     text4 = font.render('3. Hard', True, BLACK)
#     textRect4 = text4.get_rect()
#     textRect4.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2 + 100)
#     # screen.blit(text0, textRect0)
#     screen.blit(text1, textRect1)
#     screen.blit(text2, textRect2)
#     screen.blit(text3, textRect3)
#     screen.blit(text4, textRect4)


# def runGame():
# 	#Set a random starting point
# 	startx = random.randint(5, CELLWIDTH - 6)
# 	starty = random.randint(5, CELLHEIGHT - 6)
# 	global wormCoords
# 	wormCoords = [{'x' : startx, 'y' : starty}, {'x': startx - 1, 'y':starty}, {'x':startx - 2, 'y':starty}]
# 	direction = RIGHT

# 	apple = getRandomLocation()
# 	if level == "MEDIUM":
# 		obstacles = MEDIUM_OBSTACLES
# 	elif level == "HARD":
# 		obstacles = HARD_OBSTACLES
# 	else:
# 		obstacles = []

# 	while True:
# 		for event in pygame.event.get():
# 			if event.type == QUIT:
# 				terminate()
# 			elif event.type == KEYDOWN:
# 				if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
# 					direction = LEFT
# 				elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
# 					direction = RIGHT
# 				elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
# 					direction = UP
# 				elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
# 					direction = DOWN
# 				elif event.key == K_ESCAPE:
# 					terminate()
# #Collision Detection
# 		#Check Collision with edges
# 		if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
# 			return
# 		#Check Collision with snake's body
# 		for wormBody in wormCoords[1:]:
# 			if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
# 				return
# 		# Check Collision with obstacles
# 		for obstacle in obstacles:
# 			if (
#        			wormCoords[HEAD]["x"] == obstacle[0]
#         		and wormCoords[HEAD]["y"] == obstacle[1]
#     		):	
# 				return 
# 		#Check Collision with Apple
# 		if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
# 			APPLEEATSOUND.play()
# 			apple = getRandomLocation()
# 		else:
# 			del wormCoords[-1]

		 
# #Moving the Snake
# 		if direction == UP:
# 			newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
# 		elif direction == DOWN:
# 			newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
# 		elif direction == RIGHT:
# 			newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
# 		elif direction == LEFT:
# 			newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
# 		wormCoords.insert(0, newHead)

# #Drawing the Screen
# 		SCREEN.fill(BGCOLOR)
# 		drawGrid()
# 		drawWorm(wormCoords)
# 		drawApple(apple)
# 		drawObstacles(obstacles)
# 		drawScore((len(wormCoords) - 3) * 5)
# 		pygame.display.update()
# 		CLOCK.tick(FPS)

# def getTotalScore():
# 	return ((len(wormCoords) - 3) * 5)

# def drawPressKeyMsg():
# 	pressKeyText = FONT.render('Press A Key To Play', True, BLUE)
# 	pressKeyRect = pressKeyText.get_rect()
# 	pressKeyRect.center = (WINDOWWIDTH - 200, WINDOWHEIGHT - 100)
# 	SCREEN.blit(pressKeyText, pressKeyRect)


# def checkForKeyPress():
# 	if len(pygame.event.get(QUIT)) > 0:
# 		terminate()

# 	keyUpEvents = pygame.event.get(KEYUP)
# 	if len(keyUpEvents) == 0:
# 		return None
# 	if keyUpEvents[0].key == K_ESCAPE:
# 		terminate()
# 	return keyUpEvents[0].key

# def showStartScreen(SCREEN,FPS):
# 	titlefont = pygame.font.Font('freesansbold.ttf', 100)
# 	titleText = titlefont.render('PYGLIDE.', True, DARKGREEN)
# 	while True:
# 		SCREEN.fill(BGCOLOR)
# 		titleTextRect = titleText.get_rect()
# 		titleTextRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
# 		SCREEN.blit(titleText, titleTextRect)

# 		drawPressKeyMsg()
# 		if checkForKeyPress():
# 			pygame.event.get()
# 			return
# 		pygame.display.update()
# 		CLOCK.tick(FPS)

# def terminate():
# 	pygame.quit()
# 	sys.exit()

# def getRandomLocation():
# 	return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}
# def showGameOverScreen():
#     gameOverFont = pygame.font.Font('freesansbold.ttf', 75)
#     gameOverText = gameOverFont.render('Game Over', True, RED)
#     gameOverRect = gameOverText.get_rect()
#     total_score = getTotalScore()
#     high_scores = loadHighScores()
#     new_highscore = False
    
#     if level == "EASY":
#         if total_score > high_scores["EASY"]:
#             high_scores["EASY"] = total_score
#             new_highscore = True
#     elif level == "MEDIUM":
#         if total_score > high_scores["MEDIUM"]:
#             high_scores["MEDIUM"] = total_score
#             new_highscore = True
#     elif level == "HARD":
#         if total_score > high_scores["HARD"]:
#             high_scores["HARD"] = total_score
#             new_highscore = True

#     saveHighScores(high_scores)

#     high_score_text = ""
#     if level == "EASY":
#         high_score_text = f'High Score - Easy: {high_scores["EASY"]} '
#     elif level == "MEDIUM":
#         high_score_text = f'High Score -  Medium: {high_scores["MEDIUM"]}'
#     elif level == "HARD":
#         high_score_text = f'High Score - Hard: {high_scores["HARD"]}'

#     highScoreFont = pygame.font.Font('freesansbold.ttf', 30)
#     highScoreText = highScoreFont.render(high_score_text, True, BLACK)
#     highScoreRect = highScoreText.get_rect()
#     highScoreRect.midtop = (WINDOWWIDTH/2, 300)

#     totalScoreFont = pygame.font.Font('freesansbold.ttf', 35)
#     totalScoreText = totalScoreFont.render(' Total Score: %s' % (total_score), True, BLACK)
#     totalScoreRect = totalScoreText.get_rect()
#     totalScoreRect.midtop = (WINDOWWIDTH/2, 150)
#     gameOverRect.midtop = (WINDOWWIDTH/2, 30)

#     SCREEN.fill(BGCOLOR)
#     SCREEN.blit(gameOverText, gameOverRect)
#     SCREEN.blit(totalScoreText, totalScoreRect)
#     SCREEN.blit(highScoreText, highScoreRect)

#     # Display new high score message if applicable
#     if new_highscore:
#         newHighScoreFont = pygame.font.Font('freesansbold.ttf', 30)
#         newHighScoreText = newHighScoreFont.render('Congratulations New highscore!', True, BLUE)
#         newHighScoreRect = newHighScoreText.get_rect()
#         newHighScoreRect.midtop = (WINDOWWIDTH/2, 250)
#         SCREEN.blit(newHighScoreText, newHighScoreRect)

#     drawPressKeyMsg()
#     pygame.display.update()
#     pygame.time.wait(1000)

#     while True:
#         if checkForKeyPress():
#             pygame.event.get()
#             return

# # def showGameOverScreen():
# # 	gameOverFont = pygame.font.Font('freesansbold.ttf', 80)
# # 	gameOverText = gameOverFont.render('Game Over', True, RED)
# # 	gameOverRect = gameOverText.get_rect()
# # 	totalscoreFont = pygame.font.Font('freesansbold.ttf', 40)
# # 	total_score = getTotalScore()
# # 	high_scores = loadHighScores() 
# # 	if level == "EASY":
# # 		if total_score > high_scores["EASY"]:
# # 			high_scores["EASY"] = total_score
# # 	elif level == "MEDIUM":
# # 		if total_score > high_scores["MEDIUM"]:
# # 			high_scores["MEDIUM"] = total_score
# # 	elif level == "HARD":
# # 		if total_score > high_scores["HARD"]:
# # 			high_scores["HARD"] = total_score

# # 	saveHighScores(high_scores)
# # 	# Render high scores text
# # 	if level == "EASY":
# # 		high_score_text = f'High Score - Easy: {high_scores["EASY"]} '
# # 	elif level == "MEDIUM":
# # 		high_score_text = f'High Score -  Medium: {high_scores["MEDIUM"]}'
# # 	elif level == "HARD":
# # 		high_score_text = f'High Score - Hard: {high_scores["HARD"]}'
# # 	highScoreFont = pygame.font.Font('freesansbold.ttf', 30)
# # 	highScoreText = highScoreFont.render(high_score_text, True, BLACK)
# # 	highScoreRect = highScoreText.get_rect()
# # 	highScoreRect.midtop = (WINDOWWIDTH/2, 250)


# # 	totalscoreText = totalscoreFont.render(' Total Score: %s' % (total_score), True, BLACK)
# # 	totalscoreRect = totalscoreText.get_rect()
# # 	totalscoreRect.midtop = (WINDOWWIDTH/2, 150)
# # 	gameOverRect.midtop = (WINDOWWIDTH/2, 30)

# # 	SCREEN.fill(BGCOLOR)
# # 	SCREEN.blit(gameOverText, gameOverRect)
# # 	SCREEN.blit(highScoreText, highScoreRect)
# # 	SCREEN.blit(totalscoreText, totalscoreRect)
# # 	drawPressKeyMsg()
# # 	pygame.display.update()
# # 	pygame.time.wait(1000)
# # 	checkForKeyPress()

# # 	while True:
# # 		if checkForKeyPress():
# # 			pygame.event.get()
# # 			return

# def drawScore(score):
# 	scoreText = FONT.render('Score: %s' % (score), True, BLACK)
# 	scoreRect = scoreText.get_rect()
# 	scoreRect.center = (WINDOWWIDTH - 100, 30)
# 	SCREEN.blit(scoreText, scoreRect)

# def drawWorm(wormCoords):
# 	x = wormCoords[HEAD]['x'] * CELLSIZE
# 	y = wormCoords[HEAD]['y'] * CELLSIZE
# 	wormHeadRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
# 	pygame.draw.rect(SCREEN, YELLOW, wormHeadRect)

# 	for coord in wormCoords[1:]:
# 		x = coord['x'] * CELLSIZE
# 		y = coord['y'] * CELLSIZE
# 		wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
# 		pygame.draw.rect(SCREEN, GREEN, wormSegmentRect)

# def drawApple(coord):
# 	x = coord['x'] * CELLSIZE + CELLSIZE // 2  # Adjust x-coordinate to center of cell
# 	y = coord['y'] * CELLSIZE + CELLSIZE // 2  # Adjust y-coordinate to center of cell
# 	radius = CELLSIZE // 2  # Radius of the circle
# 	pygame.draw.circle(SCREEN, RED, (x, y), radius)

# def drawObstacles(obstacles):
#     for obs in obstacles:
#         x = obs[0] * CELLSIZE
#         y = obs[1] * CELLSIZE
#         obstacleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
#         pygame.draw.rect(SCREEN, DARKGRAY, obstacleRect)

# def drawGrid():
# 	for x in range(0, WINDOWWIDTH, CELLSIZE):
# 		pygame.draw.line(SCREEN, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
# 	for y in range(0, WINDOWHEIGHT, CELLSIZE):
# 		pygame.draw.line(SCREEN, DARKGRAY, (0, y), (WINDOWWIDTH, y))

# if __name__ == '__main__':
# 	pygame.init()
# 	SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
# 	main(SCREEN)


import random
import pygame
import sys
from pygame.locals import *
from settingsSnakeFun import *

MEDIUM_OBSTACLES = [(10, 10), (15, 15), (20, 20), (5, 5), (7, 20), (7, 21), (25, 15), (26, 15), (23, 10), (22, 11), (4, 15), (5, 16), (22, 5)]
HARD_OBSTACLES = [(5, 5), (5, 6), (5, 7), (6, 5), (7, 5), (10, 11), (10, 12), (10, 13), (10, 10), (11, 10), (12, 10), (13, 10), (15, 15), (15, 16), (15, 17), (15, 18), (20, 5), (21, 5), (22, 5), (23, 5), (5, 19), (5, 18), (5, 27), (5, 20), (6, 20), (7, 20), (20, 20), (21, 20), (25, 13), (25, 12), (25, 14), (25, 11), (20, 3), (21, 3), (22, 3), (23, 3)]


def set_speed(selected_level):
    if selected_level == "EASY":
        return 3
    elif selected_level == "MEDIUM":
        return 5
    elif selected_level == "HARD":
        return 6


def main(SCREEN):
    global CLOCK, FONT, level, FPS
    pygame.init()
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake Game')
    showStartScreen(SCREEN,FPS=None)

    while True:
        pygame.mixer.music.play(-1, 0.0)
        level = showLevelSelection(SCREEN)  # Determine level first
        FPS = set_speed(level)  # Set FPS based on the chosen level
        # showStartScreen(SCREEN,FPS)  # Pass FPS as a parameter
        runGame()
        pygame.mixer.music.stop()
        showGameOverScreen()

def showLevelSelection(screen):
    # Add interface for level selection
    while True:
        screen.fill(BGCOLOR)
        drawLevelSelection(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_1:
                    return "EASY"
                elif event.key == K_2:
                    return "MEDIUM"
                elif event.key == K_3:
                    return "HARD"


def drawLevelSelection(screen):
    # Draw level selection options
    font = pygame.font.Font('freesansbold.ttf', 36)
    titlefont = pygame.font.Font('freesansbold.ttf', 50)
    text1 = font.render('Select Level:', True, BLACK)
    textRect1 = text1.get_rect()
    textRect1.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 3)
    text2 = font.render('1. Easy', True, BLACK)
    textRect2 = text2.get_rect()
    textRect2.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2)
    text3 = font.render('2. Medium', True, BLACK)
    textRect3 = text3.get_rect()
    textRect3.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2 + 50)
    text4 = font.render('3. Hard', True, BLACK)
    textRect4 = text4.get_rect()
    textRect4.center = (WINDOWWIDTH // 2, WINDOWHEIGHT // 2 + 100)
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)


def runGame():
    # Set a random starting point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    global wormCoords
    wormCoords = [{'x': startx, 'y': starty}, {'x': startx - 1, 'y': starty}, {'x': startx - 2, 'y': starty}]
    direction = RIGHT

    apple = getRandomLocation()
    if level == "MEDIUM":
        obstacles = MEDIUM_OBSTACLES
    elif level == "HARD":
        obstacles = HARD_OBSTACLES
    else:
        obstacles = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # Collision Detection
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            return
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                return
        for obstacle in obstacles:
            if wormCoords[HEAD]["x"] == obstacle[0] and wormCoords[HEAD]["y"] == obstacle[1]:
                return
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            APPLEEATSOUND.play()
            apple = getRandomLocation()
        else:
            del wormCoords[-1]

        # Moving the Snake
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)

        # Drawing the Screen
        SCREEN.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawObstacles(obstacles)
        drawScore((len(wormCoords) - 3) * 5)
        pygame.display.update()
        CLOCK.tick(FPS)


def getTotalScore():
    return (len(wormCoords) - 3) * 5


def drawPressKeyMsg():
    pressKeyText = FONT.render('Press A Key To Play', True, BLUE)
    pressKeyRect = pressKeyText.get_rect()
    pressKeyRect.center = (WINDOWWIDTH - 200, WINDOWHEIGHT - 100)
    SCREEN.blit(pressKeyText, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
            
    return keyUpEvents[0].key


def showStartScreen(SCREEN,FPS):
    titlefont = pygame.font.Font('freesansbold.ttf', 100)
    titleText = titlefont.render('PYGLIDE.', True, DARKGREEN)
    if FPS is None:
        FPS = 3
    while True:
        SCREEN.fill(BGCOLOR)
        titleTextRect = titleText.get_rect()
        titleTextRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        SCREEN.blit(titleText, titleTextRect)

        drawPressKeyMsg()
        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        CLOCK.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 75)
    gameOverText = gameOverFont.render('Game Over', True, RED)
    gameOverRect = gameOverText.get_rect()
    total_score = getTotalScore()
    high_scores = loadHighScores()
    new_highscore = False

    if level == "EASY":
        if total_score > high_scores["EASY"]:
            high_scores["EASY"] = total_score
            new_highscore = True
    elif level == "MEDIUM":
        if total_score > high_scores["MEDIUM"]:
            high_scores["MEDIUM"] = total_score
            new_highscore = True
    elif level == "HARD":
        if total_score > high_scores["HARD"]:
            high_scores["HARD"] = total_score
            new_highscore = True

    saveHighScores(high_scores)

    high_score_text = ""
    if level == "EASY":
        high_score_text = f'High Score - Easy: {high_scores["EASY"]} '
    elif level == "MEDIUM":
        high_score_text = f'High Score -  Medium: {high_scores["MEDIUM"]}'
    elif level == "HARD":
        high_score_text = f'High Score - Hard: {high_scores["HARD"]}'

    highScoreFont = pygame.font.Font('freesansbold.ttf', 30)
    highScoreText = highScoreFont.render(high_score_text, True, BLACK)
    highScoreRect = highScoreText.get_rect()
    highScoreRect.midtop = (WINDOWWIDTH / 2, 300)

    totalScoreFont = pygame.font.Font('freesansbold.ttf', 35)
    totalScoreText = totalScoreFont.render(' Total Score: %s' % (total_score), True, BLACK)
    totalScoreRect = totalScoreText.get_rect()
    totalScoreRect.midtop = (WINDOWWIDTH / 2, 150)
    gameOverRect.midtop = (WINDOWWIDTH / 2, 30)

    SCREEN.fill(BGCOLOR)
    SCREEN.blit(gameOverText, gameOverRect)
    SCREEN.blit(totalScoreText, totalScoreRect)
    SCREEN.blit(highScoreText, highScoreRect)

    # Display new high score message if applicable
    if new_highscore:
        newHighScoreFont = pygame.font.Font('freesansbold.ttf', 30)
        newHighScoreText = newHighScoreFont.render('Congratulations New highscore!', True, BLUE)
        newHighScoreRect = newHighScoreText.get_rect()
        newHighScoreRect.midtop = (WINDOWWIDTH / 2, 250)
        SCREEN.blit(newHighScoreText, newHighScoreRect)

    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(1000)

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


def drawScore(score):
    scoreText = FONT.render('Score: %s' % (score), True, BLACK)
    scoreRect = scoreText.get_rect()
    scoreRect.center = (WINDOWWIDTH - 100, 30)
    SCREEN.blit(scoreText, scoreRect)


def drawWorm(wormCoords):
    x = wormCoords[HEAD]['x'] * CELLSIZE
    y = wormCoords[HEAD]['y'] * CELLSIZE
    wormHeadRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(SCREEN, YELLOW, wormHeadRect)

    for coord in wormCoords[1:]:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(SCREEN, GREEN, wormSegmentRect)


def drawApple(coord):
    x = coord['x'] * CELLSIZE + CELLSIZE // 2  # Adjust x-coordinate to center of cell
    y = coord['y'] * CELLSIZE + CELLSIZE // 2  # Adjust y-coordinate to center of cell
    radius = CELLSIZE // 2  # Radius of the circle
    pygame.draw.circle(SCREEN, RED, (x, y), radius)


def drawObstacles(obstacles):
    for obs in obstacles:
        x = obs[0] * CELLSIZE
        y = obs[1] * CELLSIZE
        obstacleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(SCREEN, DARKGRAY, obstacleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(SCREEN, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(SCREEN, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    main(SCREEN)
