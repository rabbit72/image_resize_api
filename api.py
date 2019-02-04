import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

# sentry_sdk.init(
#     dsn="https://80a6df4bce44486fa86ad5c542eb7181@sentry.io/1385196",
#     integrations=[AioHttpIntegration()]
# )

from aiohttp import web
from celery_queue import tasks
import io
from PIL import Image

routes = web.RouteTableDef()


@routes.get("/")
async def index(request):
    return web.Response(
        text=(
"""Welcome user!

/image/ - POST for resizing JPEG and PNG images
required fields:
    height=<1-9999px>
    width=<1-9999px>
    image=<Bytes like object>
    
Example for HTTPie:
    http -f POST localhost:8080/image/ height=128 width=128 image@~/test.jpeg

/image/{id} - GET get resized image

/image/{id}/status/ - GET check resizing status"""
        )
    )


@routes.post("/image/")
async def resize_image(request):
    data = await request.post()
    height = int(data["height"])
    width = int(data["width"])
    image_data = data["image"]
    image_data = io.BytesIO(image_data.file.read())
    task = tasks.resize_image.delay(image_data, height, width)
    return web.json_response({"task_id": task.id})


@routes.get("/image/{id}")
async def get_image(request):
    task_id = request.match_info["id"]
    if not is_image_ready(task_id):
        web.json_response(
            {"task_id": task_id, "message": "Image resizing has not finished"}
        )
    task = tasks.resize_image.AsyncResult(task_id)
    raw_image = task.result
    new_size_image = Image.frombytes(**raw_image["data"])
    image_bytes = io.BytesIO()
    new_size_image.save(image_bytes, format=raw_image["format"])
    return web.Response(body=image_bytes)


@routes.get("/image/{id}/status/")
async def get_image_status(request):
    task_id = request.match_info["id"]
    data = {"task_id": task_id, "status": is_image_ready(task_id)}
    return web.json_response(data)


def is_image_ready(task_id):
    return tasks.resize_image.AsyncResult(task_id).ready()


app = web.Application()
app.add_routes(routes)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
