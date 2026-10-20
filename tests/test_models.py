from models import User


def test_user_password_hashing():

    user = User(username="Dirk")
    user.set_password("secret_test_password")

    assert user.check_password("wrong_password") == False
    assert user.check_password("secret_test_password") == True