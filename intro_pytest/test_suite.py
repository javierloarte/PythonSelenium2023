
class TestLogin:

    @classmethod
    def setup_class(cls):
        print("*" * 80)
        print(f"CLASS SETUP - Crear usuario con la llamada a la BD")
        print("*" * 80)

    def setup_method(self):
        print("*" * 80)
        print(f"METHOD SETUP - Abrir un nuevo navegador")
        print("*" * 80)

    def test_login(self):
        print("Login Test")

    def test_invalid_login(self):
        print("Invalid login Test")

    Luis
    M
    Rivas
    Zepeda
    21: 10


class TestLogin:
    @classmethod
    def setup_class(cls):
        print("*" * 80)
        print(f"CLASS SETUP - Crear usuarios con llamadas a DB")
        print("*" * 80)

    def setup_method(self):
        print("*" * 80)
        print(f"METHOD SETUP - Abrir un nuevo navegador")
        print("*" * 80)

    def test_login(self):
        print("Login test")

    def test_invalid_logic(self):
        print("Invalid login test")

    def teardown_method(self):
        print("*" * 80)
        print(f"TEARDOWN SETUP - Cerrar el navegador")
        print("*" * 80)

    @classmethod
    def teardown_class(cls):
        print("*" * 80)
        print(f"TEARDOWN SETUP - limpiar usuario con la llamada a la BD")
        print("*" * 80)