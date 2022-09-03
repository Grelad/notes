import time

from first_project.celery import app


@app.task
def sleep_and_print(value: int, message: str):
    time.sleep(value)
    print(message)