from models import User


def test_db():
    User("99461", "Juan Jose", "STUDENT")
    User("9946", "Juan Jose", "PROFESSOR")

    print( User.login("9946") )

    User.add_note("99461", "Matemáticas", 5.0, 1)
    User.add_note("99461", "Matemáticas", 5.0, 2)
    User.add_note("99461", "Matemáticas", 5.0, 3)

    print( User.get_notes("99461", "Matemáticas") )

    User.add_note("99461", "Matemáticas", 3.0, 2)

    print( User.get_notes("99461", "Matemáticas") )


if __name__ == "__main__":
    test_db()
