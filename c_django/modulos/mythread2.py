# from time import sleep

# print ('Hello')

# for i in range (10):
#     print(i)
#     sleep(.5)

# print('world!')

from threading import Thread
from time import sleep

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)
t1 = Thread(target=vai_demorar, args=('Thread 1',5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Thread 2',1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Thread 3',2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)