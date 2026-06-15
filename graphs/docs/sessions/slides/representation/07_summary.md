## Comparison Summary

| Representation    | Edge Check | Iterate Edges from node | Memory     | Best For                     |
|-------------------|-----------|------------------------|------------|------------------------------|
| Adjacency List    | O(degree) | O(degree)              | O(n + m)   | Most graph algorithms        |
| Adjacency Matrix  | **O(1)**  | O(n)                   | O(n²)      | Dense graphs, edge queries   |
| Edge List         | O(m)       | N/A                    | O(m)       | Processing all edges once    |

---

## Key Takeaways

* **Adjacency list** is the most versatile — efficient for traversal and lightweight on memory
* **Adjacency matrix** gives fast edge lookup but wastes space on sparse graphs
* **Edge list** is minimal — useful when your algorithm visits every edge exactly once
