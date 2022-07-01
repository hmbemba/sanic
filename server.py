from sanic import Sanic, json
from sanic.response import text, json, html
from jinja2 import Environment, FileSystemLoader

fl = FileSystemLoader('templates')
env = Environment(loader=fl,)

app = Sanic("MyHelloWorldApp")
app.static('/static','./static')

@app.get("/")
async def hello_world(request):
    t = env.get_template('index.html')
    o = t.render(var = ['people','influencersrg'])
    return html(o)

if __name__ == '__main__':
    app.run(auto_reload=True, debug=True)