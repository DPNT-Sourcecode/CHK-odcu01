from typing import Dict, List, Tuple, NamedTuple
from math import floor


class PriceQty(NamedTuple):
    price: int
    qty: int


PriceQtyPairs = List[PriceQty]


class Item:
    def __init__(self, price_qty_list: PriceQtyPairs) -> None:
        self.price_qty_list = price_qty_list

    def checkout(self, qty: int) -> int:
        price = 0
        for price_qty in self.price_qty_list:
            discount_price_n = floor(qty / price.qty)
            qty = qty % self.special_offer_qty

        return (self.price * regular_price_n) + \
               (self.special_offer_price * discount_price_n)


PRICE_TABLE: Dict[str, Item] = {
    "A": Item([PriceQty(3, 130), PriceQty(1, 50)]),
    "B": Item([PriceQty(2, 45), PriceQty(1, 30)]),
    "C": Item([PriceQty(1, 20)]),
    "D": Item([PriceQty(1, 15)]),
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


