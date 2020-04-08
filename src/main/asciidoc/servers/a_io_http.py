from aiohttp import web


async def handle(request):
    return {"Hello": "World"}


def init_func(argv):
    print("I am starting")
    app = web.Application()
    app.router.add_get("/", handle)
    return app
