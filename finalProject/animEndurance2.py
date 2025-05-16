import dash
from dash import State, dcc, html
import pandas as pd
# from sqlalchemy import create_engine
import sqlite3
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from datetime import datetime  # Import datetime module
import dash_bootstrap_components as dbc  # Import Dash Bootstrap Components
from dash import callback_context

# Create a connection to the local MariaDB database using SQLAlchemy
# engine = create_engine('mariadb+mariadbconnector://powerlab:thisisatest@10.229.27.250/fp_powerlab')
db_name = "sdet101_test.db"

con = sqlite3.connect(db_name, check_same_thread=False)

# Function to load data from the 'endurance_data' table into a pandas dataframe
def load_data():
    query = "SELECT * FROM endurance_data"
    df = pd.read_sql_query(query, con)
    column_mapping = {
        "date": "Data",
        "hh": "H-H (ms)",
        "icoil": "I-Coil",
        "vsrc": "V-Source",
        "op_dir": "Transfer Direction"
    }
    df["date"] = pd.to_datetime(df["date"])
    df.rename(columns=column_mapping, inplace=True)
    return df

# Load initial data
dataEndurance_df = load_data()
# Create a Dash application with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Alexandria Data Monitoring System"), width=8)
    ], className="my-3"),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Label("Date Range"),
                dcc.DatePickerRange(
                id='date-picker-range',
                # start_date=dataEndurance_df['Date'].min().strftime('%Y-%m-%d'),
                start_date=dataEndurance_df['Data'].min().strftime('%Y-%m-%d'),

                end_date=datetime.today().strftime('%Y-%m-%d'),
                display_format='YYYY-MM-DD',
                className="mb-3",
                minimum_nights=0,
                )
            ])   
        ], width=6),
        dbc.Col([
            dbc.Row([
                dbc.Label("Start time"),
                dbc.Col(dcc.Input(id='start-time', type='text', placeholder='Start Time (HH:MM:SS)', value='00:00:00', className="mb-3"), width=12)
            ])
        ], width=3),
        dbc.Col([
            dbc.Row([
                dbc.Label("Stop time"),
                dbc.Col(dcc.Input(id='end-time', type='text', placeholder='End Time (HH:MM:SS)', value='23:59:59', className="mb-3"), width=12)
            ])
        ], width=3),
        dbc.Col([
            dbc.Row([
                dbc.Col(dbc.Button("Toggle X-axis", id='x-axis-toggle', color="primary", className="mb-3"),width="auto"),
                dbc.Col(dbc.Button("Download Data", id='btn-download-csv', color="info", className="mb-3"), width="auto"),
                dcc.Download(id="download-dataframe-csv"),
                dbc.Col(dbc.Button("Play", id='play-button', color="success",disabled=True, className="mb-3"),width="auto"),
                dbc.Col(dbc.Button("Pause", id='pause-button', color="danger",disabled=False, className="mb-3"),width="auto"),
            ]),
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col(dcc.Store(id='data-store', data=dataEndurance_df.to_dict('records')), width=12),
        dcc.Store(id='filtered-data-store'),

    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='dataEndurance-graph'), width=12)
    ]),
    dcc.Interval(
        id='interval-component',
        interval=3*1000,  # Update every 3 seconds
        n_intervals=0,
        disabled=False  # Set to True to disable the interval
    ),
    dbc.Row([
        dbc.Col(html.Div(id='data-table', style={'height': '500px', 'overflowY': 'scroll'}), width=12)
    ])
], fluid=True)

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn-download-csv", "n_clicks"),
    State("filtered-data-store", "data"),
    prevent_initial_call=True
)
def download_csv(n_clicks, data):
    df = pd.DataFrame(data)
    filename = f"data_{datetime.now().strftime('%d%m%y_%H%M')}.csv"
    print(filename)
    return dcc.send_data_frame(df.to_csv, filename, index=False)

@app.callback(
    Output('interval-component', 'disabled'),
    Output('play-button', 'disabled'),
    Output('pause-button', 'disabled'),
    Input('play-button', 'n_clicks'),
    Input('pause-button', 'n_clicks'),
)
def toggle_interval(n_play, n_pause):
    ctx = callback_context
    if not ctx.triggered:
        # no button has been clicked yet
        raise dash.exceptions.PreventUpdate
    btn_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if btn_id == 'play-button':
        return False, True,  False   # enable interval  to start screen updates
    else:
        return True ,  False, True   # disable interval to stop screen updates

@app.callback(
    Output('data-store', 'data'),
    Input('interval-component', 'n_intervals')
)
def update_data(n):
    # Load new data from the database
    dataEndurance_df = load_data()
    return dataEndurance_df.to_dict('records')

@app.callback(
    [Output('dataEndurance-graph', 'figure'), Output('data-table', 'children'),Output('filtered-data-store', 'data')],
    [Input('data-store', 'data'), Input('date-picker-range', 'start_date'), Input('date-picker-range', 'end_date'), Input('start-time', 'value'), Input('end-time', 'value'), Input('x-axis-toggle', 'n_clicks')]
)
def update_graph(data, start_date, end_date, start_time, end_time, n_clicks):
    dataEndurance_df = pd.DataFrame(data)
    
    # Combine date and time for filtering
    start_datetime = f"{start_date} {start_time}"
    end_datetime = f"{end_date} {end_time}"
    
    # Ensure datetime format is consistent
    dataEndurance_df['Data'] = pd.to_datetime(dataEndurance_df['Data'])
    start_datetime = pd.to_datetime(start_datetime)
    end_datetime = pd.to_datetime(end_datetime)
    
    # Filter data based on selected date-time range
    filtered_df = dataEndurance_df[(dataEndurance_df['Data'] >= start_datetime) & (dataEndurance_df['Data'] <= end_datetime)]
    # sort by ascending order 
    filtered_df = filtered_df.sort_values(by='Data', ascending=False)

    # Separate datasets based on 'Transfer Direct'
    df_ne = filtered_df[filtered_df['Transfer Direction'] == 2]
    df_en = filtered_df[filtered_df['Transfer Direction'] == 1]
    
    # Determine x-axis type based on toggle button clicks
    if n_clicks and n_clicks % 2 == 1:
        x_ne = list(range(len(df_ne)))
        x_en = list(range(len(df_en)))
        xaxis_title = 'Record Count'
        tick_format = ""
        tick_angle = 0
    else:
        x_ne = df_ne['Data']
        x_en = df_en['Data']
        xaxis_title = 'Date'
        tick_format = '%m-%d %h:%m:%S'
        tick_angle = -45
    
    # Create the figure with two lines for H-H (ms) values based on Transfer Direct
    figure = {
        'data': [
            go.Scatter(x=x_ne, y=df_ne['H-H (ms)'], mode='lines+markers', name='N->E', line={'width': 3}),
            go.Scatter(x=x_en, y=df_en['H-H (ms)'], mode='lines+markers', name='E->N', line={'width': 3})
        ],
        'layout': go.Layout(
            title='Endurance Data Graph',
            xaxis={'title': xaxis_title,  'tickangle': tick_angle,'tickfont': {'size': 10}},
            yaxis={'title': 'Transfer Speed (H-H) Values (ms)', 'range': [0, None]},
            transition={'duration': 250},
        )
    }
    
    # Create table with filtered data
    table_header = [
        html.Thead(html.Tr([html.Th("Record Id"),html.Th("Date"), html.Th("Transfer Speed (H-H) (ms)"), html.Th("Transfer Direction"), html.Th("Current (A)"), html.Th("Voltage (Vrms)")]))  # Add table header
    ]
    
    table_rows = []
    # create two dictionaries, one for each transfer direction. and set the the data table row color
    for index, row in filtered_df.iterrows():
        if row["Transfer Direction"] == 1:
            row_class = "row-n2e"  # N->E
            transfer_direct_value = "N->E"
        elif row["Transfer Direction"] == 2:
            row_class = "row-e2n"  # E->N
            transfer_direct_value = "E->N"
        else:
            row_class = ""
            transfer_direct_value = "N/A"
        table_rows.append(html.Tr([html.Td(row["id"]),html.Td(row["Data"].strftime("%Y-%m-%d %H:%M:%S" )), html.Td(row["H-H (ms)"]), html.Td(transfer_direct_value), html.Td(row["I-Coil"]), html.Td(row["V-Source"])], className=row_class))
    #create data table components
    table_body = [html.Tbody(table_rows)]
    table = dbc.Table(table_header + table_body, bordered=True, striped=True, hover=True)

    return figure, table, filtered_df.to_dict('records')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=18080)