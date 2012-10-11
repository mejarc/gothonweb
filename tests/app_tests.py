from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #404
    resp = app.request("/lugly")
    assert_response(resp, status="404")
    
    #hello
    resp = app.request("/")
    assert_response(resp)
    
    #defaults for form values
    resp = app.request("/game", method="POST")  #must, must be all uppercase, or tests won't work
    assert_response(resp, contains="Nobody")
    
    #mock data
    data = {"name": "Zed", "greet": "Hola"}
    resp = app.request("/hello", method="POST", data= data)
    assert_response(resp, contains="Zed")