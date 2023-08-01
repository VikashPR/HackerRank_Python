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
    
    if n >= -1:
        for i in range(n):
            print(pow(i,2))
```

## Print Function
```python
if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n+1):
        print(i, end="")
```

## Write a function
```python
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True; 
    if year % 100 == 0:
            leap = False;
            if year % 100 == 0 and year % 400 == 0:
                leap = True;    
    return leap
```

## List Comprehensions
```python
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    newList = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(newList)
```

## Find the Runner-Up Score!
```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    setList = set(list(arr))
    setList = sorted(setList, reverse=True)
    print(setList[1])
```
