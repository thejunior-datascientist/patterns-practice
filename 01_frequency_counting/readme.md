# Pattern 01: Frequency Counting

## 📌 What is it?
Frequency Counting is a technique to **count how many times something appears** in a collection (string, list, or array).  
It uses a **dictionary (hash map)** to store items as keys and their counts as values.

---

## 🔑 Core Template
```python
freq = {}
for item in data:
    freq[item] = freq.get(item, 0) + 1
