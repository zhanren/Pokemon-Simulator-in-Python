# -*- coding: utf-8 -*-
"""
Created on Sat May  2 17:40:13 2020

@author: qwerdf
"""


import dash_html_components as html
import dash_core_components as dcc

def NamedSlider(name, short, min, max, step, val, marks=None):
    """
    

    Parameters
    ----------
    name : TYPE
        text of the slider
    short : TYPE
        slider id
    min : TYPE
        min
    max : TYPE
        max
    step : TYPE
        step of each sliding
    val : TYPE
        default value
    marks : TYPE, optional
        marks on the slider

    Returns
    -------
    TYPE
        html slider object

    """
    if marks:
        step = None
    else:
        marks = {i: i for i in range(min, max + 1, step)}

    return html.Div(
        style={"margin": "25px 5px 30px 0px"},
        children=[
            f"{name}:",
            html.Div(
                style={"margin-left": "5px"},
                children=[
                    dcc.Slider(
                        id=f"slider-{short}",
                        min=min,
                        max=max,
                        marks=marks,
                        step=step,
                        value=val,
                    )
                ],
            ),
        ],
    )

def NamedInlineRadioItems(name, short, options, val, **kwargs):
    return html.Div(
        id=f"div-{short}",
        style={"display": "inline-block"},
        children=[
            f"{name}:",
            dcc.RadioItems(
                id=f"radio-{short}",
                options=options,
                value=val,
                labelStyle={"display": "inline-block", "margin-right": "7px"},
                style={"display": "inline-block", "margin-left": "7px"},
            ),
        ],
    )

def Card(children,**kwargs):
    """
    

    Parameters
    ----------
    children : TYPE
        html items
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    return html.Section(children,className="card-style")