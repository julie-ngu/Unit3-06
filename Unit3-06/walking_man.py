# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program swiches out the image of a man walking at a set time to create the illusion that this image 
# is animated

import ui
import time

@ui.in_background

def see_walking_man_button_touch_up_inside(sender):
    # This makes the man walk when button is pressed
    
    # variables
    number_of_pictures = 10
    counter = 0
    
    # process
    while counter < number_of_pictures:
        if counter == 0:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_1.bmp')
        
        elif counter == 1:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_2.bmp')
            
        elif counter == 2:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_3.bmp')
            
        elif counter == 3:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_4.bmp')
            
        elif counter == 4:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_5.bmp')
            
        elif counter == 5:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_6.bmp')
            
        elif counter == 6:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_7.bmp')
            
        elif counter == 7:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_8.bmp')
            
        elif counter == 8:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_9.bmp')
            
        elif counter == 9:
            # output
            view['walking_man_image'].image = ui.Image.named('./Resources/walk_10.bmp')
            
        counter = counter + 1
        time.sleep(0.1)

view = ui.load_view()
view.present('sheet')
