# Short numbers

A Python package to display big numbers in short format and vice-versa, parse short format and return an origin value. 

e.g. it can format number `25300` as `25.3k` and convert `25.3k` to `25300`

## Usage

### Format numbers in short format 

```python
from shortnumbers import millify

millify(1000); # -> '1k'
millify(5678000); # -> '6M'
millify(-2000); # -> '-2k'
millify(-30000000000.12); # -> '-30B'
millify(12345, precision=2); # -> '12.35k'
millify(12345, precision=2, suffix=" ", ending="B"); # -> '12.35 kB'
millify(12345, precision=2, prefix="$"); # -> '$12.35k'
```

### Parse short format as an origina value

```python
from shortnumbers import parse_millify

parse_millify("0"); # -> 0.0
parse_millify("1"); # -> 1.0
parse_millify("1k"); # -> 1000.0
parse_millify("-1.56k"); # -> -1560.0
parse_millify("24.5MB"); # -> 24500000.0
parse_millify("24.5B"); # -> 24500000000.0
```
