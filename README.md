This README.md is designed to turn the 50 questions provided into a professional-grade practice project. It follows standard documentation practices you'll see in real-world Python development.
## Python Data Structures & Manipulation Practice

A collection of 50 practical challenges focused on mastering core Python data structures: Lists, Dictionaries, Sets, and Tuples. This project is designed to prepare you for technical exams by emphasizing Pythonic logic and unit testing.

## 🚀 Getting Started
1. Prerequisites
   
    Ensure you have *Python 3.10+* and *pytest* installed:
    **Terminal / Bash:**
    ```bash
    pip install pytest
    ```

2. Project Structure
    ```text
    python_exam_prep/
    ├── README.md             # Challenge descriptions and instructions
    ├── solution.py           # Create this file to write your code
    └── tests/
        └── test_ds_practical.py  # The provided test suite
    ```

## 📝 Challenge List
### 🧠 Level 1: Sequences & Sets
1. Unique Filter: Return a sorted list of unique elements.
2. List Rotation: Rotate a list left by n positions.
3. Frequency Map: Count character occurrences in a string.
4. Intersection: Find common elements using list comprehension.
5. Flattening: Convert a list of lists into a flat 1D list.
6. Chunking: Split a list into chunks of size n.
7. Parity Sort: Sort list: even numbers first, then odd.

### 🧠 Level 2: Dictionaries & Mapping
8. Key Inversion: Swap dictionary keys and values.
9. Merge & Sum: Combine two dicts, summing values for duplicate keys.
10. Top N: Get keys of the top 3 highest values.
11. Filter Dict: Remove keys where value is <50.
12. Safe Get: Safely retrieve deeply nested values (e.g., a['b']['c']).

### 🧠 Level 3: Advanced Data Processing
13. Grouping: Group words by their starting letter.
14. Multi-level Sort: Sort objects by multiple criteria (e.g., Score then Name).
15. Price Calculator: Apply conditional tax to specific categories in a list of dicts.
16. Transpose: Convert matrix rows to columns.
17. Record Update: Bulk update nested student record statuses.
18. List Difference: Find items in List A not present in List B.
19. Anagram Checker: Use frequency maps to compare two strings.
20. Data Cleaning: Deep clean None values from nested structures.

## 🧠 Level 4: Real-World Python Challenges (Advanced)

21. Stable Unique Preserve Order  
   Return unique values while preserving original order.

22. Windowed Average  
   Given a list of numbers and window size `k`, return a list of moving averages.

23. Deep Merge Dictionaries  
   Recursively merge two dictionaries. If keys conflict and values are dicts, merge them.

24. Normalized Frequency Map  
   Count characters ignoring case and spaces.

25. Cartesian Product  
   Given two lists, return all possible pairs as tuples.

26. Deep Key Search  
   Search for a key in nested dictionaries and return its value if found.

27. Nested Flatten  
   Flatten arbitrarily nested lists (e.g., [1, [2, [3, 4]]]).

28. Stable Multi-Sort  
   Sort records by multiple fields but preserve relative order where equal.

29. Schema Validator  
   Validate if a dict matches a required schema (keys + types).

30. Deduplicate Records  Given list of dicts, remove duplicates by key(e.g., "id").


## 🧠 Level 5: Expert-Level Python (Real-World Constraints)

31. Streaming Deduplicator  
    Deduplicate a large iterable using a generator (yield unique items without loading all into memory).

32. Deep Diff  
    Compare two nested dicts and return only the keys that changed.

33. Path-Based Getter  
    Retrieve a deeply nested value using dot-notation path (e.g. "a.b.c").

34. Group By Multiple Keys  
    Group list of dicts by multiple fields (e.g. cat + status).

35. Sliding Window Max  
    Return max values for each window of size k (efficient approach).

36. Circular List Iterator  
    Implement a generator that loops infinitely over a list.

37. Deep Freeze  
    Convert nested dicts/lists into immutable equivalents (frozenset, tuple).

38. Record Reconciliation  
    Merge two record lists by ID, preferring latest timestamp.

39. Data Masking  
    Mask sensitive fields (email, id, phone) in nested structures.

40. Fault-Tolerant Pipeline  
    Apply multiple functions to a list and skip failures gracefully.

## 🧠 Level 6: Senior/Staff Python (Production-Grade Thinking)

41. LRU Cache (Pure Python)  
    Implement a fixed-size LRU cache with O(1) get/set.

42. Top-K Frequent (Streaming)  
    Return top-k frequent items from a stream without storing the entire dataset.

43. JSON Patch (Mini RFC6902)  
    Apply patch operations (add, replace, remove) to nested dicts via paths.

44. Deterministic Hashing  
    Hash nested structures deterministically (order-independent for dicts).

45. Dependency Resolver  
    Given a DAG of dependencies, return a valid execution order (topological sort).

46. Rate Limiter (Token Bucket)  
    Simulate a token-bucket rate limiter.

47. Circuit Breaker (State Machine)  
    Implement CLOSED → OPEN → HALF-OPEN transitions.

48. Event Debouncer  
    Given timestamps, drop events that occur within N ms of the previous accepted event.

49. Schema Evolution  
    Migrate records between schema versions (v1 → v2 with defaults/renames).

50. Memory-Efficient Join  
    Join two large datasets by key using generators (no full materialization).



## 🧪 How to Test Your Solutions
1. Open solution.py.
2. Implement a function (e.g., unique_sorted).
3. Run the following command in your terminal:

    ```bash
    # Run all tests
    pytest tests/test_ds_practical.py

    # Run a specific test
    pytest tests/test_ds_practical.py -k "test_unique_sorted"
    ```
