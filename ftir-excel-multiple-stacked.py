"""
Stacked FTIR Plotter from Excel Files
Copyright (C) 2026 Nitish Kapur
GitHub: github.com/nitish-kapur
Licensed under GNU GPLv3

    This script was made as a part of a biofuel research project.

    1.  Loads FTIR transmission data from a hard-coded Excel file
        ('FTIR Precursors.xls') in the same directory; the first column
        must contain wavenumbers and each subsequent column one sample's
        transmission spectrum.
    2.  Assigns a distinct colour from a predefined palette to each sample;
        colours cycle if there are more than 13 samples.
    3.  Adds one Plotly Scatter trace per sample, plotting transmission (%)
        against wavenumber (cm⁻¹).
    4.  Configures hover tooltips to display the wavenumber and transmission
        value with a yellow background for visibility.
    5.  Sets the X-axis to inverted order as per FTIR convention.
    6.  Applies a clean white background to both the plot area and the
        surrounding paper, with black axis lines mirrored on all sides.
    7.  Displays the interactive plot in the default web browser.
"""


import pandas as pd
import plotly.graph_objects as go

# Load the Excel file
file_path = 'FTIR Precursors.xls'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Extract wavenumber values (first column)
wavenumber = df.iloc[:, 0]

# Create a plotly figure
fig = go.Figure()

# Define colors for the plot
colors = [
    '#000000',  # Blue
    '#ff7f0e',  # Orange
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#9467bd',  # Purple
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#7f7f7f',  # Gray
    '#bcbd22',  # Yellow-Green
    '#17becf',  # Cyan
    '#f9a825',  # Yellow
    '#1f77b4',  # Black
    '#9c27b0'   # Violet
]


# Add traces for each column (except the first one)
for i, col in enumerate(df.columns[1:]):
    fig.add_trace(go.Scatter(
        x=wavenumber,
        y=df[col],
        mode='lines',
        marker=dict(size=2),
        name=col,
        line=dict(color=colors[i % len(colors)]),
        # hoverinfo='name+y+x',  # Show name and coordinates on hover

        hovertemplate= '%{x} cm<sup>-1</sup><br>' +  # Display wavenumber value inside hover box
                      '<b>%{y}%</b>',  # Display transmission value inside hover box
        hoverlabel=dict(bgcolor="yellow", font_size=20, font_family="Arial"),


        opacity=1  # Default opacity for all lines
    ))

# Update layout to include hover effects and invert x-axis
fig.update_layout(
    title="Averaged Transmission Spectra",
    xaxis_title=r'Wavenumber (cm<sup>-1</sup>)',
    yaxis_title='Averaged Transmission Values(%)',
    hovermode="closest",
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis=dict(
        autorange="reversed",
        showgrid=False,
        gridcolor='lightgrey',
        gridwidth=1,
        tickfont=dict(size=16),
        title_font=dict(size=18),
        showline=True,
        linecolor='black',
        linewidth=2,
        mirror=True,                  # Draws axis line on opposite side too
    ),
    yaxis=dict(
        showgrid=False,
        gridcolor='lightgrey',
        gridwidth=1,
        tickfont=dict(size=16),
        title_font=dict(size=18),
        showline=True,
        linecolor='black',
        linewidth=2,
        mirror=True,                  # Draws axis line on opposite side too
    ),
    legend=dict(
        font=dict(size=16)
    ),
)
# Add hover interaction to dim all lines except the one being hovered
fig.update_traces(
    # hoverlabel=dict(bgcolor="yellow", font_size=16, font_family="Arial"),
    opacity=1,  # Dim all traces by default
    selected=dict(marker=dict(color='black', opacity=1))  # Make hovered trace bold
)

# Show the plot
fig.show()
