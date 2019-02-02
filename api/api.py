import sentry_sdk
from sentry_sdk.integrations.aiohttp import AioHttpIntegration

sentry_sdk.init(
    dsn="https://80a6df4bce44486fa86ad5c542eb7181@sentry.io/1385196",
    integrations=[AioHttpIntegration()]
)

from aiohttp import web
from tasks import add


routes = web.RouteTableDef()


@routes.get('/')
@routes.get('/{name}')
async def handler(request):

    celery_response = add(4, 4)
    print(celery_response)
    text = f"Your result: {celery_response}"
    return web.Response(text=text)


app = web.Application()
app.add_routes(routes)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
