# -*- coding: utf-8 -*-
import unittest

import unittest
from gilded_rose import Item, GildedRose, DefaultItemStrategy, AgedBrieStrategy, BackstagePassStrategy, SulfurasStrategy



class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    def test_default_item_quality_decrease(self):
        item = Item("regular item", 5, 10)
        strategy = DefaultItemStrategy()
        strategy.update_quality(item)
        self.assertEqual(9, item.quality)  
        self.assertEqual(4, item.sell_in)  

    def test_aged_brie_quality_increase(self):
        item = Item("Aged Brie", 5, 10)
        strategy = AgedBrieStrategy()
        strategy.update_quality(item)
        self.assertEqual(11, item.quality)  
        self.assertEqual(4, item.sell_in)   

    def test_backstage_pass_quality_rules(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 8, 20)
        strategy = BackstagePassStrategy()
        strategy.update_quality(item)
        self.assertEqual(22, item.quality)  
        self.assertEqual(7, item.sell_in)   

    # Syntax Test
    def test_strategy_inheritance(self):
        strategies = [
            DefaultItemStrategy(),
            AgedBrieStrategy(),
            BackstagePassStrategy(),
            SulfurasStrategy()
        ]
        
        for strategy in strategies:
            self.assertTrue(hasattr(strategy, 'update_quality'))
            self.assertTrue(callable(getattr(strategy, 'update_quality')))

if __name__ == '__main__':
    unittest.main()
