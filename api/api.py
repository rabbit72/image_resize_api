from aiohttp import web


routes = web.RouteTableDef()


@routes.get('/')
@routes.get('/{name}')
async def handler(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)


app = web.Application()
app.add_routes(routes)


if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
