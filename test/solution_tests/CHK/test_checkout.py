from lib.solutions.CHK.checkout_solution import checkout, Item


class TestItem:
    def test_item_checkout_simple_item(self):
        item = Item(10, (1, 10))

        assert item.checkout(1) == 10
        assert item.checkout(2) == 20
        assert item.checkout(3) == 30

    def test_item_checkout_single_discount(self):
        item = Item(10, ((2, 15)))

        assert item.checkout(1) == 10
        assert item.checkout(2) == 15
        assert item.checkout(3) == 25

    def test_item_checkout_multi_discount(self):
        item = Item(10, ((2, 15), (3, 12)))

        assert item.checkout(1) == 10
        assert item.checkout(2) == 15
        assert item.checkout(3) == 12
        assert item.checkout(4) == 22
        assert item.checkout(5) == 27
        assert item.checkout(6) == 24


class TestCheckout:
    def test_checkout_error(self):
        invalid_inputs = (
            None, ["A"], 1, {"A": "A"}, "X", "ABCDX",
        )

        for input_ in invalid_inputs:
            assert checkout(input_) == -1

def test_checkout_ok(self):
        in_out = {
            "": 0,  # not sure about this one
            "A": 50, "AB": 80, "C": 20,
            "CCCCC": 100, "AAA": 130, "AAAA": 180,
            "DABDBC": 145,

        }

        for input_, output in in_out.items():
            assert checkout(input_) == output, input_




