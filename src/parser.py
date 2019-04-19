import re
from collections import Counter


class Parser:

    pkg_files = {}

    def parse_contents_file(self, filepath):
        self._parse(filepath)
        self._print_results()

    def _parse(self, filepath):
        """Read contents file line by line."""
        print('Parsing contents file...')
        self.fname = filepath.split('-')[-1]
        with open(filepath) as infile:
            for line in infile:
                self._parse_line(line)

    def _parse_line(self, line):
        """Parse a contents line and update pkg files list."""
        vals = re.split(r'\s+', line[:-1])
        pkg = vals[-1]
        if not self.pkg_files.get(pkg):
            self.pkg_files[pkg] = 1
        else:
            self.pkg_files[pkg] += 1

    def _get_top_results(self):
        """Retrieve top 10 pkgs. Returns list of tuples."""
        return Counter(self.pkg_files).most_common(10)

    def _print_results(self):
        """Display the top pkg names ordered by number of files."""
        self._print_header()
        top_results = self._get_top_results()
        print('   {:<20} \t {: <20}'.format('pkg_name', 'num_files'))
        for idx, result in enumerate(top_results):
            print('{}. {:<20} \t {: <20}'.format(idx+1, result[0], result[1]))

        print('\n')

    def _print_header(self):
        bumper = ''.join(['*' for x in range(42)])
        print('\n' + bumper)
        print('Top 10 Packages for {}'.format(self.fname))
        print(bumper)

