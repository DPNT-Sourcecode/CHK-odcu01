from math import floor
from typing import Dict, List, NamedTuple


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


PRICE_TABLE: Dict[str, Item] = {
    "A": Item(
        [Offer(qty=5, price=200), Offer(qty=3, price=130), Offer(qty=1, price=50)]
    ),
    "B": Item([Offer(qty=2, price=45), Offer(qty=1, price=30)]),
    "C": Item([Offer(qty=1, price=20)]),
    "D": Item([Offer(qty=1, price=15)]),
    "E": Item([Offer(qty=1, price=40)]),
    "F": Item([Offer(qty=1, price=10)]),
    "G": Item([Offer(qty=1, price=20)]),
    "H": Item([Offer(qty=10, price=80), Offer(qty=5, price=45), Offer(qty=1, price=10)]),
    "I": Item([Offer(qty=1, price=35)]),
    "J": Item([Offer(qty=1, price=60)]),
    "K": Item([Offer(qty=2, price=120), Offer(qty=1, price=70)]),
    "L": Item([Offer(qty=1, price=90)]),
    "M": Item([Offer(qty=1, price=15)]),
    "N": Item([Offer(qty=1, price=40)]),
    "O": Item([Offer(qty=1, price=10)]),
    "P": Item([Offer(qty=5, price=200), Offer(qty=1, price=50)]),
    "Q": Item([Offer(qty=3, price=80), Offer(qty=1, price=30)]),
    "R": Item([Offer(qty=1, price=50)]),
    "S": Item([Offer(qty=1, price=20)]),
    "T": Item([Offer(qty=1, price=20)]),
    "U": Item([Offer(qty=1, price=40)]),
    "V": Item([Offer(qty=3, price=130), Offer(qty=2, price=90), Offer(qty=1, price=50)]),
    "W": Item([Offer(qty=1, price=20)]),
    "X": Item([Offer(qty=1, price=17)]),
    "Y": Item([Offer(qty=1, price=20)]),
    "Z": Item([Offer(qty=1, price=21)]),
}


class InterItemPromotion(NamedTuple):
    src_item: str
    src_qty: int
    dest_item: str
    dest_qty: int


INTER_ITEM_PROMOTIONS: List[InterItemPromotion] = [
    InterItemPromotion(src_item="E", src_qty=2, dest_item="B", dest_qty=-1),
    InterItemPromotion(src_item="F", src_qty=3, dest_item="F", dest_qty=-1),
    InterItemPromotion(src_item="N", src_qty=3, dest_item="M", dest_qty=-1),
    InterItemPromotion(src_item="R", src_qty=3, dest_item="Q", dest_qty=-1),
    InterItemPromotion(src_item="U", src_qty=4, dest_item="U", dest_qty=-1),
]


class GroupPromotion:
    pass


class SkuNotFoundException(Exception):
    pass


def count_items(skus: str) -> Dict[str, int]:
    counter = {sku: 0 for sku, _ in PRICE_TABLE.items()}

    for sku in skus:
        if sku not in counter:
            raise SkuNotFoundException(f"sku not found: {sku}")
        counter[sku] += 1

    return counter


def apply_inter_item_promotions(
        promotions: List[InterItemPromotion], counter: Dict[str, int]
) -> None:
    for promo in promotions:
        n = floor(counter[promo.src_item] / promo.src_qty)
        counter[promo.dest_item] += promo.dest_qty * n
        if counter[promo.dest_item] < 0:
            counter[promo.dest_item] = 0


def checkout_items(counter: Dict[str, int]) -> int:
    prices = []
    for sku, qty in counter.items():
        item = PRICE_TABLE[sku]
        price = item.checkout(qty)
        prices.append(price)

    return sum(prices)


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str):
        return -1

    try:
        counter = count_items(skus)
    except SkuNotFoundException:
        return -1

    apply_inter_item_promotions(INTER_ITEM_PROMOTIONS, counter)

    return checkout_items(counter)


