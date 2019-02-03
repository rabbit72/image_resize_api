import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

# sentry_sdk.init(
#     dsn="https://80a6df4bce44486fa86ad5c542eb7181@sentry.io/1385196",
#     integrations=[AioHttpIntegration()]
# )

from aiohttp import web
from celery_queue import tasks
import io

routes = web.RouteTableDef()


@routes.get("/")
async def index(request):
    return web.Response(
        text="Welcome user!\n\n"
        "/image/ - POST for resizing\n"
        "/image/{id} - GET get resized image\n"
        "/image/{id}/status/ - GET check resizing status"
    )


@routes.post("/image/")
async def resize_image(request):
    data = await request.post()
    height = int(data["height"])
    width = int(data["width"])
    print(str(data["image"].file))  # TODO serialize this object and send to workers
    task = tasks.resize_image.delay(1, 2, 3)
    return web.json_response({"task_id": task.id})


@routes.get("/image/{id}")
async def get_image(request):
    task_id = request.match_info["id"]
    if not is_image_ready(task_id):
        web.json_response(
            {"task_id": task_id, "message": "Image resizing has not finished"}
        )
    task = tasks.resize_image.AsyncResult(task_id)
    image = task.result
    return web.Response(text=task.result)
    # return web.Response(body=io.StringIO(image_bytes))


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
