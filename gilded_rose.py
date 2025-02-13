# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

class ItemStrategy(ABC):
    @abstractmethod
    def update_quality(self, item: Item) -> None:
        pass

class DefaultItemStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        if item.quality > 0:
            item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality = item.quality - 1

class AgedBrieStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        if item.quality < 50:
            item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality = item.quality + 1

class BackstagePassStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            item.quality = 0

class SulfurasStrategy(ItemStrategy):
    def update_quality(self, item: Item) -> None:
        # Sulfuras never decreases in quality and doesn't need to be sold
        pass

