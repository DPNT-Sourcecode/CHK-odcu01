from typing import Dict, List, Tuple, NamedTuple
from math import floor


class Offer(NamedTuple):
    qty: int
    price: int


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


class InterItemPromotion(NamedTuple):
    



PRICE_TABLE: Dict[str, Item] = {
    "A": Item([Offer(qty=5, price=200), Offer(qty=3, price=130), Offer(qty=1, price=50)]),
    "B": Item([Offer(qty=2, price=45), Offer(qty=1, price=30)]),
    "C": Item([Offer(qty=1, price=20)]),
    "D": Item([Offer(qty=1, price=15)]),
    "E": Item([Offer(qty=1, price=40)]),
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





