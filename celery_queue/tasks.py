import os
from PIL import Image
from celery import Celery

os.environ["CELERY_ACCEPT_CONTENT"] = "pickle"
app = Celery("tasks", backend="redis://localhost:6379/0", broker="redis://localhost")
print(app.co)


@app.task
def resize_image(image, height: int, width: int):
    image = Image.frombytes(image)  # TODO more arguments
    resized_img = image.resize((width, height))
    return  # TODO serialize Image object and save redis
