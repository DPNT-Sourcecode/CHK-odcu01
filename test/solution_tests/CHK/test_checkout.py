from lib.solutions.CHK.checkout_solution import checkout, Item, Offer


class TestItem:
    def test_item_checkout_simple_item(self):
        item = Item([Offer(qty=1, price=10)])

        assert item.checkout(1) == 10
        assert item.checkout(2) == 20
        assert item.checkout(3) == 30

    def test_item_checkout_single_discount(self):
        item = Item([Offer(qty=2, price=15),
                     Offer(qty=1, price=10)])

        assert item.checkout(1) == 10
        assert item.checkout(2) == 15
        assert item.checkout(3) == 25

    def test_item_checkout_multi_discount(self):
        item = Item([Offer(qty=3, price=12),
                     Offer(qty=2, price=15),
                     Offer(qty=1, price=10)])

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

    def test_checkout_no_error(self):
        input_ = "ABCDE"
        assert checkout(input_) > 0

    def test_checkout_ok(self):
            in_out = {
                "": 0,
                "A": 50, "AB": 80, "C": 20,
                "AAA": 130, "AAAA": 180, "AAAAA": 200, "AAAAAA": 250,
                "CCCCC": 100,
                "DABDBC": 145,
                # "BE": 70, "BEE": 80, "BBEE": 110, "BBBEE": 125, "BBBEEE": 165, "BBBEEEE": 190
            }

            for input_, output in in_out.items():
                assert checkout(input_) == output, input_


