import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

from utils.constants import home_page_location, forecast_page_location, iris_page_location

from pages.home import home
from pages.forecast import forecast
from pages.iris import iris



@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    app.logger.debug(pathname)
    if pathname == forecast_page_location:
        return forecast.get_layout()
    elif pathname == home_page_location :
        return dbc.NavLink(href="https://iotmind.vn/", active="exact")
    elif pathname == iris_page_location:
        return iris.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )