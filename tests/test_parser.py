import unittest

from src.parser import Parser


class TestParser(unittest.TestCase):

    def setUp(self):
        self.p = Parser()

    def test_parse_line(self):
        self.assertEquals(self.p.pkg_files, {})
        line = '/some/dir/with/files        foo/bar\n'
        self.p._parse_line(line)
        self.assertEquals(self.p.pkg_files, {'foo/bar': 1})

    def test_update_pkg_files(self):
        self.assertEquals(self.p.pkg_files, {})
        self.p._update_pkg_files('foo')
        self.assertEquals(self.p.pkg_files, {'foo': 1})
        self.p._update_pkg_files('foo')
        self.assertEquals(self.p.pkg_files, {'foo': 2})

    def test_get_top_results(self):
        pkg_files = {'foo': 123, 'bar': 456, 'baz': 789, 'zab': 333, 'rab': 212,
                     'oof': 455, 'eeg': 223, 'eeeeght': 32, 'neeen': 212,
                     'teeen': 100}
        self.p.pkg_files = pkg_files
        res = self.p._get_top_results()
        expected = [('baz', 789), ('bar', 456), ('oof', 455), ('zab', 333),
                    ('eeg', 223), ('rab', 212), ('neeen', 212), ('foo', 123),
                    ('teeen', 100), ('eeeeght', 32)]
        self.assertEquals(res, expected)
