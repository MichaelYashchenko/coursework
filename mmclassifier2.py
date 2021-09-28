import functions
import drawH
import matplotlib.pyplot as plt


#для двумерного случая / для n > 2 нужно изменить количество параметров, передаваемых из файла

hyberboxes_of_class_1 = []
hyberboxes_of_class_2 = []


def training(file_name):
    
    print('Training process:')
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    
    for line in open(file_name, 'r', encoding='utf-8'):
        
        expansion = False
        hyberboxes_array = []
        class_array = []
        
        plt.cla()

        data = line.strip().split()
        x, y, c = [float(x) for x in data]
        if c == 1:
            for hyberbox in hyberboxes_of_class_1:

                if(functions.HyberboxExpansionTest(hyberbox[0], hyberbox[1], [x, y])):

                    functions.HyberboxExpansion(hyberbox[0], hyberbox[1], [x, y])
                        
                    expansion = True
                    for hyberbox2 in hyberboxes_of_class_2:
                            
                        functions.HyperboxOverlapTestAndContraction(hyberbox[0], hyberbox[1], hyberbox2[0], hyberbox2[1])
                    break
            if(not expansion): 
                
                for hyberbox2 in hyberboxes_of_class_2:
                    functions.HyperboxOverlapTestAndContraction([x, y], [x, y], hyberbox2[0], hyberbox2[1])
                
                hyberboxes_of_class_1.append([[x, y], [x, y]])
            
        else:
            for hyberbox in hyberboxes_of_class_2:

                if(functions.HyberboxExpansionTest(hyberbox[0], hyberbox[1], [x, y])):

                    functions.HyberboxExpansion(hyberbox[0], hyberbox[1], [x, y])

                    expansion = True

                    for hyberbox2 in hyberboxes_of_class_1:
                            
                        functions.HyperboxOverlapTestAndContraction(hyberbox[0], hyberbox[1], hyberbox2[0], hyberbox2[1])
                    break
            if(not expansion): 
                
                for hyberbox2 in hyberboxes_of_class_1:
                    functions.HyperboxOverlapTestAndContraction([x, y], [x, y], hyberbox2[0], hyberbox2[1])
                
                hyberboxes_of_class_2.append([[x, y], [x, y]])

        print(hyberboxes_of_class_1)
        print(hyberboxes_of_class_2)
        print("\n")

        for hyberbox in hyberboxes_of_class_1:
            hyberboxes_array.append( hyberbox )
            class_array.append( 1 )

        for hyberbox in hyberboxes_of_class_2:
            hyberboxes_array.append( hyberbox )
            class_array.append( 2 )

        drawH.draw_array_of_hyberbox(hyberboxes_array, class_array, ax)
        fig.show()
        plt.pause(2)
        

        
def DefineClassOfDot(x):

    max_grade_of_membership = -1
    class_membership = - 1

    for hyberbox in hyberboxes_of_class_1:
        if max_grade_of_membership < functions.membership(hyberbox[0], hyberbox[1], x):
            max_grade_of_membership = functions.membership(hyberbox[0], hyberbox[1], x)
            class_membership = 1       

    for hyberbox in hyberboxes_of_class_2:
        if max_grade_of_membership < functions.membership(hyberbox[0], hyberbox[1], x):
            max_grade_of_membership = functions.membership(hyberbox[0], hyberbox[1], x)
            class_membership = 2

    print('Result:')
    print('Class: ' + str(class_membership))
    print('Grade of membership: ' + str(max_grade_of_membership))


training("input.txt")
DefineClassOfDot([0.15, 0.2])
DefineClassOfDot([0.5, 0.5])
