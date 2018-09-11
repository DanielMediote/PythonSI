from threading import thread
import time

def my_funct(i):
    print('Iniciaando a Thread %d\n' % i)
    time.sleep(5)
    print('Thread %d foi finalizado' % i)

for i in threads:
    t = Thread(target=my_funct, args=(i,))
    t.start()
