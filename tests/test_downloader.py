import unittest
from unittest.mock import Mock, patch, mock_open

from src.downloader import Downloader


class TestDownloader(unittest.TestCase):

    def setUp(self):
        self.d = Downloader()

    def test_download_contents_file(self):
        download_mock_fn = Mock()
        self.d._download = download_mock_fn
        res = self.d.download_contents_file('amd-foo')
        expected = 'Contents-amd-foo'
        expected_ext = expected + '.gz'
        self.assertEquals(res, expected)
        self.d._download.assert_called_with(expected_ext, expected)

    @patch('urllib.request.urlopen')
    @patch('gzip.decompress')
    @patch("__main__.open", new_callable=mock_open, read_data="data")
    def test_download(self, mock_urlopen, mock_gzip, mock_open_handler):
        a = Mock()
        a.read.return_value = bytes('foo','utf-8')
        mock_urlopen.return_value = a
        mock_gzip.return_value = bytes('foo', 'utf-8')
        fpath = '/tmp/baz'
        fname = fpath.split('/')[-1]
        self.d._download(fname, fpath)
        mock_open_handler.assert_called_once()
