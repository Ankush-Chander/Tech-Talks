# Representation Shapes Algorithm: A Graph Story

Imagine you're building a feature that checks whether any two users in a social
network are connected. You have the data. Now you have to store it somehow — and
that choice will determine not just how fast your code runs, but what kind of
solution you even think to write.

This is the central idea: **how you represent a problem constrains how you can
solve it.** The same graph, stored two different ways, can lead to fundamentally
different algorithms — sometimes by making the fast approach obvious, sometimes
by making it nearly impossible.

We'll look at two concrete examples, starting with the more intuitive one.

---

## Part 1: Same Algorithm, Different Cost

### Problem: Shortest Path in an Unweighted Graph

Given a graph, find the shortest distance (in number of edges) from a start
vertex `s` to every other vertex. The standard approach is **BFS** — explore
neighbors level by level. Both representations below use BFS. But watch what
happens to the inner loop.

---

### Adjacency List

An adjacency list stores, for each vertex, only the vertices it's actually
connected to.

```
Vertex 0: [1, 3]
Vertex 1: [0, 2]
Vertex 2: [1]
Vertex 3: [0]
```

```cpp
vector<int> bfs(int s, int V, const vector<vector<int>>& adj) {
    vector<int> dist(V, -1);
    queue<int> q;
    dist[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v : adj[u]) {         // only visits real neighbors
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}
```

When you process vertex `u`, you iterate over only its actual neighbors — nothing
extra. Across the whole BFS, every edge gets looked at exactly once.

**Total work: O(V + E)**

---

### Adjacency Matrix

An adjacency matrix stores a V × V grid. Cell `[i][j]` is `1` if edge `i → j`
exists, `0` otherwise.

```
     0  1  2  3
  0 [0, 1, 0, 1]
  1 [1, 0, 1, 0]
  2 [0, 1, 0, 0]
  3 [1, 0, 0, 0]
```

```cpp
vector<int> bfs(int s, int V, const vector<vector<int>>& mat) {
    vector<int> dist(V, -1);
    queue<int> q;
    dist[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (int v = 0; v < V; ++v) {  // scans the entire row, always
            if (mat[u][v] && dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}
```

To find the neighbors of `u`, you must scan all V entries in its row — even if
`u` only has 2 or 3 actual neighbors. Every zero you check is wasted work.

**Total work: O(V²), regardless of how many edges exist**

---

### The Gap in Practice

The difference between O(V + E) and O(V²) is abstract. Here's what it means
with real numbers:

| Graph | Edges | Adjacency List | Adjacency Matrix | Ratio |
|---|---|---|---|---|
| Large sparse (V = 100,000, E = 500,000) | 500K | ~600,000 ops | ~10,000,000,000 ops | **~17,000× slower** |
| Small sparse (V = 1,000, E = 2,000) | 2K | ~3,000 ops | ~1,000,000 ops | ~300× slower |
| Dense (V = 500, E ≈ 125,000) | 125K | ~125,500 ops | ~250,000 ops | ~2× slower |

Real-world graphs — social networks, road maps, dependency trees — are almost
always sparse. A person has hundreds of friends, not millions. A city has roads
to adjacent blocks, not every other block. For these graphs, the adjacency
matrix is doing enormous amounts of pointless work.

> **Key insight:** The algorithm didn't change. BFS is BFS. But the
> representation injected hidden cost into every single step. The adjacency
> list pays only for edges that exist; the matrix pays for edges that *don't*
> exist too.

---

## Part 2: Different Representation, Different Algorithm Entirely

The BFS example showed how representation affects *speed*. This example shows
something deeper: how it can change *what you even think to do*.

### Problem: All-Pairs Reachability (Transitive Closure)

For every pair of vertices `(i, j)`, does a path from `i` to `j` exist?

With an adjacency list, the natural answer is: run BFS or DFS from every
vertex. That's fine, and it works — but you have to design and implement the
traversal logic yourself.

With an adjacency matrix, something unexpected becomes available.

---

### The Matrix Multiplication Insight

Let `A` be the adjacency matrix. Under Boolean arithmetic (where `1 + 1 = 1`):

- `A[i][j] = 1` means there's a direct edge from `i` to `j` (a path of length 1)
- `(A²)[i][j] = 1` means there's a path of length exactly 2 from `i` to `j`
- `(Aᵏ)[i][j] = 1` means there's a path of length exactly `k` from `i` to `j`

Since the longest useful path in a graph of V vertices has length at most V − 1,
the full reachability matrix is:

```
Reachability = (I + A)^(V-1)   [under Boolean arithmetic]
```

The graph problem has become an algebra problem. You don't design traversal
logic — you raise a matrix to a power.

```cpp
#include <bits/stdc++.h>
using namespace std;
using Matrix = vector<bitset<100>>;

Matrix multiply(const Matrix& A, const Matrix& B, int V) {
    Matrix C(V);
    for (int i = 0; i < V; ++i)
        for (int k = 0; k < V; ++k)
            if (A[i][k])
                C[i] |= B[k];  // Boolean OR of entire row — fast with bitset
    return C;
}

Matrix transitiveClosure(Matrix A, int V) {
    Matrix R(V);
    for (int i = 0; i < V; ++i) R[i].set(i);  // start with identity

    Matrix P = A;
    for (int i = 0; i < V; ++i) P[i] |= R[i]; // I + A

    int exp = V - 1;
    while (exp > 0) {
        if (exp & 1) R = multiply(R, P, V);
        P = multiply(P, P, V);
        exp >>= 1;
    }
    return R;
}
```

No queues, no visited arrays, no recursion. The representation made the graph
behave like a linear-algebra object, so an algebraic solution became natural.

---

### Warshall's Algorithm — The Practical Version

Before reaching for matrix exponentiation, it's worth knowing that there's a
simpler matrix-based approach that runs in O(V³):

```cpp
// Warshall's algorithm — simpler, O(V³), same idea
vector<vector<bool>> warshall(int V, vector<vector<int>> R) {
    for (int k = 0; k < V; ++k)
        for (int i = 0; i < V; ++i)
            for (int j = 0; j < V; ++j)
                R[i][j] = R[i][j] || (R[i][k] && R[k][j]);
    return R;
}
```

The matrix representation enabled both of these approaches. Neither is natural
with an adjacency list.

---

### A Note on When to Use This

The matrix approach makes sense when:

- Your graph is **small or dense** (V ≤ a few thousand; matrix storage is O(V²))
- You want to leverage the algebraic structure (e.g., hardware-accelerated
  matrix ops, parallel processing)

For large sparse graphs, running BFS from every vertex using an adjacency list
will be faster in practice. The value of the matrix approach isn't always speed —
it's that the problem dissolves into algebra you already know how to manipulate.

---

## The Pattern, Summarized

Both examples illustrate the same underlying principle from different angles:

| | What changed | Lesson |
|---|---|---|
| **BFS example** | Same algorithm, different representation | Representation can hide cost in every step — pay for what doesn't exist |
| **Reachability example** | Different algorithm, triggered by representation | Representation can open entirely different solution strategies |

A useful way to think about it: the adjacency list invites you to *traverse* the
graph; the adjacency matrix invites you to *compute* on it. Same graph, different
mental model, different toolkit.

---

## Practical Takeaways

When picking a graph representation, ask two questions:

**1. How dense is the graph?**
If E is much smaller than V², use an adjacency list. The matrix will waste
memory and time on empty cells. If E is close to V², the matrix overhead becomes
acceptable.

**2. What operations do you need?**
- Fast neighbor iteration → adjacency list
- Edge existence check in O(1) → adjacency matrix
- Linear-algebra operations (matrix powers, spectral methods) → adjacency matrix
- Memory-efficient storage of sparse graphs → adjacency list

> The representation you choose doesn't just store your data — it shapes which
> solutions feel natural and which feel forced. Choosing well can make a hard
> problem easy. Choosing poorly can make an easy problem hard.
