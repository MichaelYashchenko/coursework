import pylab
import matplotlib.patches

#рисует прямоугольник
def drawHyberbox (v, w, classification, axes):

    if v[0] == w[0] and v[1] == w[1]:
        rect_coord = v
        rect_width = 0.01
        rect_height = 0.01
        rect_angle = 0
    else:
        rect_coord = v
        rect_width = (w[0] - v[0])
        rect_height = (w[1] - v[1])
        rect_angle = 0
    
    if classification == 1:
        color = "g"
    else:
        color = "r"

    rect = matplotlib.patches.Rectangle (rect_coord,
                                         rect_width,
                                         rect_height,
                                         rect_angle,
                                         color=color,
                                          fill = False)
    axes.add_patch (rect)
    #pylab.text (-1.5, 1.5, "Rect", horizontalalignment="center")


#отрисовывает массив прямоугольников
def draw_array_of_hyberbox(array_of_hyberboxes, array_of_classification, axes):

    for hyberbox, classification in zip(array_of_hyberboxes,
                                        array_of_classification):
        drawHyberbox (hyberbox[0], hyberbox[1], classification, axes)