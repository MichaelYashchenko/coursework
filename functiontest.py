import functions

#проверяем работу функций HyberboxExpansionTest и membership и HyberboxExpansion

w = [0.3, 0.3]
v = [0.2, 0.2]
x = [0.1, 0.1]

print(functions.HyberboxExpansionTest(w, v, x))
print(functions.membership(w, v, x))

functions.HyberboxExpansion(w, v, x)
print( v, " ", w)

#проверяем работу функции HyperboxOverlapTestAndContraction
# такой пример был в статье

v1 = [0.2, 0.2]
w1 = [0.5, 0.5]

v2 = [0.4, 0.3]
w2 = [0.6, 0.6]

functions.HyperboxOverlapTestAndContraction(v1, w1, v2, w2)


print(v1," ", w1, " ", v2, w2)

