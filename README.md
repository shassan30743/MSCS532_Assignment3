his project contains implementations of Randomized Quicksort, Deterministic Quicksort, and a Hash Table, along with an analysis of their performance.

How to Run the Code
**Randomized quicksort.py**
Ensure you have Python installed on your system.
Open a terminal or command prompt.
Navigate to the directory containing Randomized quicksort.py
Run the script using the command:
python Randomized quicksort.py
The script will output the sorted array and the execution times for both Randomized and Deterministic Quicksort.

**Hash with chaining.py**
Navigate to the directory containing Hash with chaining.py
Run the script using the command:
python Hash with chaining.py
The script will demonstrate the basic operations of the Hash Table implementation.

**Summary of Findings**
Randomized quicksort
Time Complexity

Both Randomized and Deterministic Quicksort have an average-case time complexity of O(n log n).
Randomized Quicksort helps prevent worst-case scenarios (O(n^2)) that can occur in Deterministic Quicksort.

Performance Comparison
For an array of 1000 elements, both algorithms performed similarly, with Deterministic Quicksort being slightly faster.
The overhead of random number generation in Randomized Quicksort may account for the small time difference in small datasets.

Input Distribution Effects
Randomized Quicksort is more robust against already sorted, reverse sorted, or arrays with many duplicates.
Deterministic Quicksort can degrade to O(n^2) for sorted or reverse sorted arrays.

**Hash with chaining**
Time Complexity
Expected time complexity for insert, search, and delete operations is O(1) under simple uniform hashing.
Worst-case time complexity can degrade to O(n) if many elements hash to the same index.

Load Factor
The load factor (α = n/m) significantly influences the hash table's performance.
A lower load factor results in faster operations due to shorter chains.

Strategies for Efficiency
Dynamic resizing: Increase table size when the load factor exceeds a threshold.
Universal hashing: Use a family of hash functions to distribute keys evenly.
Prime number table size: Reduces clustering of hash values.
