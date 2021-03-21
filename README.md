# flatten_xyz
Flatten arrays projects


## Install

```sh
pip install flatten-xyz
```

## Meta
License: BSD 2-clause

Author: Adrian Meza

Requires: Python >=3.6

## Example

```python
from flatten_xyz import flatten

f =  flatten.Flatten()
f.flatten([1, [2, [3, [4, 5]]]])

# Result: [1, 2, 3, 4, 5]
```

## Test

```sh
python3 -m pytest
```


