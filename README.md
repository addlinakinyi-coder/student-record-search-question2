# Question 2: Student Registration Number Search

## a) Linear Search Implementation
Implemented in [`question2_linear_search.py`](./question2_linear_search.py) to search through student records sequentially for a target registration number.

## b) Efficiency as the Number of Student Records Increases
As the number of student records ($n$) increases, the **worst-case and average time complexity grows linearly**, written as $O(n)$:
- **Worst-case ($O(n)$):** If the registration number is near the end, at the last position, or not present at all, the algorithm checks up to all $n$ records. Doubling the number of records roughly doubles the maximum number of comparisons.
- **Best-case ($O(1)$):** If the target registration number is found at the very first record, it takes only 1 comparison regardless of list size.
- **Space complexity ($O(1)$):** Uses constant extra memory as it checks records in place.

## c) Linear Search vs. Binary Search

| Feature | Linear Search | Binary Search |
| :--- | :--- | :--- |
| **How it works** | Checks elements one by one from start to end. | Repeatedly divides a sorted search range in half by checking the middle element. |
| **Condition to apply** | Works on **any** list or array (**sorted or unsorted**). | Requires the list or array to be **sorted** (e.g., ascending/descending order). |
| **Access / structure** | Works on arrays, lists, or sequential structures. | Best on indexed arrays/lists with direct middle access. |
| **Time complexity** | Best: $O(1)$, Average: $O(n)$, Worst: $O(n)$ | Best: $O(1)$, Average: $O(\log n)$, Worst: $O(\log n)$ |
| **When to apply** | Best for **small lists**, **unsorted records**, or **one-off searches** without sorting first. | Best for **large, pre-sorted datasets** with frequent searches. |
