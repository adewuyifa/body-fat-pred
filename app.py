import pickle

import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import html, dcc, Input, Output, State
import pandas as pd
import numpy as np

# App dev
navbar = dbc.NavbarSimple(
    brand="Body Fat Predictor",
    brand_href="#",
    color="orange",
    dark=True,
    brand_style={'fontSize': 30, 'fontWeight': 'bold'}
)

question_one = html.Div(
    [
        dbc.Label("1. What is your Density (determined from underwater weighing)"),
        dbc.Input(
            id='density',
            type='float',
            min=0,
            max=10,
            step=1,
            placeholder="Density",
        ),
    ]
)

question_two = html.Div(
    [
        dbc.Label("2. How old are you?"),
        dbc.Input(
            id='age',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Age in years",
        ),
    ]
)

question_three = html.Div(
    [
        dbc.Label("3. How much do you weigh?"),
        dbc.Input(
            id='weight',
            type='number',
            min=0,
            max=1000,
            step=1,
            placeholder="weight in pounds",
        ),
    ]
)

question_four = html.Div(
    [
        dbc.Label("4. What is your height?"),
        dbc.Input(
            id='height',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Height in inches",
        ),
    ]
)

question_five = html.Div(
    [
        dbc.Label("5. What is your Neck circumference?"),
        dbc.Input(
            id='neck',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Neck circumference in cm",
        ),
    ]
)

question_six = html.Div(
    [
        dbc.Label("6. What is your chest circumference?"),
        dbc.Input(
            id='chest',
            type='number',
            min=0,
            max=200,
            step=1,
            placeholder="Chest circumference in cm",
        ),
    ]
)

question_seven = html.Div(
    [
        dbc.Label("7. What is your abdomen circumference?"),
        dbc.Input(
            id='abdomen',
            type='number',
            min=0,
            max=200,
            step=1,
            placeholder="Abdomen circumference in cm",
        ),
    ]
)

question_eight = html.Div(
    [
        dbc.Label("8. What is your hip circumference?"),
        dbc.Input(
            id='hip',
            type='number',
            min=0,
            max=200,
            step=1,
            placeholder="Hip circumference in cm",
        ),
    ]
)

question_nine = html.Div(
    [
        dbc.Label("9. What is your thigh circumference?"),
        dbc.Input(
            id='thigh',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Thigh circumference in cm",
        ),
    ]
)

question_ten = html.Div(
    [
        dbc.Label("10. What is your knee circumference?"),
        dbc.Input(
            id='knee',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Knee circumference in cm",
        ),
    ]
)

question_eleven = html.Div(
    [
        dbc.Label("11. What is your ankle circumference?"),
        dbc.Input(
            id='ankle',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Ankle circumference in cm",
        ),
    ]
)

question_twelve = html.Div(
    [
        dbc.Label("12. What is your biceps circumference?"),
        dbc.Input(
            id='biceps',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Biceps (extended) circumference in cm",
        ),
    ]
)

question_thirteen = html.Div(
    [
        dbc.Label("13. What is your forearm circumference?"),
        dbc.Input(
            id='forearm',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Forearm circumference in cm",
        ),
    ]
)

question_fourteen = html.Div(
    [
        dbc.Label("14. What is your wrist circumference?"),
        dbc.Input(
            id='wrist',
            type='number',
            min=0,
            max=100,
            step=1,
            placeholder="Wrist circumference in cm",
        ),
        html.Br(),
        dbc.Button('Submit', id='submit-val', n_clicks=0, color='primary',  className="d-grid gap-2 col-3 mx-auto")
    ]
)

form_1 = dbc.Form([question_one, question_two, question_three])
form_2 = dbc.Form([question_four, question_five, question_six])
form_3 = dbc.Form([question_seven, question_eight, question_nine])
form_4 = dbc.Form([question_ten, question_eleven, question_twelve])
form_5 = dbc.Form([question_thirteen, question_fourteen])
card = dbc.Card(
    [
        dbc.CardBody(
            dbc.Tabs(
                [
                    dbc.Tab(label="Page 1", children=[html.Br(), form_1]),
                    dbc.Tab(label="Page 2", children=[html.Br(), form_2]),
                    dbc.Tab(label="Page 3", children=[html.Br(), form_3]),
                    dbc.Tab(label="Page 4", children=[html.Br(), form_4]),
                    dbc.Tab(label="Page 5", children=[html.Br(), form_5]),
                ],
                id="card-tabs",
                className="nav nav-pills nav-fill"
            )
        ),
    ]
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server
app.config.suppress_callback_exceptions = True
app.title = "Body Fat Predictor"
app.layout = html.Div([
    html.Div(navbar),
    html.Br(),
    html.H4("Know your body fat percentage in 5minutes!!!", className="text-center"),
    html.Hr(),
    dbc.Container([
       dbc.Row([
           dbc.Col(card),
           dbc.Col(
                daq.Gauge(
                    showCurrentValue=True,
                    units="%",
                    color={"gradient": True, "ranges": {"yellow": [0, 11],
                                                        "green":[11, 22], "orange":[22, 28], "red":[28, 50]}},
                    value=0,
                    label={"label": 'Predicted body fat', "style": {"fontSize": "20px"}},
                    max=50,
                    min=0,
                    size=300,
                    id="gauge"
                )
           )
       ])
    ]),
    html.Hr(),
    dcc.Store(id="store-data", data=[], storage_type="session")
])


@app.callback(
    Output("store-data", "data"),
    Input("density", "value"),
    Input("age", "value"),
    Input("weight", "value"),
    Input("height", "value"),
    Input("neck", "value"),
    Input("chest", "value"),
    Input("abdomen", "value"),
    Input("hip", "value"),
    Input("thigh", "value"),
    Input("knee", "value"),
    Input("ankle", "value"),
    Input("biceps", "value"),
    Input("forearm", "value"),
    Input("wrist", "value")
)
def make_prediction(density, age, weight, height, neck, chest, abdomen,
                    hip, thigh, knee, ankle, biceps, forearm, wrist):

    data = {
        "Density": density,
        "Age": age,
        "Weight": weight,
        "Height": height,
        "Neck": neck,
        "Chest": chest,
        "Abdomen": abdomen,
        "Hip": hip,
        "Thigh": thigh,
        "Knee": knee,
        "Ankle": ankle,
        "Biceps": biceps,
        "Forearm": forearm,
        "Wrist": wrist,
    }
    df = pd.DataFrame(data, index=[0])

    return df.to_dict('records')


@app.callback(
    Output("gauge", "value"),
    Input("submit-val", "n_clicks"),
    State("store-data", "data")
)
def model_prediction(n_clicks, data):
    if n_clicks > 0:
        df = pd.DataFrame(data, index=[0])
        # Load model
        with open("model-rf.pkl", "rb") as f:
            model = pickle.load(f)
        prediction = model.predict(df)
        prediction = np.round(prediction[0], 1)

        return prediction


if __name__ == '__main__':
    app.run_server(debug=True)
