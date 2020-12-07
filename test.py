from threading import Thread
import time


class Watcher:
    is_alive: bool = False
    is_ready: bool = True
    task = None
    interval: int = None
    thread: Thread = None
    start_interval_time = None

    def __init__(self, task, interval):
        self.task = task
        self.interval = interval

    def runner(self):
        if self.is_ready:
            self.thread = Thread(target=self.task)
            self.thread.start()
            self.is_alive = True
            self.is_ready = False

    def check_thread_is_alive(self):
        if not self.thread.is_alive():
            self.is_alive = False
            self.next_start_time = time.time() + self.interval

    def check_ready(self):

