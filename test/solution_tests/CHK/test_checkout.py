from lib.solutions.CHK.checkout_solution import checkout, Item


class TestCheckout:
    def test_checkout_error(self):
        invalid_inputs = (
            None, ["A"], 1, {"A": "A"}, "E", "ABCDE",
        )

        for input_ in invalid_inputs:
            assert checkout(input_) == -1

    def test_item_checkout(self):
        item = Item(10, (2, 15))

        assert item.checkout(1) == 10
        assert item.checkout(2) == 15
        assert item.checkout(3) == 25

        item = Item(10, (1, 10))

        assert item.checkout(1) == 10
        assert item.checkout(2) == 20
        assert item.checkout(3) == 30

    def test_checkout_ok(self):
        # well i am assuming that the input will be something like:
        # "ABAABC"

        in_out = {
            "": 0,  # not sure about this one
            "A": 50, "AB": 80, "C": 20,
            "CCCCC": 100, "AAA": 130, "AAAA": 180,
            "DABDBC": 145
        }

        for input_, output in in_out.items():
            assert checkout(input_) == output, input_
