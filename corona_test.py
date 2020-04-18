#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:38:08 2020

@author: dredmond
"""

import unittest

import corona2

class TestCorona(unittest.TestCase):

    def setUp(self):
        self.contents = corona2.get_page_contents()

    def test_get_page(self):
        self.assertTrue(len(self.contents) > 0)

    def test_convert_to_soup(self):
        self.assertTrue(corona2.convert_to_soup(self.contents) is not None)

if __name__ == '__main__':
    unittest.main()
