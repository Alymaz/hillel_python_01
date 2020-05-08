from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(receiver, sender, response):
    while True:
        receiver.send(response)
        sleep(3)
        print(f"Process {getpid()} got message: {sender.recv()}")


if __name__ == "__main__":
    child1, parent1 = Pipe()
    child2, parent2 = Pipe()
    process_1 = Process(target=ponger, args=(child1, parent1, "ping")).start()
    process_2 = Process(target=ponger, args=(child2, parent2, "pong")).start()
