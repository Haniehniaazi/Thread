# we want to start the f funcs firt than gs and in the end h func

import threading
import time

def f1():
    time.sleep(3)
    print('f1 finished')
    
def f2():
    time.sleep(4)
    print('f2 finished')

def f3():
    time.sleep(2)
    print('f3 finished')

def f4():
    time.sleep(3)
    print('f4 finished')
    
def g1():
    time.sleep(1)
    print('g1 finished')

def g2():
    time.sleep(1.5)
    print('g2 finished')
    
def h():
    time.sleep(0.5)
    print('h finished')

# Threading the funs for fs :    
th_1 = threading.Thread(target = f1, name = '1')
th_2 = threading.Thread(target = f2, name = '2')
th_3 = threading.Thread(target = f3, name = '3')
th_4 = threading.Thread(target = f4, name = '4')

# start f funs :
th_1.start()
th_2.start()
th_3.start()
th_4.start()

#join Threads for fs :
th_1.join()
th_2.join()
th_3.join()
th_4.join() 

th_1 = threading.Thread(target = g1, name = '1')
th_2 = threading.Thread(target = g2, name = '2')

# start g funcs :
th_1.start()
th_2.start()

#join Threads for gs :
th_1.join()
th_2.join()

th_1 = threading.Thread(target = h, name = '1')

# start h fun :
th_1.start()






    