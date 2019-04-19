import re
from collections import Counter

from src.settings import TOP_N
from src.utils import _print_column_keys, _print_header, _print_row


class Parser:

    """Parse a contents file stored on disk.
    This will also print out the top-n results
    based by number of files.
    """

    def __init__(self):
        self.pkg_files = {}

    def parse_contents_file(self, filepath):
        """Parse a file and print out the results."""
        self._parse(filepath)
        top_results = self._get_top_results()
        self._print_results(top_results)

    def _parse(self, filepath):
        """Read contents file line by line."""
        print('Parsing contents file...')
        self.fname = filepath.split('-')[-1]
        with open(filepath) as infile:
            for line in infile:
                self._parse_line(line)

    def _parse_line(self, line):
        """Parse a contents line and update pkg files list."""
        # split on whitespace and remove newline
        vals = re.split(r'\s+', line[:-1])
        pkg_names = vals[-1]  # pkg_name is in last column
        self._update_pkg_files(pkg_names)

    def _update_pkg_files(self, pkg_names):
        """Increment or initialize num file count for all pkgs."""
        for pkg_name in pkg_names.split(','):
            if not self.pkg_files.get(pkg_name):
                self.pkg_files[pkg_name] = 1
            else:
                self.pkg_files[pkg_name] += 1

    def _get_top_results(self):
        """Retrieve top-n pkgs. Returns list of tuples."""
        return Counter(self.pkg_files).most_common(TOP_N)

    def _print_results(self, results):
        """Display the top pkg names ordered by number of files."""
        _print_header(self.fname)
        _print_column_keys()
        for idx, result in enumerate(results):
            _print_row(idx, result)
        print('\n')
