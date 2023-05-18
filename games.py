import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_width = int(width/1.6)
#we are going to make the line 10px
center_line_width = int(width/80)
# variables for the enemy car movements
right_lane = width/2 + road_width/4
left_lane = width/2 - road_width/4
speed = 1
pygame.init()
running = True

# display window for our game, width and length
screen = pygame.display.set_mode((size))

# to add a title 
pygame.display.set_caption("Unity_El Car Game")

# background colour
screen.fill((60, 221, 0))


# only after the display below will our screen turn or change colour
pygame.display.update()


# load car images
car2 = pygame.image.load("car20.png")
car2_location = car2.get_rect()
car2_location.center = ( right_lane, height * 0.8)

# load opposition images
car = pygame.image.load("car10.png")
car_location = car.get_rect()
car_location.center = (left_lane, height * 0.2)

counter = 0

''' below we creating a while loop to shut the Game when the logic
 in event is equal to quit them running is equal to calse colapsing the window
'''
while running:
    counter += 1
    if counter == 4000:
        speed += 0.15
        counter = 0
        print("level up", speed)
    # allowing the car to trancend downwards 1px at a time as the loop continues
    car_location[1] += speed
    # this is to make the car reappear when it goes of screen
    if car_location[1] > height:
        # randomizing car movement of the enemy
        if random.randint(0,1) == 0:
            car_location.center = right_lane, - 200
        else:
            car_location.center = left_lane, - 200
            
    # ENd Game
    if car2_location[0] == car_location[0] and car_location[1] > car2_location[1] -250:
        print("game over, you lost")
        break
        
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        # event for pressing buttons
        if event.type == KEYDOWN:
            # left
            if event.key in [K_a, K_LEFT]:
                car2_location = car2_location.move([-int(road_width/2), 0])
            # right    
            if event.key in [K_d, K_RIGHT]:
                car2_location = car2_location.move([+int(road_width/2), 0])
                
    # drawing grafics moved into while loop because 
    # "road"
    pygame.draw.rect(
        # black road
        screen,(50 ,50, 50),
        # specify the the width x, the positioning which is zero(center)y, then the size of the road and hight
        (width/2-road_width/2, 0, road_width, height)
    )

    # "line"
    pygame.draw.rect(
        screen, 
        # color
        (255, 240, 62),
        (width/2 - center_line_width/2, 0, center_line_width, height)
    )

    # "side line 1"
    pygame.draw.rect(
        screen, 
        # color
        (255, 255, 255),
        # positioning x, y, line wideth. height 
        (width/2 - road_width/2 + center_line_width * 2, 0, center_line_width, height)
    )

    # "side line 2"
    pygame.draw.rect(
        screen, 
        # color
        (255, 255, 255),
        # positioning x, y, line wideth. height 
        (width/2 + road_width/2 - center_line_width * 3, 0, center_line_width, height)
    )        
        

    # car draw function        
    screen.blit(car, car_location)
    screen.blit(car2, car2_location)
    pygame.display.update()

# to collapse the window as soon as we are done with it
pygame.quit()

#17.42