### Hello World
```python
print("Hello, World!")
```

### If-Else
```python
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif n% 2 == 0:
        if n>= 2 and n<= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        else:
            print("Not Weird")
```

### Arithmetic Operators
```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
```

### Python: Division
```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)
```

### Loops
```python
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i*i, end="\n")
```

### Write a function
```python
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0: 
            leap = False
            if year % 400 == 0: 
                leap = True 
        else:
            leap = True       
    else:
        leap = False
    
    return leap

year = int(input())
print(is_leap(year))
```

### Print Function
```python
if __name__ == '__main__':
    n = int(input())
    
    for i in range(1, n+1):
        print(i, end="")
```

### Power - Mod Power
```python
a = int(input())
b = int(input())
m = int(input())

print(pow(a,b))

print(pow(a,b,m))
```

### Integers Come In All Sizes
```python
print(pow(a,b) + pow(c, d))
```