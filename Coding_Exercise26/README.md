# 🧮 Max and Min Finder – User Input Program

## 📋 Description

This Python program allows the user to enter numbers one at a time. It continues reading input until the user types `"done"`. After that, it prints the **maximum** and **minimum** values from the entered numbers. It also handles invalid input gracefully using a `try-except` block.

---

## 📝 Instructions

Write a Python program that:

1. Repeatedly prompts the user to enter a number.
2. Stops when the user enters `"done"`.
3. Ignores non-numeric input using a `try-except` block.
4. At the end, displays:
   - The **maximum** number entered.
   - The **minimum** number entered.

You can implement this using **any of the three approaches** below.

---

## 💡 Techniques You Can Use

- `while True` loop  
- `input()` for user interaction  
- `try-except` to catch invalid input  
- `float()` to convert strings to numbers  
- `max()`, `min()` functions (optional)  
- List storage (optional for flexibility)

---

## 🔍 Version Comparison

| Version | Description                             |
|---------|-----------------------------------------|
| **1**   | Uses `None` for initial min/max checks  |
| **2**   | Uses `float('-inf')` and built-in `max/min` |
| **3**   | Uses a list to store inputs             |

---

## ▶️ Example Output
