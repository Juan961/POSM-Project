from models import User


def test_db():
    User("99461", "Juan Jose", "STUDENT")
    User("9946", "Juan Jose", "PROFESSOR")

    print( User.login("9946") )

if __name__ == "__main__":
    test_db()
