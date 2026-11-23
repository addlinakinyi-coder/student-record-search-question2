# Question 2: Student Registration Number Search

## a) Linear Search Implementation
Implemented in [`question2_linear_search.py`](./question2_linear_search.py) to search through student records sequentially for a target registration number.

## b) Efficiency as the Number of Student Records Increases
As the number of student records (n) increases, the **worst-case and average time complexity grows linearly**, written as **O(n)**:
- **Worst-case (O(n)):** If the registration number is near the end, at the last position, or not present at all, the algorithm checks up to all n records. Doubling the number of records roughly doubles the maximum number of comparisons.
- **Best-case (O(1)):** If the target registration number is found at the very first record, it takes only 1 comparison regardless of list size.
- **Space complexity (O(1)):** Uses constant extra memory as it checks records in place.

## c) Linear Search vs. Binary Search

### Conditions for Applying Each Algorithm
- **Linear Search:** Can be applied to **any** list or array—whether **sorted or unsorted**—and works on sequential structures without needing index access.
- **Binary Search:** Can only be applied when the list or array is **sorted** (in ascending or descending order) and supports direct middle-element access (such as an indexed array or list).

### Comparison Summary
| Feature | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **How it works** | Scans one by one from start to end | Repeatedly halves a sorted search range |
| **Order required** | Sorted or unsorted | Must be sorted |
| **Best time** | O(1) | O(1) |
| **Average time** | O(n) | O(log n) |
| **Worst time** | O(n) | O(log n) |
| **Best use case** | Small, unsorted lists or one-off searches | Large, sorted lists with frequent searches |
