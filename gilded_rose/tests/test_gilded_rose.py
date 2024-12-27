# -*- coding: utf-8 -*-
import unittest
import approvaltests

from gilded_rose import Item, GildedRose

def test_update_quality():
    names = ["foo"]
    sell_ins = [0]
    qualitys = [0]

    approvaltests.verify_all_combinations(
        update_quality_for_item,
        [
            names,
            sell_ins,
            qualitys,
        ],
        formatter=update_quality_printer
    )

def update_quality_for_item(name, sell_in, quality):
    item = Item(name, sell_in, quality)
    items = [item]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    return item

def update_quality_printer(args, result):
    return f"{args} => {print_item(result)}"

def print_item(item):
    return f"Item({item.name}, sell_in={item.sell_in}, quality={item.quality})"
