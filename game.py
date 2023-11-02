# Space Dodge - Nitheeshmk_

import pygame
import random
import sys

#Pygame Initializing
pygame.init()

#Constants
FONT = pygame.font.Font('font/Pixeltype.ttf', 50)
SCREEN_WIDTH,SCREEN_HEIGHT = 1000,650
PLAYER_HEIGHT = 80
PLAYER_WIDTH = 60
PLAYER_SPEED = 5
SPIDER_HEIGHT = 60
SPIDER_WIDTH = 40
SPIDER_SPEED = 5
SPIDER_ADD_INCREMENT = 1500
FONT_COLOR = '#dad9d9'

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Monkey Spidy - Nitheeshmk')
BG = pygame.transform.scale(pygame.image.load('Asserts/forest bg.jpg'),(SCREEN_WIDTH,SCREEN_HEIGHT)).convert_alpha()

#Clock 
clock = pygame.time.Clock()


# images
player = pygame.transform.scale(pygame.image.load('Asserts/monkey.png'),(PLAYER_WIDTH,PLAYER_HEIGHT)).convert_alpha()
spider = pygame.transform.scale(pygame.image.load('Asserts/spider.png'),(SPIDER_WIDTH,SPIDER_HEIGHT)).convert_alpha()


# rectangles
player_rect = player.get_rect(midbottom = (PLAYER_WIDTH,650))
spider_rect = player.get_rect(center = (450,50))


def draw(obstacle_list,start_time):
    SCREEN.blit(BG,(0,0))
    SCREEN.blit(player,player_rect)
    global current_time
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_board = FONT.render(f'Time: {current_time} s',False,FONT_COLOR)
    time_rect = time_board.get_rect(center = (90,50))
    SCREEN.blit(time_board,time_rect)
    
    for spider_rect in obstacle_list:
        SCREEN.blit(spider,spider_rect)

    pygame.display.update()


def main():
    game_on = True
    game_active = True
    spider_count = 0
    obstacle_list = []
    start_time = 0

    while game_on:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                pygame.quit()
                sys.exit()
            if not game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                    obstacle_list = []


        if game_active:
            draw(obstacle_list,start_time)
            spider_count += clock.tick(60)
            if spider_count > SPIDER_ADD_INCREMENT:
                for _ in range(4):
                    spider_x = random.randint(0, SCREEN_WIDTH - SPIDER_WIDTH)
                    spider_rect = pygame.Rect(spider_x, -SPIDER_HEIGHT,SPIDER_WIDTH, SPIDER_HEIGHT)
                    obstacle_list.append(spider_rect)

                spider_count = 0    

            # Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and  player_rect.x > 0:
                player_rect.x -= PLAYER_SPEED
            elif keys[pygame.K_RIGHT] and player_rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
                player_rect.x += PLAYER_SPEED 
        
            
            # Falling and removing star
            for spider_rect in obstacle_list[:]:
                spider_rect.y += SPIDER_SPEED
                if spider_rect.y > SCREEN_HEIGHT:
                    obstacle_list.remove(spider_rect)
                elif spider_rect.colliderect(player_rect):
                    obstacle_list.remove(spider_rect)
                    game_active = False
                    break

        # Game Over
        else:
            
            SCREEN.blit(BG, (0, 0))
            
            lost_text = FONT.render(f"Score: {current_time}", 1, "white")
            play_again = FONT.render(f"Press SPACE to play again", False, "white")
            SCREEN.blit(lost_text, (400, 270))
            SCREEN.blit(play_again, (300, 320))

            
            pygame.display.update()
             

            
        clock.tick(60)

if __name__ == "__main__":
    main()
    