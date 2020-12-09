import logging
import time
from threading import Thread, Event

from my_logging import configure_logger

WORKING_TIME = 21


def task_1(done_event: Event):
    logger.info('Start Thread_1: Work 2 sec')
    time.sleep(2)
    logger.info('End   Thread_1')
    done_event.set()


def task_2(done_event: Event):
    logger.info('Start Thread_2: Work 5 sec')
    time.sleep(5)
    logger.info('End   Thread_2')
    done_event.set()


class Watcher:
    """
    :atribute task - задача которую надо делать
    :atribute interval - интервал между задачами
    :atribute thread - поток который делает задачу
    :atribute start_time - время когда начать следующий поток после ожидания интервала
    :atribute need_interval - требуется ли выставить время следующего потока
    """
    task = None
    interval: int = None
    thread: Thread = Thread(target=task)
    start_time = time.time()
    event = Event()

    def __init__(self, task, interval):
        self.task = task
        self.interval = interval

    def runner(self) -> None:
        """
        Создание и запуск потока.
        Ставится флаг что требуется поставить время запуска потока
        """
        self.set_start_time()
        if self.is_ready():
            Thread(target=self.task, args=(self.event,), daemon=True).start()
            self.start_time = 0

    def set_start_time(self) -> None:
        """
        Установка времени когда запустить снова поток.
        Флаг что надо поставить время запуска убирается
        """
        if self.is_done():
            self.start_time = time.time() + self.interval
            self.event.clear()

    def is_ready(self) -> bool:
        """
        Проверка что поток можно запускать
        """
        if not self.is_done() and time.time() >= self.start_time and self.start_time != 0:
            return True
        return False

    def is_done(self) -> bool:
        """
        Проверка что поток закончил работу
        """
        return self.event.is_set()



if __name__ == '__main__':
    configure_logger()
    logger = logging.getLogger()
    logger.info(f'Время работы программы: {WORKING_TIME} sec')

    start_program_time = time.time()
    stop_time = start_program_time + WORKING_TIME
    watch_1 = Watcher(task=task_1, interval=5)
    watch_2 = Watcher(task=task_2, interval=10)
    while time.time() < stop_time:
        watch_1.runner()
        watch_2.runner()
