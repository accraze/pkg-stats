import gzip
import os
import urllib.request

from src.settings import MIRROR_DOMAIN


class Downloader:

    """Handle retrieval and decompression of contents file.
    """

    def download_contents_file(self, arch_type):
        """Retrieve contents file for given arch_type."""
        fname = 'Contents-{}.gz'.format(arch_type)
        outfile_path = fname[:-3]  # remove filetype ext
        if os.path.exists(outfile_path):
            print('Contents file already exists! Skipping download.')
            return outfile_path
        self._download(fname, outfile_path)
        return outfile_path

    def _download(self, fname, outfile_path):
        """Download and decode gzip contents file."""
        print('Download Contents file: {}'.format(fname))
        response = urllib.request.urlopen(MIRROR_DOMAIN + fname)
        with open(outfile_path, 'wb') as outfile:
            # decompress response into file on disk
            outfile.write(gzip.decompress(response.read()))
