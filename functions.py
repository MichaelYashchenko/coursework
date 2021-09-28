#рассматриваем двумерный случай
n = 2

#максимальный размер гиперпрямоугольника, определяется пользователем (от 0 до 1)
maximum_size = 0.3

# "чувсвтительность" - определяет размер области в котором точка принадлежит данному гиперпрямоугольнику
sensitivity_parameter = 0.15

'''

w = 0, 0
v = 0, 0
x = 0, 0 
'''

#функция проверяет можно ли расширить гиперпрямоугольник
def HyberboxExpansionTest(v, w, x):
    eval_of_size = 0
    for i in range(n):
        eval_of_size += (max(w[i], x[i]) - min(v[i], x[i]))
    return n * maximum_size >= eval_of_size

#функция расширяет гиперпрямоугольник
'''
def HyberboxExpansion(w, v, x):
    if(HyberboxExpansionTest(w, v, x)):
        for i in range(n):
            v[i] = min(v[i], x[i])
            w[i] = max(w[i], x[i])
'''
def HyberboxExpansion(v, w, x):
    for i in range(n):
        v[i] = min(v[i], x[i])
        w[i] = max(w[i], x[i])

#функция проверяет есть ли у двух гиперпрямоугольников (из разных классов) пересечение
#если есть, сжимает их оптимальным образом
# v1, w1 - данный гиперпрямоугольник был расширен
# v2, w2 - гиперпрямоугольник из другого класса проверяемый на пересечение
def HyperboxOverlapTestAndContraction(v1, w1, v2, w2):

    OverlapFactorOld = 1
    OverlapFactorNew = 1
    dN = -1                                          #номер размерности, которую будем менять, если есть пересечение dimensionNumber
                                                     
    for i in range(n):

        if(v1[i] < v2[i] and v2[i] < w1[i] and w1[i] < w2[i]): #case 1
            OverlapFactorNew = min(w1[i] - v2[i], OverlapFactorOld)

        elif(v2[i] < v1[i] and v1[i] < w2[i] and w2[i] < w1[i]): #case 2
            OverlapFactorNew = min(w2[i] - v1[i], OverlapFactorOld)
         
        elif(v1[i] < v2[i] and v2[i] < w2[i] and w2[i] < w1[i]): #case 3
            OverlapFactorNew = min( min(w2[i] - v1[i], w1[i] - v2[i]) , OverlapFactorOld)
        
        elif(v2[i] < v1[i] and v1[i] < w1[i] and w1[i] < w2[i]): #case 4
            OverlapFactorNew = min( min(w1[i] - v2[i], w2[i] - v1[i]) , OverlapFactorOld)
        
        if(OverlapFactorOld - OverlapFactorNew > 0):
            dN = i
            OverlapFactorOld = OverlapFactorNew

    
    if(dN > -1): #если нашли пересечение

        vj, wj = v1[dN], w1[dN]
        vk, wk = v2[dN], w2[dN]

        if(vj < vk and vk < wj and wj < wk): #case 1
            wj = (wj + vk) / 2
            vk = wj
        
        elif(vk < vj and vj < wk and wk < wj): #case 2
            wk = (wk + vj) / 2
            vj = wk

        elif(vj < vk and vk < wk and wk < wj and (wk - vj) < (wj - vk)): #case 3a
            vj = wk

        elif(vj < vk and vk < wk and wk < wj and (wk - vj) > (wj - vk)): #case 3b
            wj = vk

        elif(vk < vj and vj < wj and wj < vk and (wk - vj) < (wj - vk)): #case 4a
            wk = vj

        elif(vk < vj and vj < wj and wj < vk and (wk - vj) > (wj - vk)): #case 4b
            vk = wj
        
        v1[dN], w1[dN] = vj, wj
        v2[dN], w2[dN] = vk, wk

    


def membership(w, v, x):
    sum = 0
    for i in range(n):
        sum += ( max(0, 1 - max(0, sensitivity_parameter * min(1, x[i] - w[i]))) +
                 max(0, 1 - max(0, sensitivity_parameter * min(1, v[i] - x[i]))) )

    return sum/(2 * n)

#print(HyberboxExpansionTest(w, v, x))
#print(membership(w, v, x))

        

        



        





