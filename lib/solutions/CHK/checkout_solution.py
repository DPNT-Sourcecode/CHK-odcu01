from typing import Dict, List, Tuple, NamedTuple
from math import floor


class Offer(NamedTuple):
    price: int
    qty: int


class Item:
    def __init__(self, offers: List[Offer]) -> None:
        self.offers = offers

    def checkout(self, qty: int) -> int:
        price = 0
        for offer in self.offers:
            n = floor(qty / offer.qty)
            qty = qty % offer.qty
            price += n * offer.price

        return price


PRICE_TABLE: Dict[str, Item] = {
    "A": Item([Offer(3, 130), Offer(1, 50)]),
    "B": Item([Offer(2, 45), Offer(1, 30)]),
    "C": Item([Offer(1, 20)]),
    "D": Item([Offer(1, 15)]),
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



