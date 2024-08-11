import os
from nokia import generate_image
from sanic import Sanic
from sanic.response import raw
from sanic_cors import CORS

app = Sanic(name='nokia')
CORS(app) #为什么作者不加上跨域修复??????

PRODUCTION = bool(os.environ.get("PRODUCTION"))
debug = False if PRODUCTION else True
workers = 1 if debug else os.cpu_count()


@app.post("/api/nokia")
async def index(request):
    text = request.json.get("text", "ZZKIA")
    #print(generate_image(text))
    return raw(generate_image(text))

    #这儿生成函数没有问题
app.run(host="0.0.0.0", port=3001, debug=debug, workers=workers)