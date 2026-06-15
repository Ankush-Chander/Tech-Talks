## Kruskal's Algorithm
Kruskal's algorithm builds the MST by processing edges in increasing order of their weights.

### The Strategy
Start with a graph containing all nodes but zero edges. Each node is its own separate component.
Sort all edges in increasing order of weight.
Iterate through the sorted edges. Add an edge to the tree only if it connects two different components (meaning it doesn't create a cycle).
Stop when all nodes belong to a single component.

### Why It Works
Kruskal relies on the greedy choice property. If a spanning tree does not contain the minimum weight edge, you could always remove an edge from its cycle and swap in the minimum weight edge to produce a valid spanning tree with a strictly smaller total weight.

### Implementation
The algorithm requires sorting edges in $O(m \log m)$ time, followed by iterating through them:
```cpp
//After sorting edges...
for (...) {
    if (!same(a, b)) unite(a, b);
}
```

<!--### Union-Find Structure (Disjoint Sets)
To make Kruskal's algorithm fast, we need a way to efficiently check if two nodes are in the same component (same) and to merge two components (unite). Graph traversal (DFS/BFS) takes $O(n+m)$ per edge, which is too slow. Instead, we use a Union-Find structure.

#### Structure
Each set has a "representative" element. Every other element in the set points to it via a chain.

#### Find
Follow the chain to find the representative.

#### Union
Connect the representative of the smaller set to the representative of the larger set to keep chains short ($O(\log n)$ length).

```C++
int link[N], size[N];

// Initially, each element is its own representative and size is 1
for (int i = 1; i <= n; i++) link[i] = i;
for (int i = 1; i <= n; i++) size[i] = 1;

int find(int x) {
    while (x != link[x]) x = link[x];
    return x;
}

bool same(int a, int b) {
    return find(a) == find(b);
}

void unite(int a, int b) {
    a = find(a);
    b = find(b);
    if (size[a] < size[b]) swap(a,b);
    size[a] += size[b];
    link[b] = a;
}
```

Using Union-Find, Kruskal's time complexity drops to `O(m log n)` after sorting.-->

## Prim's Algorithm

Prim's algorithm is an alternative greedy method for finding an MST. Instead of sorting all edges, it grows a single tree outward from a starting point.

#### Strategy

Start by adding an arbitrary node to the tree.
Look at all edges connecting the current tree to unvisited nodes.
Greedily choose the minimum-weight edge that adds a new node to the tree.
Repeat until all nodes are included.

#### Implementation

Prim's algorithm highly resembles Dijkstra's algorithm and can be implemented using a priority queue. The queue tracks all nodes that can be connected to the current component using a single edge, sorted by edge weight.

The time complexity is `O(n + m log m)`, which is identical to Dijkstra's algorithm.

#### Algorithm Comparison

Both algorithms are highly efficient in practice. The choice often comes down to the graph structure and personal preference.

### Comparison

| | Kruskal's Algorithm | Prim's Algorithm |
| ---   | --- | ---
| Approach | Forest-based (merges disjoint trees) | Tree-based (grows a single tree)
| Data Structure | Union-Find (Disjoint Sets) | Priority Queue
| Edge Processing | Globally sorted by weight | Locally evaluated from the tree boundary
| Time Complexity | `O(m log m)` or `O(m log n)` | `O(n + m log m)`
| Best For | Sparse graphs | Dense graphs

## Competitive Programming Note

While both are viable, most competitive programmers prefer Kruskal's algorithm due to its straightforward implementation and lack of complex priority queue state management.
