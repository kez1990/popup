import pyautogui as pg
import pygame, time, os
import webbrowser



popup = pg.confirm('Enter option Gfg', buttons =['A', 'B', 'C', 'X'])


if popup == "A":
    pygame.init()
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    time.sleep(1)
    image = pygame.image.load('hacker.jpg')
    window.blit(image, (0, 0))
    pygame.display.update()
    time.sleep(3)


if popup == "B":
    filename = "message.txt"
    filepath = os.path.join(filename)
    with open(filepath, 'w') as file:
        file.write("You want to stop this Press C.")


if popup == "C":
    webbrowser.open("Password.html")

if popup == "X":
    pg.password(text='Enter Password', title='You are free!!', default='', mask='')
 


