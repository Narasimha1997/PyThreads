from pythreads import pythread
from time import sleep

@pythread
def task1():

    for i in range(10):

        print('Task1', i)
        sleep(2)


@pythread
def task2():

    for i in range(10):

        print('Task2', i)
        sleep(2)


#run the asynchronous functions
task1()
task2()
