from celery import Celery

# Configure Celery to use Redis as a broker
app = Celery('tasks', broker='redis://redis:6379/0')

@app.task
def add(x, y):
    return x + y
