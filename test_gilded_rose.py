# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)
        sulfuras_item = items[0]
        self.assertEquals(80, sulfuras_item.quality)
        self.assertEquals(4, sulfuras_item.sell_in)
        self.assertEquals("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEquals(["Sulfuras"], all_items)

    # logical test-1
    def test_negative_item_quantity(self):
        # Test fails beacuse items cannot have negative quantity
        items = [Item("Aged Brie", 5,-10 )]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    # logical test-2
    def test_aged_brie_quality_over_50(self):
        # Test fails because Aged Brie can exceed quality 50 when multiple
        # quality increases are applied
        items = [Item("Aged Brie", -1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    # logical test-3
    def test_quality_degradation_after_sell_by(self):
        #Test fails because quality should degrade twice as fast after sell_in < 0
        items = [Item("regular item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    # syntax test-1
    def test_item_with_1_argument(self):
        # Test fails because quantity of argument
        items = [Item("Sulfuras")]
        gilded_rose = GildedRose(items)
        self.assertEquals(["Sulfuras"], all_items)

if __name__ == '__main__':
    unittest.main()
