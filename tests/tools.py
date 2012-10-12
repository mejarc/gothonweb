from nose.tools import *
import re  #what's this? Oh, reg ex

def assert_response(resp, contains=None, matches=None, headers=None, status="200"): 
#    assert status in resp.status, "Generic error message: Expected response %r isn't in %r" % (status, resp.status)
    
    if status == "200":
        assert resp.data, "Empty response"
        
    if contains:
        assert contains in resp.data, "Response didn't contain %r" % contains
    
    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response doesn't match %r" % matches
    
    if headers:
        assert_equal(resp.header, headers)