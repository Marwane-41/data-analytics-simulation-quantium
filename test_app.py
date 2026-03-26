# Need to check if : 
    #The header is present.
    #The visualisation is present.
    #The region picker is present.
    
from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict


# Import the names of callback functions you want to test
from app import app

def test_header_present(dash_duo):
    dash_duo.start_server(app) # creating a fake browser 
    header = dash_duo.find_element('h1')
    assert header is not None
    assert "Pink Morsel Sales" in header.text
    
    
def test_visualization(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element('#starter-graph')
    assert graph is not None
    
def test_radio_buttons(dash_duo):
    dash_duo.start_server(app)
    radio_button = dash_duo.find_element('#xaxis-type')
    assert radio_button is not None
    
    
