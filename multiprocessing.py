import multiprocessing
import os

#this function grabs the process id and a string defining what the process is 

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))


if __name__ == "__main__":
    whoami("Im the main program")
    for n in range(4):
        p = multiprocessing.Process(target=whoami,
                                    args=("I'm function %s" % n,))
        p.start()