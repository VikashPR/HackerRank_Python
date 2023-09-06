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

### Triangle Quest
```python
for i in range(1,int(input())):
    print(i * (pow(10, i) - 1)// 9)
```

### List Comprehensions
```python
import itertools

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])

```

### Find the Runner-Up Score!
```python
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))
    print(sorted(arr, reverse=True)[1])
```

### Nested Lists
```python
if __name__ == '__main__':
    records = []
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
        if score not in grades:
            grades.append(score)
    
    grades = sorted(grades)
    records = sorted(records, key = lambda x: x[0])
    
    
    second_lowers_grade = grades[1]
    
    for i in records:
        if i[1] == second_lowers_grade:
            print(i[0])
```

### Finding the percentage
```python
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg_list = list(student_marks.get(query_name))
    avg = sum(avg_list)/len(avg_list)
    print(f"{avg:.2f}")
```

### What's Your Name?

``` python
def print_full_name(first, last):

    print ("Hello",first,last+"!", "You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
```