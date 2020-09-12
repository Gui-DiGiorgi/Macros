# Here's some macro on the training minigames of Swords & Souls (http://armorgames.com/play/17817/swords-and-souls?t=1578005019)
# On my case it uses a 1366x768 notebook monitor. It needs to set the browser on fullscreen and go to the top of the page for it
# to start moving the mouse and pressing the keys

from PIL import ImageGrab
import pyautogui
from time import sleep
import math

screenWidth, screenHeight = pyautogui.size()
run = True

mode = int(input("Which Mode? 1 to 5... "))
mode -= 1

round_pixels = []
final_rp = []

if mode<0 or mode>4:
    run= False
    
if mode == 1:
    
    for i in range(71):
        x = round(math.sqrt(70**2-i**2))
        round_pixels.append([i,x])
        round_pixels.append([-i,x])
        round_pixels.append([i,-x])
        round_pixels.append([-i,-x])
    
    for i in range(len(round_pixels)):
        x_cord = round_pixels[i][0] + 680
        y_cord = round_pixels[i][1] + 508
        cords = [x_cord,y_cord]
        final_rp.append(cords)

while run:
    true_image = ImageGrab.grab()
    im = true_image.load()
    game_ready = im[0,0]
    
    if game_ready == (34,34,34):
        if mode == 0:
            for i in range(430,656):
                bottle = im[530,i]
                if bottle[2]<50:
                    if 445<i<470:
                        pyautogui.press('w')
                        sleep(0.1)
                        break
                    elif 545<i<570:
                        pyautogui.press('d')
                        sleep(0.1)
                        break
                    elif 620<i<645:
                        pyautogui.press('s')
                        sleep(0.15)
                        break
            if im[325,535][0]>240:
                pyautogui.press('a')
                sleep(0.05)
        elif mode == 1:
            for pix in final_rp:
                apple = im[pix[0],pix[1]]
                if apple[1]<50:
                    pyautogui.moveTo(pix[0],pix[1])
                    break
                    
                    
                
            
            
