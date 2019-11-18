import pygame
import random
import time

import sys
from PyQt5 import QtWidgets
from modules.form import Ui_Dialog


from modules.sortings import Bubble, Selection, Insertion


########################
print('MADE BY drogi17')
########################

methods = {
    "1" : "Bubble",
    "2" : "Selection",
    "3" : "Insertion"
}


########################################################################################################################
def start(x_matrix, y_matrix, width,height, method):
    image = pygame.image.load('image/image.jpg')
    array = []
    #x_matrix, y_matrix, width, height, method = input_data()
    speed = 0
    array_size = x_matrix*y_matrix



    ###############
    array_size_input = 0 #счетчик
    x_to_show = 10
    y_to_show = 10
    x_draw = 1
    while array_size_input <= array_size-1:   #заполнение массива
        array.append([(x_to_show, y_to_show, width, height), array_size_input])
        array_size_input += 1
        if x_draw <= x_matrix - 1:
            x_to_show += width + width / 10
            x_draw += 1
        else:
            x_draw = 1
            y_to_show += height + height / 10
            x_to_show = 10
    ###############






    ##############
    pygame.init()
    x_win = 10*2 + x_matrix*(round(width*1.5))  #\ размеры окна
    y_win = 10*2 + y_matrix*(round(height*1.5)) #/
    win = pygame.display.set_mode((x_win, y_win))   # отображение окна
    pygame.display.set_caption(methods[method])    # заголовок окна
    ##############


    if (x_matrix > 1) and (y_matrix > 1):
        run = True
    else:
        run = False



    ###############
    win.fill((0, 0, 0))
    x_to_show = 10
    y_to_show = 10
    x_draw = 1
    for element in array:
            win.blit(image, (x_to_show, y_to_show), element[0])
            if x_draw <= x_matrix-1:
                x_to_show += width + width / 10
                x_draw += 1
            else:
                x_draw = 1
                y_to_show += height + height / 10
                x_to_show = 10

    pygame.display.update()
    time.sleep(3)
    ###############


    random.shuffle(array) #запутывание массива



    ###############
    win.fill((0, 0, 0))
    x_to_show = 10
    y_to_show = 10
    x_draw = 1
    for element in array:
            win.blit(image, (x_to_show, y_to_show), element[0])
            if x_draw <= x_matrix-1:
                x_to_show += width + width / 10
                x_draw += 1
            else:
                x_draw = 1
                y_to_show += height + height / 10
                x_to_show = 10

    pygame.display.update()
    time.sleep(3)
    ###############



    nomber = 0
    max_n = -1
    minus = 1
    while run:
        pygame.time.delay(int(speed))

        for event in pygame.event.get():    #quit
            if event.type == pygame.QUIT:   #quit
                run = False                 #quit

        if method == '1':
            if minus < len(array):
                array = Bubble(array, nomber)
                nomber += 1
            else:
                pass
            if nomber == len(array)-minus:
                nomber = 0
                minus += 1

        if method == '2':
            if nomber == len(array)-2:
                pass
            else:
                array = Selection(array, nomber)
                nomber += 1

        if method == '3':
            if nomber == len(array):
                pass
            else:
                array = Insertion(array, nomber)
                nomber += 1


        #win.blit(image, (0, 0))
        win.fill((0, 0, 0))
        x_to_show = 10
        y_to_show = 10
        x_draw = 1
        for element in array:
            #pygame.draw.rect(win, element[0], (x_to_show, y_to_show, width, height))  # отрисовка
            win.blit(image, (x_to_show, y_to_show), element[0])
            if x_draw <= x_matrix-1:
                x_to_show += width + width / 10
                x_draw += 1
            else:
                x_draw = 1
                y_to_show += height + height / 10
                x_to_show = 10

        pygame.display.update()

    pygame.quit()

########################################################################################################################




app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def go():
    x_matrix = ui.lineEdit.text()
    y_matrix = ui.lineEdit_2.text()
    width    = ui.lineEdit_3.text()
    height   = ui.lineEdit_4.text()
    method   = ui.lineEdit_5.text()
    if (method != '1') and (method != '2') and (method != '3'):
        method = '3'
    if (x_matrix == '') or (y_matrix == '') or (width == '') or (height == ''):
        height = 50
        width = 50
        x_matrix = 10
        y_matrix = 10
    else:
        x_matrix = int(x_matrix)
        y_matrix = int(y_matrix)
        height = int(height) - 1
        width = int(width) - 1
        if (x_matrix > 1000) or (y_matrix > 1000) or (width > 1000) or (height > 1000):
            print('ТЫ ЧТО САМОУБИЙЦА??? ВИДЮХУ НЕ ЖАЛКО???')
            x_matrix = 100
            y_matrix = 100
    start(x_matrix, y_matrix, width, height, method)



ui.pushButton.clicked.connect(go)

sys.exit(app.exec_())



