# Documentation
This project include ```.py``` files with names of mathematics shapes.
Example: ```circle.py``` .

In this files realisation of area and perimeter of shapes by math formulas.
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2  

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
## Functions
### circle.py
In this file realisation of area and perimeter of circle.

**_Area function_**
```python
def area(r):
    return math.pi * r * r
``` 
Function call
```python
print(area(5))
```

Print in command line _3,14 * 5<sup>2</sup>_.

**_Perimeter fucntion_**
```python
def perimeter(r):
    return 2 * math.pi * r
```
Function call
```python
print(perimeter(5))
``` 

print in command line 
_2 * 3,14 * 5_.
### rectangle.py
In this file realisation of area and perimeter of rectangle.

**_Area function_**
```python
def area(a, b): 
    return a * b
```
Function call
 ```python
print(area(1, 2))
```

Print in command line _2_.

**_Perimeter function_**
```python
def perimeter(a, b):
    return 2 * (a + b)
```
Function call 
```python
print(perimeter(1, 2))
```

Print in command line _6_.
### square.py
In this file realisation of area and perimeter of square

**_Area function_**
```python
def area(a):
    return a * a
```
Function call  
```python
print(area(6))
```

Print in command line _36_.

**_Perimeter fucntion_**
```python
def perimeter(a):
    return 4 * a
```
Function call 
```python
print(perimeter(6))
```

Print in command line _24_.
### triangle.py
In this file realisation of area and perimeter of triangle

**_Area function_**
```python
def area(a, h): 
    return a * h / 2 
```
Function call 
```python
print(area(5, 10))
```

Print in command line _25_.

**_Perimeter function_**
```python
def perimeter(a, b, c): 
    return a + b + c
```
Function call 
```python
print(perimeter(5, 6, 6))
```

Print in command line _17_.
## Tests
Tests were added to verify the functionality and parameter handling of geometric functions. Each function was tested for correct outputs, boundary conditions, and error handling. Below are the details:
### Circle Tests
- **`area(radius)`**:
  - Added tests for positive values, such as `radius=10`, with expected result `314.16`.
  - Boundary test: `radius=0` → expected result `0`.
  - Error handling: negative radius (`radius=-5`) throws `ValueError`, and non-numeric radius (`radius="abc"`) throws `TypeError`.
- **`perimeter(radius)`**:
  - Tested for correct calculation: `radius=10` → expected result `62.83`.
  - Boundary test: `radius=0` → expected result `0`.
  - Error handling: `radius=-5` throws `ValueError`, `radius="abc"` throws `TypeError`.

### Rectangle Tests
- **`area(length, width)`**:
  - Verified calculations for `length=5, width=10` → expected result `50`.
  - Boundary test: `length=0, width=10` → expected result `0`.
  - Error handling: `length=-5` throws `ValueError`, `width="abc"` throws `TypeError`.
- **`perimeter(length, width)`**:
  - Tested for `length=5, width=10` → expected result `30`.
  - Error handling: `length=0` throws `Exception`, `width=-10` throws `ValueError`.

### Square Tests
- **`area(side)`**:
  - Verified calculations for `side=4` → expected result `16`.
  - Boundary test: `side=0` → expected result `0`.
  - Error handling: `side=-4` throws `ValueError`, `side="abc"` throws `TypeError`.
- **`perimeter(side)`**:
  - Tested for `side=4` → expected result `16`.
  - Error handling: `side=-4` throws `ValueError`.

### Triangle Tests
- **`area(base, height)`**:
  - Verified calculations for `base=6, height=4` → expected result `12`.
  - Error handling: `base=-6` throws `ValueError`, `height="abc"` throws `TypeError`.
- **`perimeter(a, b, c)`**:
  - Verified for `a=3, b=4, c=5` → expected result `12`.
  - Error handling: invalid triangle sides (`a=1, b=2, c=4`) throw `Exception`, and non-numeric side (`a="abc"`) throws `TypeError`.

## History of commits
```bash
* commit 140186a3cd52d1fe8e66e26955164b5b20dd781b
| Author: redkarasik <redkarasik@yandex.ru>
| Date:   Thu Oct 17 15:59:58 2024 +0300
| 
|     Add description of functions
| 
* commit 9154b122f907dec566303f3b3a36aec536463bdb
| Author: redkarasik <redkarasik@yandex.ru>
| Date:   Fri Sep 20 10:47:40 2024 +0300
| 
|     Fix mistake with perimetr in rectangle.py
| 
* commit f10a83571dce5902ed42f2fcaef046475a98182b
| Author: redkarasik <redkarasik@yandex.ru>
| Date:   Fri Sep 20 10:45:55 2024 +0300
| 
|     Add triangle.py
| 
* commit 3cb62b71ce74e174e32609aaf5625b2a123eab96
| Author: redkarasik <redkarasik@yandex.ru>
| Date:   Fri Sep 20 10:41:14 2024 +0300
| 
|     Add file rectangle.py
| 
* commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
| Author: smartiqa <info@smartiqa.ru>
| Date:   Thu Mar 4 14:55:29 2021 +0300
| 
|     L-03: Docs added
| 
* commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300
  
      L-03: Circle and square added
```