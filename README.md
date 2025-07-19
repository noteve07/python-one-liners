# 🐍 Python One-Liners

Welcome to **Python One-Liners**!  
This repository is a collection of codes that I wrote for fun at the end of my 11th Grade. While most have little practical use, they were a great way to boost my problem-solving skills and deepen my understanding of Python syntax. 

no semicolons ;)

---

## 🚀 What You'll Find

- Short, often single-line, Python scripts and tricks
- Creative uses of Python syntax, built-ins, and libraries
- A playground for learning, experimenting, and thinking outside the box

---

## 📂 Repository Structure

Each one-liner is typically found in its own file, or grouped in scripts with explanations as comments (where necessary).

---

## 🧑‍💻 Example

**Converting Numbers to Roman Numerals**

<details>
<summary>Traditional (multi-line) approach</summary>
    
```python
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Example use:
print(int_to_roman(1999))  # Output: MCMXCIX
```

</details>

---

<details>
<summary>One-liner approach from this repo</summary>
    
```python
(lambda r,c:[print(f'{num} -->',(lambda nums:''.join([(lambda s,f:[f:=f.replace(b,r) for b,r in{'0':s[0],'1':s[1],'2':s[2]}.items()][2])('IVXLCDMnn'[(len(nums)-1-i)*2:],['','0','00','000','01','1','10','100','1000','02'][nums[i]]) for i in range(len(nums))]))([int(d) for d in f'{num}']))for num in sorted([c([r(1,200),r(1,3999)]) for _ in range(50)])])(__import__('random').randint, __import__('random').choice)
```

</details>

---

## 🤔 Why One-Liners?

- To challenge myself to write the shortest possible code for a task
- To better understand Python's expressive power
- For fun and learning!

---

## 💡 Inspiration

These scripts were inspired by coding challenges, sololearn community, curiosity, and a desire to explore the limits of Python.

---
