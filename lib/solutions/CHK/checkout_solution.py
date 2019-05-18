class Item:
    def __init__(self, price: int, special_offer: tuple) -> None:
        self.price = price
        self.special_offer = special_offer

    def checkout(self, n: int) -> int:
        pass


PRICE_TABLE = {
    "A": Item(50, (3, 130)),
    "B": Item(30, (2, 130)),
    "C": Item(20, ()),
    "D": Item(15, ()),
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    pass



