from typing import Dict, List, Tuple
from math import floor


PriceQtyPairs = List[Tuple[int, int]]


class Item:
    def __init__(self, price_qty_list: PriceQtyPairs) -> None:
        self.price_qty_list = price_qty_list

    def checkout(self, qty: int) -> int:
        price = 0
        for price_qty in self.price_qty_list:
            discount_price_n = floor(qty / self.special_offer_qty)
            qty = qty % self.special_offer_qty

        return (self.price * regular_price_n) + \
               (self.special_offer_price * discount_price_n)


PRICE_TABLE: Dict[str, Item] = {
    "A": Item([(1, 50), (3, 130)]),
    "B": Item([(1, 30), (2, 45)]),
    "C": Item([(1, 20)]),
    "D": Item([(1, 15)]),
}


class SkuNotFoundException(Exception):
    pass


def checkout_items(counter: Dict[str, int]) -> int:
    prices = []
    for sku, qty in counter.items():
        item = PRICE_TABLE[sku]
        price = item.checkout(qty)
        prices.append(price)

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

