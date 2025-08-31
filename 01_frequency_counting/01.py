"""
Frequency Counting Patterns in Python
-------------------------------------
This file contains multiple variations of solving frequency counting problems.
Covers from scratch → dictionary → defaultdict → Counter → manual handling.
"""

# Variation 1: Using dict + .get()
def freq_with_get(data):
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    return freq


# Variation 2: Using dict + if-else (manual handling, no .get)
def freq_with_if_else(data):
    freq = {}
    for item in data:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# Variation 3: Using collections.defaultdict(int)
from collections import defaultdict

def freq_with_defaultdict(data):
    freq = defaultdict(int)  # every missing key defaults to 0
    for item in data:
        freq[item] += 1
    return dict(freq)  # convert back to normal dict if needed


# Variation 4: Using collections.Counter (one-liner)
from collections import Counter

def freq_with_counter(data):
    return dict(Counter(data))


# Variation 5: Using setdefault() (less common, but interviewers love asking)
def freq_with_setdefault(data):
    freq = {}
    for item in data:
        freq[item] = freq.setdefault(item, 0) + 1
    return freq


# Variation 6: Dictionary comprehension + Counter (compact version)
def freq_with_comprehension(data):
    return {item: data.count(item) for item in set(data)}
    # ⚠️ O(n^2) → inefficient for large data, but valid in small cases


# 🔄 Example Run
if __name__ == "__main__":
    data = "aabac"
    print("Using get():", freq_with_get(data))
    print("Using if-else:", freq_with_if_else(data))
    print("Using defaultdict:", freq_with_defaultdict(data))
    print("Using Counter:", freq_with_counter(data))
    print("Using setdefault:", freq_with_setdefault(data))
    print("Using comprehension:", freq_with_comprehension(data))
