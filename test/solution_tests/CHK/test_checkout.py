from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout:
    def test_checkout_error(self):
        invalid_inputs = (
            None, ["A"], 1, {"A": "A"}, "D"
        )

        for input_ in invalid_inputs:
            assert checkout(input_) == -1

    

