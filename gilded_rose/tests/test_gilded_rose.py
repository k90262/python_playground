# -*- coding: utf-8 -*-
import unittest

import approvaltests

from gilded_rose import Item, GildedRose


def print_item(item):
    return f"Item({item.name}, sell_in={item.sell_in}, quality={item.quality})"


def test_update_quality():
    item = Item("foo", 0, 0)
    items = [item]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    approvaltests.verify(print_item(item))


