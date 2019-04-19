from src.settings import TOP_N


def _print_header(fname):
    bumper = ''.join(['*' for x in range(42)])
    print('\n' + bumper)
    print('Top {} Packages for {}'.format(TOP_N, fname))
    print(bumper)


def _print_column_keys():
    print('   {:<20} \t {: <20}'.format('pkg_name', 'num_files'))


def _print_row(idx, result):
    print('{}. {:<20} \t {: <20}'.format(idx+1, result[0], result[1]))
