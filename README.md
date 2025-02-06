# Algorithms-Project (1)


# 🚀 Algorithms Projects: Triangle Triplets & K-th Element of Two Sorted Arrays

## 📌 Overview
This repository contains implementations for two fundamental algorithmic problems:

1. **Triangle Triplets** (Project 2) - Finding valid triangular triplets in an array.
2. **K-th Element of Two Sorted Arrays** (Project 7) - Efficiently locating the k-th smallest element without merging the arrays.

Each solution is optimized for performance and includes analysis of time complexity.

---

## 🔹 Project 2: Triangle Triplets
### 📖 Problem Statement
Given an array of integers, determine if there exists a triplet `(P, Q, R)` such that:
- `A[P] + A[Q] > A[R]`
- `A[Q] + A[R] > A[P]`
- `A[R] + A[P] > A[Q]`

Additionally, the solution should:
- Count all unique triangular triplets.
- Allow custom range-based searches.
- Return triplet details if requested.

### 🏆 Solution Approach
- **Sorting & Two Pointers:** Efficiently checks possible triplets.
- **Time Complexity:** `O(N log N + N^2)`.

### ✅ Example
```python
Input: nums = [10, 2, 5, 1, 8, 20]
Output: (5, [(8, 16, 20), (10, 16, 20), (5, 16, 20), (5, 8, 10), (8, 10, 16)])
```

---

## 🔹 Project 7: K-th Element of Two Sorted Arrays
### 📖 Problem Statement
Given two sorted arrays, find the k-th smallest element **without merging** them.

### 🏆 Solution Approach
- **Binary Search on the Shorter Array:** Ensures `O(log k)` efficiency.
- **Divide & Conquer:** Eliminates unnecessary elements in each step.

### ✅ Example
```python
Input: 
    Array 1 = [2, 3, 6, 7, 9]
    Array 2 = [1, 4, 8, 10]
    k = 5
Output: 6
```

---

## 📂 Repository Structure
```
📁 project_2_triangle_triplets
    ├── triangle_triplets.py
    ├── README.md
📁 project_7_kth_element
    ├── kth_element.py
    ├── README.md
```

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/algorithms-projects.git
   cd algorithms-projects
   ```
2. Run a specific project:
   ```bash
   python project_2_triangle_triplets/triangle_triplets.py
   ```
   ```bash
   python project_7_kth_element/kth_element.py
   ```

---

## 🛠 Technologies Used
- Python 3
- Sorting & Binary Search Algorithms
- Time Complexity Analysis

---

## 📌 Future Improvements
- Extend support for larger datasets.
- Optimize space complexity.
- Implement alternative approaches using different data structures.

---

## 🤝 Contributing
Feel free to fork the repository and submit pull requests. Any improvements are welcome!

---

## 📄 License
This project is open-source and available under the MIT License.
