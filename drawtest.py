import drawH
import pylab

v = [0.2, 0.2]
w = [0.3, 0.3]

Array_for_class_1_hyberboxes = [[[0.2, 0.2], [0.3, 0.3]],
                                [[0.4, 0.3], [0.6, 0.6]]]
                
classification_factor = [1, 0]

pylab.xlim (0, 1)
pylab.ylim (0, 1)
#pylab.grid()


# Получим текущие оси
axes = pylab.gca()
axes.set_aspect("equal")

#проверяем работу drawHyberbox
#drawHyberbox (v, w, axes)

'''
for hyberbox, classification in zip(Array_for_class_1_hyberboxes,
                                    classification_factor):
    drawRect(hyberbox[0], hyberbox[1], classification, axes)
'''
#проверяем работу draw_array_of_hyberbox
drawH.draw_array_of_hyberbox(Array_for_class_1_hyberboxes, classification_factor, axes)

pylab.show()