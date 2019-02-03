import os
# from PIL import Image
from celery import Celery

app = Celery("tasks")
app.conf.update(
    BROKER_URL=os.environ.get("CELERY_BROKER_URL", "redis://"),
    CELERY_RESULT_BACKEND=os.environ.get("CELERY_RESULT_BACKEND", "redis://"),
    CELERY_ACCEPT_CONTENT=['json']
)


@app.task
def resize_image(image, height: int, width: int):
    # image = Image.frombytes(image)  # TODO more arguments
    # resized_img = image.resize((width, height))
    return "success"  # TODO serialize Image object and save redis
