from random import random
from threading import Thread
from time import sleep
from typing import Optional

STEP_IN_SECONDS = 0.1


class Task:
    def __init__(self, payload, max_duration_in_second=5):
        self.payload = payload
        self.__execution_time = random() * max_duration_in_second

    def is_ready(self):
        self.__execution_time -= STEP_IN_SECONDS
        return self.__execution_time < 0


class EventQueue:
    def __init__(self):
        self.queue = []

    def put(self, task: Task):
        self.queue.append(task)

    def is_empty(self):
        return not bool(self.queue)

    def pop(self) -> Optional[Task]:
        done = []
        for task in self.queue:
            if task.is_ready():
                done.append(task)

        for task in done:
            self.queue.remove(task)
            return task
        else:
            return None


class EventLoop:
    def __init__(self):
        self.queue = EventQueue()
        self.__running = True

    def stop(self):
        self.__running = False

    def add_message(self, payload: str):
        if self.__running:
            self.queue.put(Task(payload))
        else:
            print("Rejected: loop is stopping")

    # tag::run_event_loop[]
    def run_event_loop(self):
        while True:
            # exit when done
            if self.queue.is_empty() and not self.__running:
                break
            task = self.queue.pop()
            if task:
                print(task.payload)
            sleep(STEP_IN_SECONDS)
    # end::run_event_loop[]


def main():
    loop = EventLoop()
    t = Thread(target=loop.run_event_loop)
    t.start()

    while True:
        try:
            message = input()
            loop.add_message(message)
        except EOFError:
            break
    loop.stop()
    t.join()


if __name__ == "__main__":
    main()
