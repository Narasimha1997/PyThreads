### PyThreads
A simple python library that makes creating and running threads easier. This library allows functions to behave 
asynchronously (similiar to JavaScript async functions).

Check the examples below:

#### Example 1:
Run two tasks in parallel:

```python
from pythreads import pythread
from time import sleep

#create a pythread
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
#task1 and task2 now behave like asynchronous functions
task1()
task2()

```

#### Example 2
Passing parameters

```python
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
```


