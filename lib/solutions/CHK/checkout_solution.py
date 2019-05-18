from typing import Dict, List, Tuple


class Item:
    def __init__(self, price: int, special_offer: tuple) -> None:
        self.price = price
        self.special_offer = special_offer

    def checkout(self, qty: int) -> int:
        pass


PRICE_TABLE = {
    "A": Item(50, (3, 130)),
    "B": Item(30, (2, 130)),
    "C": Item(20, ()),
    "D": Item(15, ()),
}


def checkout_items(counter: dict) -> int:
    prices = []
    for sku, qty in counter.items():
        item = PRICE_TABLE[sku]
        prices.append(item.checkout(qty))

    return sum(prices)

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    counter = {sku: 0 for sku, _ in PRICE_TABLE.items()}

    for sku in skus:
        if sku not in counter:
            return -1
        counter[sku] += 1




