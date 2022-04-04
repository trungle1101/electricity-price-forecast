import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

from app import app
import pandas as pd
from datetime import date

tablename_id = 'merged_dataset'
range_list = ['1 day', '3 days', '1 week', '1 month']

def get_layout(param_query=None):
    layout = html.Div(id=f"dashboard{tablename_id}")
    return dbc.Container(
        [   
            html.Div([
                html.Div([   
                    html.Div("Choose range", className="card-title"),
                    dcc.Dropdown(
                        id=f"forward_day_dropdown{tablename_id}",
                        options=[
                            {
                                "label": x,
                                "value": x
                            } for x in range_list
                        ],
                        value = range_list[0],
                        clearable=False
                    )],
                    style={'padding': '15px'}
                ),
                html.Div([   
                    html.Div("Choose predicted day", className="card-title"),
                    dcc.DatePickerSingle(
                        id='date-picker-single',
                        min_date_allowed=date(2015, 1, 1),
                        max_date_allowed=date(2018, 12, 30),
                        initial_visible_month=date(2018, 12, 30),
                        date=date(2018, 12, 30)
                    )],
                    style={'padding': '15px'}
                )],
                style={'display': 'flex', 'margin': '7px 0 7px 0'}
            ),
            html.Div(layout),
            # html.Div(id=f'table_div{tablename_id}')
        ], fluid=True
    )

################# callbacks ###############################################
@app.callback(Output(component_id=f'dashboard{tablename_id}', component_property='children'),
    # Output(component_id=f'table_div{tablename_id}', component_property='children'),
    Input(component_id=f'forward_day_dropdown{tablename_id}', component_property='value'),
)
def update_layout(range_choosen):
    df = pd.read_csv('pages/forecast/show_data.csv')
    fig = px.line(x=pd.date_range(start='31/12/2018', periods=24, freq='H'), y=df['actual_previous_day'],
             labels=dict(x="Time", y="Price", color="Time Period"), title='Electricity forecast for 1-1-2019')
    fig.add_trace(go.Scatter(mode="markers", x=pd.date_range(start='1/1/2019', periods=24, freq='H'), y=df['predict_next_day'], name="prediction"))
    return html.Div(dcc.Graph(figure=fig), className="card-inside")
    
