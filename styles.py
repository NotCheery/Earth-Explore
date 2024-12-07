#file used for styling texts, images, buttons, etc
#Styling Propterties for scale, button, images, etc in one class called 'Styling'
import pygame

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
    
    #text styling
    def write(self, text, location, screen, font_size=34, color=(255,255,255), center=False):
        font = pygame.font.Font(None, font_size)
        lines = text.split("\n")
        
        if center:
            # Calculate starting position to vertically and horizontally center the entire block of text
            total_text_height = len(lines) * font_size  # Total height of all the lines combined
            start_x = screen.get_width() // 2
            start_y = (screen.get_height() - total_text_height) // 2
        else:
            # Default starting positions
            start_x, start_y = location
        
        # Render each line
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            text_rect = text_surface.get_rect()
            
            if center:
                # Center each line
                text_rect.center = (start_x, start_y + i * font_size)
            else:
                # Render at specific offsets
                text_rect.topleft = (start_x, start_y + i * font_size)

            screen.blit(text_surface, text_rect)
