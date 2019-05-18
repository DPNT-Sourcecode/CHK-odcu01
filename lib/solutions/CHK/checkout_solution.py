from typing import Dict, Tuple
from math import floor

class Item:
    def __init__(self, price: int, special_offer: Tuple[int, int] = None) -> None:
        self.price = price
        self._special_offer = special_offer

    @property
    def special_offer_qty(self):
        return self._special_offer[0]

    @property
    def special_offer_price(self):
        return self._special_offer[1]

    def checkout(self, qty: int) -> int:
        regular_price_n = qty % self.special_offer_qty
        discout_price_n = qty / self.special_offer_qty


PRICE_TABLE: Dict[str, Item] = {
    "A": Item(50, (3, 130)),
    "B": Item(30, (2, 130)),
    "C": Item(20),
    "D": Item(15),
}


class SkuNotFoundException(Exception):
    pass


def checkout_items(counter: Dict[str, int]) -> int:
    prices = []
    for sku, qty in counter.items():
        item = PRICE_TABLE[sku]
        prices.append(item.checkout(qty))

    return sum(prices)


def count_items(skus: str) -> Dict[str, int]:
    counter = {sku: 0 for sku, _ in PRICE_TABLE.items()}

    for sku in skus:
        if sku not in counter:
            raise SkuNotFoundException(f"sku not found: {sku}")
        counter[sku] += 1

    return counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    try:
        counter = count_items(skus)
    except SkuNotFoundException:
        return -1

    return checkout_items(counter)







