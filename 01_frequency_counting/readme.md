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
```
# Pattern 1: Frequency Counting

---

## 1. `freq = {}`  
- **What is this?** → Initializing an empty dictionary in Python.  
- **Dictionary** → A key → value mapping.  
- **Keys** = unique identifiers (characters, numbers, words, etc.)  
- **Values** = data associated (here, counts).  
- **Why dictionary?** → Because lookups (`freq[item]`) are O(1) average case due to hash tables.  

---

## 2. `for item in data:`  
- **for loop** → Iterates through every element in the given sequence.  
- **data** → Can be a string, list, or any iterable.  
- **String** → iteration gives characters (`"abc"` → `'a'`, `'b'`, `'c'`)  
- **List** → iteration gives elements (`[1,2,3]` → `1`, `2`, `3`)  
- **item** → A placeholder variable. Holds one element at a time.  

---

## 3. `freq[item] = ...`  
- **LHS meaning** → “Make item a key inside freq dictionary.”  
- If item already exists → update its value.  
- If not → insert new key with given value.  
- This is **assignment** (not addition, not appending).  
- It always overwrites whatever value is there.  

---

## 4. `freq.get(item, 0)`  
- `.get(key, default)` → Safe way to fetch a value from dictionary.  
- If key exists → returns its value.  
- If not → returns the default.  
- Here → if item was never seen → treat its count as `0`.  
- **Why not just `freq[item]`?** → Because if the key doesn’t exist, Python will throw a `KeyError`.  

---

## 5. `+ 1`  
- Every time we see the item, we add `1` to its count.  
- First time → `0 + 1 = 1` (creates the key with value `1`).  
- Second time → `1 + 1 = 2` (updates the count).  
- So, this line is both **initializing and incrementing** counts.  

---

## 🔄 Example Run (Dry Run)

**Input:** `data = "aabac"`  
- Start: `freq = {}`  

1. item = `'a'` → `freq.get('a',0)` → 0 → `freq['a'] = 0+1 = 1` → `{'a':1}`  
2. item = `'a'` → `freq.get('a',0)` → 1 → `freq['a'] = 1+1 = 2` → `{'a':2}`  
3. item = `'b'` → `freq.get('b',0)` → 0 → `freq['b'] = 0+1 = 1` → `{'a':2,'b':1}`  
4. item = `'a'` → `freq.get('a',0)` → 2 → `freq['a'] = 2+1 = 3` → `{'a':3,'b':1}`  
5. item = `'c'` → `freq.get('c',0)` → 0 → `freq['c'] = 0+1 = 1` → `{'a':3,'b':1,'c':1}`  

✅ **Final Output:** `{'a': 3, 'b': 1, 'c': 1}`  

---

## 🧩 Key Vocabulary Recap
- **Dictionary (`{}`)** → Stores counts with O(1) average lookup.  
- **Key** → The unique element (letter/word/number).  
- **Value** → The count of that key.  
- **`.get(key, default)`** → Retrieves safely, avoids `KeyError`.  
- **Assignment (`=`)** → Overwrites or creates a new entry in dictionary.  
- **Increment (`+1`)** → Updates the frequency each time element is seen.  

---

## 🎯 Why This Matters
This is the **foundation pattern** for many higher-level problems:  
- **Anagrams** → Compare two frequency dicts.  
- **Sliding Window** → Add/remove frequencies as window moves.  
- **Top K Elements** → Sort by frequency.  
- **Duplicate detection** → Check if count > 1.  
