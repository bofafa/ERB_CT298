import plotly.io as pio
pio.renderers.default = 'browser'

fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "Python Bar Chart"}}
})

pio.show(fig)

fig = dict({
    "data": [{"type": "scatter",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "Python Scatter Chart"}}
})

pio.show(fig)