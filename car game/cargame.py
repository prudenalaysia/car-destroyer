#All the graphics are by me, however I got the music from
#the pygame tutorial because I was unsure where to find the music


import pygame
from sys import exit
from button import Button
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('CAR DESTROYER')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 30)
game_active = True
start_time = 0
background_music = pygame.mixer.Sound('music.wav')
background_music.play(loops = -1)
background_music.set_volume(0.1)

def reset_game():
     global game_active, rock_rect
     game_active = True
     rock_rect.y = 0

     

def main_menu():
    pygame.display.set_caption("Main Menu")

    while True:
        global event
        screen.blit(menuBG, (0,0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = test_font.render('MENU',True,'White')
        menu_rect = menu_text.get_rect(center = (300, 50))

        desert_button = Button(pygame.image.load('desertbutton.png'), pos=(300, 150))
        daytime_button = Button(pygame.image.load('daytimebutton.png'), pos=(300, 250))
        nightime_button = Button(pygame.image.load('nightimebutton.png'), pos=(300, 350))

        for button in [desert_button, daytime_button, nightime_button]:
            button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if desert_button.input(mouse_pos):
                desert()
                return
            if daytime_button.input(mouse_pos):
                daytime()
                return
            if nightime_button.input(mouse_pos):
                nightime()
                return
            

        screen.blit(menu_text, menu_rect)

        pygame.display.flip()

def back():
    back_button = Button(pygame.image.load('backBUTTON.png'), pos = (520, 20))
    
    while True:

        mouse_pos = pygame.mouse.get_pos()
    
        back_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.input(mouse_pos):
                    main_menu()
                    
        pygame.display.flip
           
def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, 'White')
    score_rect = score_surf.get_rect(center = (50,20))
    screen.blit(score_surf,score_rect)

def rock_animation():
    global rock_surf, rock_index
    rock_index += .05
    if rock_index >= len(rock_glide):
        rock_index = 0
    rock_surf = rock_glide[int(rock_index)]

def falling():
        rock_rect.y += 10


def directions():
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
                    car_rect.x +=10        
        if keys[pygame.K_LEFT]:
                    car_rect.x -=10           
        if keys[pygame.K_a]:
                    rock_rect.x -=10      
        if keys[pygame.K_d]:
                    rock_rect.x +=10          
        if keys[pygame.K_s]:
                    falling()
        
                  



score_surf = test_font.render('Score:',False,'White')
score_rect = score_surf.get_rect(center = (50, 20))
background = pygame.image.load('carbackground.png.png')
desertBG = pygame.image.load('desertbackground.png')
daytimeBG = pygame.image.load('daytime.png')
menuBG = pygame.image.load('menubg.png')

car_surf = pygame.image.load('car.png').convert_alpha()
car_rect = car_surf.get_rect(topleft = (200,300))

rock_glide_1 = pygame.image.load('rock.png').convert_alpha()
rock_glide_2 = pygame.image.load('rock2.png').convert_alpha()
rock_glide = [rock_glide_1, rock_glide_2]
rock_index = 0
rock_surf = rock_glide[rock_index]
rock_rect = rock_surf.get_rect(topleft = (300, 0))
rock_gravity = 5


def desert():
    global game_active
    reset_game()
    pygame.display.set_caption("desert")
    back_button = Button(pygame.image.load('backBUTTON.png'), pos = (520, 20))
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    

            
                 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.input(mouse_pos):
                    main_menu()
                    return

            
        
            
        if game_active:
        
            screen.blit(desertBG, (0,0))
            screen.blit(car_surf,(car_rect))
            screen.blit(rock_surf, (rock_rect))  
 
            display_score()

            screen.blit(car_surf,car_rect)

            if rock_rect.bottom >= 390:
                rock_rect.bottom = 0
            screen.blit(rock_surf,rock_rect)

            if rock_rect.colliderect(car_rect):
                game_active = False
                main_menu()
                return
            back_button.update()
        
        else:
            return
    
        directions()
        rock_animation()
        pygame.display.flip()
        clock.tick(60)

def daytime():
    global game_active
    reset_game()
    pygame.display.set_caption("daytime")
    back_button = Button(pygame.image.load('backBUTTON.png'), pos = (520, 20))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.input(mouse_pos):
                    main_menu()
                    return
                

     
        if game_active:

            
            screen.blit(daytimeBG, (0,0))
            screen.blit(car_surf,(car_rect))
            screen.blit(rock_surf, (rock_rect))
        
            display_score()
            
            screen.blit(car_surf,car_rect)

    
            if rock_rect.bottom >= 390:
                rock_rect.bottom = 0
            screen.blit(rock_surf,rock_rect)

            if rock_rect.colliderect(car_rect):
                game_active = False
                main_menu()
                return
            back_button.update()
        else:
            return
    
        directions()
        rock_animation()
        pygame.display.flip()
        clock.tick(60) 

def nightime():
    global game_active
    reset_game()
    pygame.display.set_caption("night time")
    back_button = Button(pygame.image.load('backBUTTON.png'), pos = (520, 20))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.input(mouse_pos):
                    main_menu()
                    return

               
                    
        
            
        if game_active:
        
            screen.blit(background, (0,0))
            screen.blit(car_surf,(car_rect))
            screen.blit(rock_surf, (rock_rect))  
            
            display_score()
            
    

            screen.blit(car_surf,car_rect)

           

    
            if rock_rect.bottom >= 390:
                rock_rect.bottom = 0
            screen.blit(rock_surf,rock_rect)

            if rock_rect.colliderect(car_rect):
                game_active = False
                main_menu()
                return
            back_button.update()
        else:
            return
        directions()
        rock_animation()
        pygame.display.flip()
        clock.tick(60)

def run():
     while True:
        main_menu()

run()