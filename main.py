import random
import csvcreator as _csv
import services as _services
from schemas import csvCreate
import pandas as pd

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import dash
from dash import dcc
from dash import html
import plotly.express as px

import uvicorn as uvicorn

app = FastAPI()
app_dash = dash.Dash(__name__,  requests_pathname_prefix='/dash/')

app.mount("/dash", WSGIMiddleware(app_dash.server))
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

########################################################
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app_dash.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
####################################################

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    product_names = _services.find_product_names()
    random.shuffle(product_names)
    num = len(product_names)
    return templates.TemplateResponse('index.html', {'request': request, 'products': product_names, 'num': num})


@app.get("/{element}", response_class=HTMLResponse)
async def product(request: Request, element: str):

    if not _services.find_product_by_name(element):
        raise HTTPException(status_code=404, detail="Item not found")

    product_names = _services.find_product_names()
    random.shuffle(product_names)
    data = _services.set_data(element)
    return templates.TemplateResponse('template.html', {'request': request, 'data': data, 'products': product_names})


if __name__ == "__main__":
    uvicorn.run(app)