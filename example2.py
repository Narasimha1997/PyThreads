from pythreads import pythread
from time import sleep

@pythread
def task(times, sleep_time , name = "Prasanna"):

    for i in range(times):

        print(name)
        sleep(sleep_time)



def demo_call():

    task(10, 2)

    print("I execute first")

demo_call()
