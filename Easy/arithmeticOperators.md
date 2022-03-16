## Task 
The provided code stub reads two integers from STDIN, ***a***  and ***b***. Add code to print three lines where:

1) The first line contains the sum of the two numbers.

1) The second line contains the difference of the two numbers (first - second).

1) The third line contains the product of the two numbers.

## Example 

***a = 3***

***b = 5***

Print the following:
```
8

-2

15
```

## Input Format

The first line contains the first integer, ***a***. 

The second line contains the second integer, ***b***.

## Constraints

***1 ≤ a ≤ 10²***

***1 ≤ b ≤ 10²***

## Output Format

Print the three lines as explained above.

## Sample Input 0
```
3
2
```
## Sample Output 0
```
5
1
6
```

## Explanation 0

***3 + 2 ⇒ 5***

***3 - 2 ⇒ 1***

***3 * 2 ⇒ 5***

# Solution
```
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
# Solution Starts
    
    addTwo = a + b;
    diffTwo = a - b;
    proTwo = a * b;
    
    print(addTwo);
    print(diffTwo);
    print(proTwo);
    
# Solution Ends
    
```
# Submission Code

<img src="../output/arithmeticOperators_output.png">