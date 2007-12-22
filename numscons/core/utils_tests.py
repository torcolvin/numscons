#! /usr/bin/env python
# Last Change: Fri Nov 16 01:00 PM 2007 J

# test module for utils module
import os
import unittest

from utils import pkg_to_path, _rsplit

class PkgToPathTester(unittest.TestCase):
    def setUp(self):
        self.pkg1 = "foo"
        self.pkg2 = "foo.bar"

        self.path1_expected = "foo"
        self.path2_expected = "foo" + os.sep + "bar"

    def test1(self):
        assert pkg_to_path(self.pkg1) == self.path1_expected
        assert pkg_to_path(self.pkg2) == self.path2_expected

class RsplitTester(unittest.TestCase):
    def test1(self):
        a1 = 'a.b.c'
        assert a1.split('.', -1) == a1.rsplit('.', -1) == _rsplit(a1, '.', -1)
        assert a1.rsplit('.', 1) == _rsplit(a1, '.', 1)
        assert a1.rsplit('.', 0) == _rsplit(a1, '.', 0)
        assert a1.rsplit('.', 2) == _rsplit(a1, '.', 2)

    def test2(self):
        a2 = 'floupi'
        assert a2.rsplit('.') ==  _rsplit(a2, '.', -1)
        assert a2.rsplit('.', 1) == _rsplit(a2, '.', 1)

if __name__ == "__main__":
    unittest.main()