#Core Game Loop
import pygame
from pygame.locals import *
from styles import Styling


def run_game():
    
    #initialize Pygame
    pygame.init()

    #Display setup
    screen = pygame.display.set_mode((800,400), pygame.RESIZABLE) #this sets the size of the window
    pygame.display.set_caption('Earth Discovery') #this names the window

    style_manager = Styling() #call to class function Styling

    #beginning background image
    background = pygame.image.load(r"images\planet-581239_1280.jpg") #Load background image 
    background = style_manager.scale_image(background, 800, 400) #scale image to fit the background
    
    #Intro description
    text = ("Since earth’s destruction 300 years ago, a new artificial planet emerged, Neos.\n"
        "You are a Specialist.\n"
        "Your mission is to travel to earth and collect resources.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #For when you maximize the window
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.size #get the sizes after maximizing the window
                background = style_manager.scale_image(background, screen_width, screen_height) #make the background image fit
      
        screen.blit(background, (0,0)) #draw background
        #     # Pass screen to the write function
        style_manager.write(
            text,
            (200, 200),  # X, Y coordinates
            screen,
            font_size = 40,
            center=True
        )
       
        pygame.display.flip() #update the display

    pygame.quit()

