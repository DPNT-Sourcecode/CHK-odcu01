from lib.solutions.HLO.hello_solution import hello


class TestHello:
    def test_hello(self):
        assert hello("John") == "Hello, John!"

        assert hello("my friend") == "Hello, my friend!"
