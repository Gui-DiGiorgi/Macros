# Here's a bot for my Rock Paper Scissors Game. It's pretty fast.


from PIL import ImageGrab
import pyautogui
import time
import keyboard

def pixel_lookout(screenWidth, screenHeight,image):
    for i in range(screenHeight):
        for j in range(screenWidth):
            if image[j,i] == (255,0,0) or image[j,i] == (0,255,0) or image[j,i] == (0,0,255):
                found = image[j,i]
                if j+149<=screenWidth:
                    if image[j+149,i] == found:
                        return [j,i]

keyboard.wait('S')

print("Starting Recognition!")

screenWidth, screenHeight = pyautogui.size()

true_image = ImageGrab.grab()
im = true_image.load()
rules_pix = pixel_lookout(screenWidth, screenHeight, im)

move = [175,-300]
recg_pixs = []
for i in range(len(move)):
    recg_pixs.append(rules_pix[i]-move[i])
    
clicker = [100,250,400]
item_clicker = []
for i in clicker:
    item_clicker.append([recg_pixs[0] + i, recg_pixs[1]])
    
symb_keys = ["Rock","Paper","Scissors"]

symb = {"Rock": [(28, 15, 7), (36, 23, 12), (53, 35, 21), (67, 48, 33), (70, 49, 32), (62, 39, 21), (54, 29, 9), 
                 (50, 23, 2), (51, 23, 2), (89, 57, 36), (105, 70, 50), (130, 95, 75), (159, 124, 104), (186, 151, 131), 
                 (206, 171, 151), (219, 184, 164), (225, 190, 170), (242, 207, 187), (242, 207, 187), (242, 207, 187), (243, 208, 188), 
                 (243, 208, 188), (243, 208, 188), (244, 209, 189), (242, 209, 190), (236, 205, 187), (230, 201, 185), (220, 191, 175), 
                 (199, 172, 155), (166, 140, 126), (126, 103, 87), (89, 66, 50), (64, 45, 28), (43, 24, 9), (45, 29, 13), 
                 (47, 31, 16), (50, 37, 21), (60, 48, 32), (64, 52, 36), (44, 35, 20)],
        "Paper": [(40, 18, 7), (62, 34, 20), (60, 25, 6), (86, 45, 23), (192, 148, 123), (225, 178, 150), (200, 154, 121), 
                  (216, 170, 134), (231, 188, 146), (241, 196, 157), (236, 193, 151), (233, 188, 149), (234, 191, 149), (237, 192, 153), 
                  (233, 190, 148), (236, 193, 151), (236, 193, 151), (237, 194, 152), (238, 195, 153), (240, 196, 157), (241, 197, 158), 
                  (242, 198, 159), (243, 199, 160), (240, 194, 158), (239, 193, 157), (238, 194, 159), (237, 193, 158), (236, 192, 157), 
                  (236, 192, 157), (235, 191, 156), (234, 191, 157), (234, 191, 157), (226, 183, 149), (224, 181, 147), (230, 189, 157), 
                  (234, 193, 161), (234, 195, 162), (244, 203, 173), (250, 215, 185), (233, 207, 182), (252, 246, 225), (171, 153, 133), 
                  (46, 27, 12), (52, 34, 22), (38, 22, 14)],
        "Scissors":[(61, 45, 36), (57, 40, 26), (49, 30, 15), (159, 136, 121), (228, 201, 182), (225, 197, 176), (230, 201, 183), 
                    (241, 213, 193), (249, 226, 207), (252, 223, 202), (229, 198, 177), (204, 173, 152), (160, 128, 107), (150, 118, 95), 
                    (133, 101, 78), (119, 87, 64), (114, 79, 57), (114, 79, 57), (120, 86, 61), (126, 90, 64), (206, 167, 138), 
                    (255, 222, 191), (231, 190, 162), (245, 206, 177), (247, 208, 179), (255, 220, 193), (249, 209, 183), (243, 206, 179), 
                    (246, 209, 182), (245, 209, 183), (245, 209, 183), (244, 210, 183), (245, 209, 185), (244, 210, 185), (245, 209, 185), 
                    (244, 210, 183), (250, 216, 188), (245, 214, 183), (242, 211, 180), (239, 210, 181), (247, 217, 189), (254, 226, 202), 
                    (252, 232, 211), (234, 223, 204), (208, 186, 171), (91, 69, 56), (32, 14, 3), (48, 34, 27), (32, 22, 18)]}

color_mouse_moving = [[(255,0,0),-2],[(0,255,0),-1],[(0,0,255),0]]

start = 0

while True:
    
    if start == 0:
        pass
        
    else:
        
        keyboard.wait('R')

        print("Restarting Game!")
        
    start += 1

    now = time.time()

    while time.time()-now < 60:

        true_image = ImageGrab.grab()
        im = true_image.load()

        if im[rules_pix[0],rules_pix[1]] == (255,0,0) \
        or im[rules_pix[0],rules_pix[1]] == (0,255,0) \
        or im[rules_pix[0],rules_pix[1]] == (0,0,255):

            item_recg = 125

            item_detec = [rules_pix[0], rules_pix[1]+item_recg]

            item = []

            color_rules = im[rules_pix[0],rules_pix[1]]
            new_color_rules = []

            for i in range(len(color_rules)):
                new_color = []
                for j in range(len(color_rules)):
                    c = color_rules[j]
                    if c+i<=255:
                        c += i
                    new_color.append(c)
                new_color_tuple = tuple(new_color)
                new_color_rules.append(new_color_tuple)

            banned = []

            for i in new_color_rules:
                banned.append(i)

            if item_detec[0]+150<=screenWidth:

                for i in range(150):

                    color_pix = im[item_detec[0],item_detec[1]]

                    if color_pix not in banned:
                        item.append(color_pix)

                    item_detec[0] += 1

            for i in symb_keys:
                if len(symb[i]) == len(item):
                    hand = i
                    break

            order = []

            color_list = []

            banned = [(0,0,0),(1,1,1),(2,2,2)]

            recg_pixs_copy = recg_pixs.copy()

            if recg_pixs[0]+500<=screenWidth:

                for i in range(500):

                    color_pix = im[recg_pixs_copy[0],recg_pixs_copy[1]]

                    if color_pix in banned and len(color_list)>0:
                        order.append(color_list)
                        color_list = []

                    elif color_pix not in banned:
                        color_list.append(color_pix)

                    recg_pixs_copy[0] += 1

            named_order = []

            for o in order:
                for i in symb_keys:
                    if len(symb[i]) == len(o):
                        named_order.append(i)
                        break

            for i in color_mouse_moving:
                if color_rules == i[0]:
                    victory = i[1]

            hand_to_click = symb_keys[symb_keys.index(hand) + victory]

            for i in range(len(symb_keys)):
                if named_order[i] == hand_to_click:
                    where_to_click = item_clicker[i]

            pyautogui.moveTo(where_to_click[0],where_to_click[1])
            pyautogui.click()
            time.sleep(0.1)
