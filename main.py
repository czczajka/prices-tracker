import random
import services as _services
import pandas as pd

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import dash
from dash import dcc
from dash import html

from plotly.subplots import make_subplots
import plotly.graph_objects as go

import uvicorn as uvicorn

app = FastAPI()
app_dash = dash.Dash(__name__,  requests_pathname_prefix='/dash/')

app.mount("/dash", WSGIMiddleware(app_dash.server))
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def new_func(product_name: str):
    print(product_name)
    df = pd.read_csv('csv-db/hause_prices.csv')

    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(
    go.Scatter(x=df['Date'], y=df['Price']),
    row=1, col=1
)

    df = pd.read_csv('csv-db/data_salary.csv')
    fig.add_trace(
    go.Scatter(x=df['date'], y=df['Value']),
    row=2, col=1
)

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

    #funkcja ktora bedzie uruchamiala serwer dash z argumentami
    new_func(element)
    ####
    
    return templates.TemplateResponse('template.html', {'request': request, 'product': element})


if __name__ == "__main__":
    uvicorn.run(app)