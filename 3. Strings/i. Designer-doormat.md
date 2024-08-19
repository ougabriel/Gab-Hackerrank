###autor: Ugochi Gabriel Okom
###19/08/2024

Let's break down how text alignment and the design function work in a simpler way. I'll explain it step by step, focusing on how to generate patterns and align them in the center.

### 1. **Text Alignment Basics**
Text alignment means positioning text within a certain width. In Python, you can use the `center()` method to align text within a specified width by padding it with a specified character.

**Example:**
```python
text = 'Hello'
print(text.center(11, '-'))
```
**Output:**
```
---Hello---
```

- **`center(11, '-')`**: This tells Python to center the text 'Hello' in a string of width 11, using `-` to fill the empty space on both sides.

### 2. **Pattern Generation**
The design involves repeating a pattern like `.|.` multiple times and centering it within a line of a specific width.

**Example:**
- Suppose we want to generate a line with `.|.` repeated 3 times and centered in a width of 15.

```python
pattern = '.|.'
print((pattern * 3).center(15, '-'))
```
**Output:**
```
--.|..|..|.--
```

### 3. **Building the Design Step by Step**
Let's build the door mat design one step at a time.

#### **Step 1: Understanding the Design Layout**
- **Size**: The mat has `N` rows and `M` columns.
  - `N` is odd (e.g., `7`).
  - `M` is `3 * N` (e.g., `21` when `N = 7`).
- The design has three parts:
  1. **Top Half**: Increasing patterns.
  2. **Middle Line**: The word "WELCOME".
  3. **Bottom Half**: Decreasing patterns (mirrors the top half).

#### **Step 2: Top Half**
The top half starts with a single `.|.` in the middle and increases by adding more `.|.` patterns.

- For `N = 7`, `M = 21`:
  
```python
N = 7
M = 21

for i in range(1, N, 2):  # Start at 1, end at N, step by 2
    print((i * '.|.').center(M, '-'))
```

**How It Works:**
- The loop starts at `1` and increases by `2` each time (1, 3, 5, ...).
- For each `i`, the pattern `.|.` is repeated `i` times.
- The result is centered within a width of `21` using `-`.

**Top Half Output:**
```
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
```

#### **Step 3: Middle Line**
This line simply centers the word "WELCOME".

```python
print('WELCOME'.center(M, '-'))
```

**Middle Line Output:**
```
-------WELCOME-------
```

#### **Step 4: Bottom Half**
This part mirrors the top half, but in reverse order.

```python
for i in range(N-2, -1, -2):  # Start at N-2, go down to 1, step by -2
    print((i * '.|.').center(M, '-'))
```

**How It Works:**
- The loop starts at `N-2` (e.g., `5` for `N = 7`) and decreases by `2` each time.
- The pattern is printed and centered, just like in the top half.

**Bottom Half Output:**
```
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
```

### 4. **Full Code Example**
```python
N = 7  # Number of rows (odd)
M = 21  # Number of columns (3 times N)

# Top half
for i in range(1, N, 2):
    print((i * '.|.').center(M, '-'))

# Middle part with 'WELCOME'
print('WELCOME'.center(M, '-'))

# Bottom half
for i in range(N-2, -1, -2):
    print((i * '.|.').center(M, '-'))
```

### Final Output:
```
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
```

This approach breaks down the process into manageable parts. Start by generating and aligning simple patterns, then build the full design by combining these elements.