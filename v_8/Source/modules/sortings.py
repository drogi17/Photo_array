def Bubble(array, nomber):
    if array[nomber][1] > array[nomber + 1][1]:
            last = array[nomber]
            array[nomber] = array[nomber + 1]
            array[nomber + 1] = last
    return array


def Selection(array, nomber):
    z = nomber
    min = z
    while z <= len(array)-1:
        if array[z][1] < array[min][1]:
            min = z
        z += 1
    array[nomber], array[min] = array[min], array[nomber]
    #print(array[min])
    return array

def Insertion(array, nomber):
    x = 0
    while x <= nomber:
        if array[nomber][1] <= array[x][1]:
            elem = array[nomber]
            n = nomber-1
            while n >= x:
                array[n], array[n+1] = array[n+1], array[n]
                n -= 1
            array[x] = elem
            break
        else:
            x += 1
    return array