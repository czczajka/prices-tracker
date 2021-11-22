import os

import services as _services
import pandas as pd

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse


import plotly.express as px

import uvicorn

from typing import List
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

import boto3
from botocore.exceptions import ClientError

bucket_name="pricestrackerstaticplots"

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_plots():
# TODO Try to use ORM instead of raw sql
#    df = pd.read_sql(Session.query(models.ItemEntry), Session.query(models.ItemEntry).session.bind)
    df = pd.read_sql('SELECT * FROM item_entries', engine, index_col='id')
    products = _services.find_items()
    for item in products:
        temp_df = df.loc[df['item_name'] == item.get_uri()]
        plot = px.line(data_frame=temp_df, x=temp_df['date'], y=temp_df['price'],
                       template='plotly_dark', )
        plot.update_layout(
            margin=dict(l=0, r=0, t=0, b=0, pad=20)
        )
        plot.update_xaxes()
        plot.update_yaxes(showgrid=False)
        file_path = 'static/plots/' + item.get_uri() + '.html'
        plot.write_html(file_path,
                        full_html=False,
                        include_plotlyjs='cdn')


@app.get("/g_plots")
def graph_create():
    generate_plots()
    s3_client = boto3.client('s3')
    for filename in os.listdir("static/plots/"):
        s3_client.upload_file("static/plots/" + filename, bucket_name, filename)
    return {"status": "success"}


# TODO Static files are each time downloaded, caching mechanism maybe
def download_plots_files():
    s3 = boto3.client('s3')
    for key in s3.list_objects(Bucket=bucket_name)['Contents']:
        filename = key['Key']
        s3.download_file(bucket_name, filename, "static/plots/" + filename)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    products = _services.find_items()
    download_plots_files()
    return templates.TemplateResponse('main.html', {'request': request, 'products': products})


@app.post("/add_entry/", response_model=schemas.Item)
def create_entry(entry: schemas.ItemEntry, db: Session = Depends(get_db)):
    return crud.add_item_entry(db=db, entry=entry)


@app.get("/entries/", response_model=List[schemas.Item])
def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    entries = crud.get_item_entries(db, skip=skip, limit=limit)
    return entries


if __name__ == "__main__":
    uvicorn.run(app)
