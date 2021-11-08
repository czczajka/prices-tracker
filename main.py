import services as _services
import pandas as pd

from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


import plotly.express as px

import uvicorn

import os

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


def generate_plots():
    products = _services.find_items()
    for item in products:
        df = pd.read_csv('data/' + item.get_path())
        plot = px.line(data_frame=df, x=df.iloc[:, 0], y=df.iloc[:, 1])
        plot.update_layout(
            margin=dict(l=0, r=0, t=0, b=0)
        )
        file_path = 'static/plots/' + item.get_uri() + '.html'
        plot.write_html(file_path,
                        full_html=False,
                        include_plotlyjs='cdn')


@app.get("/g_plots")
def graph_create():
    generate_plots()
    return {"status": "success"}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    products = _services.find_items()
    return templates.TemplateResponse('main.html', {'request': request, 'products': products})


if __name__ == "__main__":
    uvicorn.run(app)
