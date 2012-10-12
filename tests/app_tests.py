from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #404
    resp = app.request("/lugly")
    assert_response(resp, status="404")
    
    #index
    resp = app.request("/")
    assert_response(resp)
    
    #defaults for form values
#    resp = app.request("/game", method="POST")  #must, must be all uppercase, or tests won't work
#    assert_response(resp, contains="action")
    
    #game
    resp = app.request("/game")
    assert_response(resp)
