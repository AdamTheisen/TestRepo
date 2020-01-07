import testrepo

def test_hello():
    result = testrepo.hello.hello_world.hello_world()
    assert result == 'Hello World'
