# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                html.Br(),
dcc.Dropdown(
    id='site-dropdown',
    options=[
        {'label': 'All Sites', 'value': 'ALL'},
        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
    ],
    value='ALL',
    placeholder='Select a Launch Site here',
    searchable=True
),



                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
html.P("Payload range (Kg):"),

dcc.RangeSlider(
    id='payload-slider',
    min=0,
    max=10000,
    step=1000,
    value=[min_payload, max_payload]
),
html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    Input('site-dropdown', 'value'),
    Input('payload-slider', 'value')
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    mask = (
        (spacex_df['Payload Mass (kg)'] >= low)
        & (spacex_df['Payload Mass (kg)'] <= high)
    )
    filtered_df = spacex_df[mask]

    if selected_site == 'ALL':
        fig = px.scatter(
            filtered_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title='Correlation between Payload and Success for all sites'
        )
    else:
        site_df = filtered_df[filtered_df['Launch Site'] == selected_site]
        fig = px.scatter(
            site_df,
            x='Payload Mass (kg)',
            y='class',
            color='Booster Version Category',
            title=f'Correlation between Payload and Success for {selected_site}'
        )


    return fig

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# TASK 2: Add a callback function to render success-pie-chart based on selected site dropdown
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    filtered_df = spacex_df

    # If ALL sites are selected, show total success launches by site
    if entered_site == 'ALL':
        # Filter only successful launches
        all_success_df = filtered_df[filtered_df['class'] == 1]
        # Group by Launch Site and count successes
        all_success_counts = all_success_df.groupby('Launch Site').size().reset_index(name='success_count')

        fig = px.pie(
            all_success_counts,
            values='success_count',
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
        return fig

    # If a specific site is selected, show success vs failure for that site
    else:
        site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        # Count successes (class=1) and failures (class=0)
        outcome_counts = site_df.groupby('class').size().reset_index(name='count')
        # Make labels more readable
        outcome_counts['Outcome'] = outcome_counts['class'].replace({1: 'Success', 0: 'Failure'})

        fig = px.pie(
            outcome_counts,
            values='count',
            names='Outcome',
            title=f'Total Success vs Failure for site {entered_site}'
        )
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app

# ---------------------------------------------------------
# Final Findings from My Dashboard (Using My Dataset)
#
# 1. Which site has the largest number of successful launches?
#    Answer: KSC LC-39A (10 successful launches)
#
#    Visual Insight:
#    When selecting KSC LC-39A in the dropdown, the scatter plot shows a
#    dense cluster of class=1 (success) points compared to other sites.
#
# 2. Which site has the highest launch success rate?
#    Answer: KSC LC-39A (76.9 percent success)
#
#    Visual Insight:
#    The KSC LC-39A scatter shows very few failures (class=0 points),
#    confirming the high performance relative to other sites.
#
# 3. Which payload range has the highest launch success rate?
#    Answer: 7500–10000 kg (60 percent success rate)
#
#    Visual Insight:
#    Although few launches occur in this range, the scatter plot shows
#    that almost all points in the 7500–10000 kg area are successes (class=1).
#    This produces the highest success rate despite the low sample size.
#
# 4. Which payload range has the lowest launch success rate?
#    Answer: 5000–7500 kg (22.2 percent success rate)
#
#    Visual Insight:
#    This range shows a large number of failures (class=0) in the scatter plot,
#    creating a visually noticeable band of unsuccessful missions.
#
# 5. Which F9 Booster Version Category has the highest launch success rate?
#    Answer: B5 (100 percent success; perfect record)
#            Next best: FT (66.7 percent)
#
#    Visual Insight:
#    In the scatter plot, every B5 launch appears as a class=1 success.
#    FT (green dots) also cluster strongly at success values compared to
#    versions like v1.0 or v1.1 which show many failures.
#
# Additional Visual Interpretation:
#    Even though the 7500–10000 kg payload range has the highest success rate,
#    the majority of successful launches (by count) are visually clustered
#    between 2000–4000 kg in the scatter plot. This indicates that while
#    heavy payloads are highly reliable percentage-wise, the mid-range
#    payload missions dominate the dataset in terms of total successful launches.
# ---------------------------------------------------------

