__author__ = "Pavlo Vozniuk"
__copyright__ = "Copyright 2017, Pavlo Vozniuk"
__license__ = "MIT"
__version__ = "0.1.1"

import math
import re

regex = r"([\d\.\-])([kMBTPE]*)"
millnames = ['', 'k', 'M', 'B', 'T', 'P', 'E']

# convert 1.1k to 1100
# 1.1kB is also converted to 1100
def parse_millify(string):
    parts = re.search("([-+]?\d*\.\d+|\d+)([kMBTPE]{0,1})([\S]*)", str(string))
    # print(string + ' -> ' + parts[1] + ' ' + parts[2]);

    if (parts[1]):
        multiply = 1;

        if (parts[2]):
            index = millnames.index(parts[2]);

            if (index):
                multiply = 1000 ** (index)

        return float(parts[1]) * multiply
    else:
        return 0

# convert 1100 to 1.1k
def millify(number, precision=0, ending='', suffix='', prefix=''):
    try:
        n = float(number)
        millidx = max(  0,
                        min(len(millnames) - 1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

        return '{prefix}{:.{prec}f}{suffix}{dx}{ending}'.format(n / 10**(3 * millidx), dx=millnames[millidx], prec=precision, ending=ending, prefix=prefix, suffix=suffix)
    except ValueError:
        return str(number)
