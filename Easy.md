## Hello World!
``` python
if __name__ == '__main__':
    print ("Hello, World!")
```

## Python If-Else
```python
#!/bin/python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(raw_input().strip())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

```

## Arithmetic Operators
```python
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
# Solution Starts

    addTwo = a + b
    diffTwo = a - b
    proTwo = a * b

    print(addTwo)
    print(diffTwo)
    print(proTwo)

```

## Python: Division
```python
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
# Solution starts
    one = a // b
    two = a / b
    print(one);
    print(two)
```

## Loops
```python
if __name__ == '__main__':
    n = int(input())
    
    for i in range(5):
        print(pow(i,2))
```
