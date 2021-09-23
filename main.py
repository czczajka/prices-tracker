import random

from fastapi import FastAPI, Request, HTTPException
import csvcreator as _csv
from schemas import csvCreate
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import plot
import services as _services

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


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


@app.post("/csvCreate")
def create_csv(file_data: csvCreate):
    _csv.create_file(file_data)
    return {"detail": "its working :)"}


@app.get("/gcreate")
def graph_create():
    plot.generate_site()
    return {"detail": "git"}
