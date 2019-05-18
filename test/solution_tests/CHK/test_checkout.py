from typing import Dict

from lib.solutions.CHK.checkout_solution import (InterItemPromotion, Item,
                                                 Offer,
                                                 apply_inter_item_promotions,
                                                 checkout)


class TestItem:
    def test_item_checkout_simple_item(self) -> None:
        item = Item([Offer(qty=1, price=10)])

        assert item.checkout(1) == 10
        assert item.checkout(2) == 20
        assert item.checkout(3) == 30

    def test_item_checkout_single_discount(self) -> None:
        item = Item([Offer(qty=2, price=15), Offer(qty=1, price=10)])

        assert item.checkout(1) == 10
        assert item.checkout(2) == 15
        assert item.checkout(3) == 25

    def test_item_checkout_multi_discount(self) -> None:
        item = Item(
            [Offer(qty=3, price=12), Offer(qty=2, price=15), Offer(qty=1, price=10)]
        )

        assert item.checkout(1) == 10
        assert item.checkout(2) == 15
        assert item.checkout(3) == 12
        assert item.checkout(4) == 22
        assert item.checkout(5) == 27
        assert item.checkout(6) == 24


class TestInterItemPromotions:
    def test_inter_promotions(self) -> None:
        promotions = [
            InterItemPromotion(src_item="A", src_qty=2, dest_item="B", dest_qty=-1),
            InterItemPromotion(src_item="C", src_qty=1, dest_item="D", dest_qty=-1),
            InterItemPromotion(src_item="E", src_qty=1, dest_item="F", dest_qty=-1),
            InterItemPromotion(src_item="G", src_qty=3, dest_item="G", dest_qty=-1),
        ]

        counter: Dict[str, int] = {"A": 5, "B": 3, "C": 1, "D": 10, "E": 1, "F": 0, "G": 3}
        apply_inter_item_promotions(promotions, counter)

        assert len(counter) == 7
        assert counter["A"] == 5
        assert counter["B"] == 1
        assert counter["C"] == 1
        assert counter["D"] == 9
        assert counter["E"] == 1
        assert counter["F"] == 0
        assert counter["G"] == 2


class TestCheckout:
    def test_checkout_error(self) -> None:
        invalid_inputs = (None, ["A"], 1, {"A": "A"}, "X", "ABCDX")

        for input_ in invalid_inputs:
            assert checkout(input_) == -1  # type: ignore

    def test_checkout_no_error(self) -> None:
        input_ = "ABCDE"
        assert checkout(input_) > 0

    def test_checkout_ok(self) -> None:
        in_out = {
            "": 0,
            "A": 50,
            "AB": 80,
            "C": 20,
            "AAA": 130,
            "AAAA": 180,
            "AAAAA": 200,
            "AAAAAA": 250,
            "CCCCC": 100,
            "EE": 80,
            "DABDBC": 145,
            "BE": 70,
            "BEE": 80,
            "BBEE": 110,
            "BBBEE": 125,
            "BBBEEE": 165,
            "BBBEEEE": 190,
            "F": 10,
            "FF": 20,
            "FFF": 20,
        }

        for input_, output in in_out.items():
            assert checkout(input_) == output, input_
