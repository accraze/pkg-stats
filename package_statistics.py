import sys

from src.downloader import Downloader
from src.parser import Parser
from src.settings import ARCH_TYPES


def get_pkg_stats(arch_type):
    # download contents file
    outfile_path = Downloader().download_contents_file(arch_type)
    # parse contents file and print top 10 files
    Parser().parse_contents_file(outfile_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception('Missing architecture type param')

    arch_type = sys.argv[1]
    if arch_type not in ARCH_TYPES:
        raise Exception('Architecture type must be one of {}'.format(
            ", ".join(ARCH_TYPES)))

    get_pkg_stats(arch_type)
