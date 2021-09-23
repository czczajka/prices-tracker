import pandas as pd
import plotly.express as px


def generate_site():
    df = pd.read_csv('csv-db/product11.csv')
    create_plot_iframe(df, 'date', 'price', 'static/graphs/product11.html',
                       'title')


def create_plot_iframe(df, x_name, y_name, outpath, title):
    plot = px.line(data_frame=df, x=x_name, y=y_name, title=title)
    plot.update_layout(
        margin=dict(l=0, r=0, t=0, b=0)  # plot_bgcolor='pink'
    )
    plot.write_html(outpath,
                    full_html=False,
                    include_plotlyjs='cdn')
