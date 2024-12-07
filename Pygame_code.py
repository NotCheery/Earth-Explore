import pygame
from pygame.locals import *

#initialize Pygame
pygame.init()

#Display setup
screen = pygame.display.set_mode((800,400), pygame.RESIZABLE) #this sets the size of the window
pygame.display.set_caption('Earth Discovery') #this names the window

#Styling Propterties for scale, button, images, etc in one class called 'Styling'
class Styling:
    def __init__(self, text=None, color=(255, 255, 255), font_size=36):
        self.text = text
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        
    def style_button(self): #changes to anything relying on here
        return self.color, 3, self.text
    
    #Scale to keep background images proportional
    def scale_image(self, image, width, height): #Figure out the math
        og_width, og_height = image.get_size() #get original sizes
        
        width_scale_factor = width/og_width
        height_scale_factor = height/og_height
        scale_factor = min(width_scale_factor, height_scale_factor)
        new_width = int(og_width * scale_factor)
        new_height = int(og_height * scale_factor)
        return pygame.transform.scale(image, (new_width, new_height))

call_to_Styling = Styling() #call to class function Styling

#beginning background image
background = pygame.image.load(r"planet-581239_640.jpg") #Load background image
background = call_to_Styling.scale_image(background, 800, 400) #scale image to fit the background

#Button creation
# rectangle = pygame.draw.rect(screen, (255,255,0), pygame.Rect(30, 30, 60, 60))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #For when you maximize the window
        elif event.type == pygame.VIDEORESIZE:
            screen_width, screen_height = event.size #get the sizes after maximizing the window
            background = call_to_Styling.scale_image(background, screen_width, screen_height) #make the background image fit
            
    screen.blit(background, (0,0)) #draw background
    pygame.draw.rect(screen, (255,255,0), [150, 50, 150, 50],2) #(w,h,w,h)
   
    
    
    pygame.display.flip() #update the display

pygame.quit()
