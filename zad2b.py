def fun1for(liczby):
    for n in liczby:
        print(n*2)

def fun2list(liczby):
    list=[]
    list=[n*2 for n in liczby]
    for l in list:
        print (l)

fun1for([2,4,6,1,6])
fun2list([2,4,6,1,6])