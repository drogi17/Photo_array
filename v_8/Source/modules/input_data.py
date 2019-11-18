def input_data():
    x_matrix = input('X: ')
    y_matrix = input('Y: ')
    width = input('width(50): ')
    height = input('height(50): ')
    print('')
    print('1. Bubble')
    print('2. Selection')
    print('3. Insertion')
    method = input('Method: ')
    if method == '':
        method = '3'
    if (x_matrix == '') or (y_matrix == '') or (width == '') or (height == ''):
        height = 50
        width = 50
        x_matrix = 10
        y_matrix = 10
    else:
        x_matrix = int(x_matrix)
        y_matrix = int(y_matrix)
        height = int(height)-1
        width = int(width)-1
        if (x_matrix > 1000) or (y_matrix > 1000) or (width > 1000) or (height  > 1000):
            print('ТЫ ЧТО САМОУБИЙЦА??? ВИДЮХУ НЕ ЖАЛКО???')
            x_matrix = 100
            y_matrix = 100
    return x_matrix, y_matrix, width, height, method