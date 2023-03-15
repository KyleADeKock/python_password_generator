import password_generator

# no two passwords should be identical therefore,
# running this many times using pytest will allow us to see if any passwords are identical
def test_password_generator():
    temp1 = password_generator.password_generator()
    temp2 = password_generator.password_generator()
    assert temp1 != temp2

# are we connecting to the home page?
def test_home_page():
    with password_generator.app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

# Please Note:    
# pip install pytest-repeat
# run pytest --count=100 test_password_generator.py in cmd
# if you wish to test the randomness of password_generator
