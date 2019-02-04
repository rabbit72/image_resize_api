import os
from PIL import Image
from celery import Celery

app = Celery("tasks")
app.conf.update(
    BROKER_URL=os.environ.get("CELERY_BROKER_URL", "redis://"),
    CELERY_RESULT_BACKEND=os.environ.get("CELERY_RESULT_BACKEND", "redis://"),
    CELERY_ACCEPT_CONTENT=["json", "pickle"],
    CELERY_TASK_SERIALIZER="pickle",
    CELERY_RESULT_SERIALIZER="pickle"
)
# CELERY_TASK_SERIALIZER="json"  # default option for celery app
# CELERY_RESULT_SERIALIZER="json"  # default option for celery app


@app.task(serializer="pickle")
def resize_image(image_data, height: int, width: int):
    image = Image.open(image_data)
    new_img = image.resize((width, height))
    serialized_image = {
        "data": {
            'data': new_img.tobytes(),
            'size': new_img.size,
            'mode': new_img.mode
        },
        "format": image.format,
    }
    return serialized_image
