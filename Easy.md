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