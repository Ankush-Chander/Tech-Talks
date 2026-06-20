# Graph Representation Tradeoffs: When Format Begets Algorithm

## The Idea

The way you represent a graph doesn't just affect constant factors — it can **suggest entirely different algorithms** for the same problem. A representation that makes one approach natural may make another nearly impossible without reformulation.

This document examines one such case and critiques it honestly.

---

## The Example: Connectivity via Matrix Multiplication

### Problem
Given a directed graph, determine whether there exists a path from vertex `i` to vertex `j` for all pairs `(i, j)`. This is the **all-pairs reachability** (transitive closure) problem.

---

### Adjacency Matrix Representation

Let `A` be the adjacency matrix where:

```
A[i][j] = 1  if edge i → j exists
A[i][j] = 0  otherwise
```

#### Key Mathematical Insight

Under **Boolean arithmetic** (where `1 + 1 = 1` and normal multiplication applies):

- `(A²)[i][j] > 0` ⟺ there exists a path of length **2** from `i` to `j`
- `(Aᵏ)[i][j] > 0` ⟺ there exists a path of length **k** from `i` to `j`
- Since longest simple path ≤ V − 1:

```
Reachability matrix = (I + A)^(V-1)   [computed under Boolean arithmetic]
```

In C++ with `std::bitset`, this becomes clean and fast:

```cpp
#include <bits/stdc++.h>
using namespace std;

using Matrix = vector<bitset<100>>; // assume V < 100

Matrix multiply(const Matrix& A, const Matrix& B, int V) {
    Matrix C(V);
    for (int i = 0; i < V; ++i)
        for (int k = 0; k < V; ++k)
            if (A[i][k])
                C[i] |= B[k]; // Boolean OR of entire row
    return C;
}

Matrix transitiveClosure(Matrix A, int V) {
    Matrix R(V);
    for (int i = 0; i < V; ++i) R[i].set(i); // identity

    Matrix P = A;
    P += R; // I + A

    // Binary exponentiation: (I + A)^(V-1) under Boolean mult
    int exp = V - 1;
    while (exp > 0) {
        if (exp & 1) R = multiply(R, P, V);
        P = multiply(P, P, V);
        exp >>= 1;
    }
    return R;
}
```

#### What Happened?
The problem of "does a path exist?" collapsed into **matrix multiplication and exponentiation**. No BFS, no DFS, no recursion — just algebra. The representation **encoded the graph as a linear-algebra object**, so we inherited everything linear algebra offers: decomposition, composition, fast algorithms, parallelism-friendly operations.

---

### Adjacency List Representation

Now consider the same problem with an adjacency list. You **cannot** multiply adjacency lists. Instead, you must reason logically:

```cpp
// BFS/DFS from every vertex — O(V(V + E))
vector<vector<bool>> reachFromAL(int V, const vector<vector<int>>& adj) {
    vector<vector<bool>> reachable(V, vector<bool>(V, false));

    for (int src = 0; src < V; ++src) {
        queue<int> q;
        vector<bool> visited(V, false);
        q.push(src);
        visited[src] = true;
        reachable[src][src] = true;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    reachable[src][v] = true;
                    q.push(v);
                }
            }
        }
    }
    return reachable;
}
```

Here, the algorithm requires you to **invent traversal logic** — queue management, visited arrays, nested loops. The adjacency list represents sparsity and topology faithfully but offers no algebraic structure to exploit.

---

## Critique of This Example

### Where It Works (Strengths)

| Aspect | Verdict |
|---|---|
| Demonstrates representation-driven algorithm shift | ✅ Strong — matrix mult is a fundamentally different algorithm than BFS |
| Mathematically elegant | ✅ Path existence ⟺ matrix entry > 0 is clean and provable |
| Bitset optimization is practical | ✅ `bitset<100>` makes the O(1) inner OR operation viable even without fast matrix multiplication |

### Where It Falls Short (Weaknesses)

#### 1. Asymptotic performance isn't the point — and it loses anyway

| Representation | Naive time with its idiomatic algorithm | With optimization |
|---|---|---|
| Adjacency matrix + matrix mult | O(V³) per multiplication, O(V·log V) multiplications → **O(V⁴ log V)** total | Binary exponentiation helps; using Strassen or Coppersmith–Winograd, each multiply is Õ(V^2.373), total Õ(V^3.373 log V). Warshall's algorithm on the matrix representation is O(V³) and simpler but doesn't use multiplication per se |
| Adjacency list + BFS from each node | **O(V(V + E))** = O(V² + VE) | For sparse graphs (E ≈ V), this is **O(V²)**. Matrix mult blows it out of the water |

The example's strength isn't speed — adjacency lists win asymptotically for sparse graphs. The strength is that it **eliminates algorithm design**: you don't invent BFS; you raise a matrix to a power.

#### 2. Warshall's algorithm muddies the waters

Floyd-Warshall (or just Warshall for reachability) operates on an adjacency matrix and runs in O(V³):

```cpp
vector<vector<bool>> warshall(int V, vector<vector<int>> R) {
    for (int k = 0; k < V; ++k)
        for (int i = 0; i < V; ++i)
            for (int j = 0; j < V; ++j)
                R[i][j] = R[i][j] || (R[i][k] && R[k][j]);
    return R;
}
```

This is arguably the "correct" matrix-based reachability algorithm — simple, O(V³), no exponentiation needed. The matrix multiplication framing adds mathematical elegance but isn't the most practical choice. Consider both and note that **Warshall's is what you'd actually write in competition.**

#### 3. Dense-graph bias

Adjacency matrices consume O(V²) space regardless of edges. For V = 10⁵, E = 10⁵, the matrix wastes ~64 GB while an adjacency list uses a few MB. The example only makes sense for **small or dense** graphs — a limitation worth calling out explicitly.

#### 4. What problem is this actually solving?

All-pairs reachability via matrix multiplication is intellectually satisfying but rarely needed. Single-source shortest path (BFS/Dijkstra), connectivity check (DFS/DSU), and topological sort are what people actually solve. The example shines in a pedagogical setting but has narrow practical relevance.

---

## Verdict

### Keep the Example, But Frame It Correctly

This example works well as a demonstration that **representation changes the problem-solving paradigm**, not as a performance recommendation. The takeaway:

> An adjacency matrix lets you treat graph problems as linear-algebra problems. You trade generality and asymptotic efficiency for elegance, composability, and access to a rich toolkit (decomposition, parallelization, hardware acceleration). The algorithm "writes itself" once you commit to the right representation.

### When to Teach This

- **Pedagogical**: Shows that "choosing data structures is choosing algorithms" — a deep CS insight
- **Practical**: Limited to small or dense graphs, or when bitset tricks make matrix ops feasible (V ≤ ~10⁴ with 64-way packing)
- **Interviews**: Recognizing the reachability ⟺ matrix entry equivalence is impressive, but follow-through on complexity matters

---

## Broader Pattern: Representation Dictates Algorithm

| Graph Problem | Adjacency List enables... | Adjacency Matrix enables... |
|---|---|---|
| Reachability | BFS/DFS traversal | Matrix exponentiation or Warshall's |
| Shortest path (unweighted) | Single-source BFS in O(V + E) | Warshall-Floyd over all pairs |
| Connected components | Union-Find on edges, DFS per component | Spectral clustering via eigendecomposition of Laplacian |
| PageRank / centrality | Iterative neighbor walks | Eigenvector of adjacency matrix power method (same idea, but matrix view suggests SVD, Rayleigh quotient) |

The pattern: **adjacency lists** invite graph-traversal thinking; **adjacency matrices** invite linear-algebra thinking. Neither is universally better — they open different doors to the same rooms.

---

## Worked Example: Adjacency List Wins — Single-Source Shortest Path

### Problem
Find the shortest distance (by number of edges) from vertex `s` to every other vertex in an unweighted graph.

Both representations can solve this via BFS. But the work each BFS step does is **drastically different**.

---

### Adjacency List — O(V + E)

```cpp
vector<int> bfsShortestPath(int s, int V, const vector<vector<int>>& adj) {
    vector<int> dist(V, -1);
    queue<int> q;

    dist[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : adj[u]) {            // iterate only over existing edges
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}
```

Each vertex is enqueued once. Across the entire run, **every edge in `adj` is looked at exactly once**. Total work: touch every vertex + scan every adjacency list = **O(V + E)**.

---

### Adjacency Matrix — O(V²) Always

```cpp
vector<int> bfsShortestPath(int s, int V, const vector<vector<int>>& adjMat) {
    vector<int> dist(V, -1);
    queue<int> q;

    dist[s] = 0;
    q.push(s);

    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v = 0; v < V; ++v) {         // scan entire row, no matter what
            if (adjMat[u][v] && dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return dist;
}
```

To find neighbors of `u`, you **must scan the entire V-length row**, even if `u` has degree 1 or 2. Every dequeued vertex costs O(V). Over V vertices: **O(V²)**, regardless of how many edges actually exist.

---

### Concrete Numbers

| Graph | E (edges) | Adjacency list BFS | Adjacency matrix BFS | Ratio |
|---|---|---|---|---|
| Sparse, V = 10⁵, E = 5·10⁵ | 500K | O(6·10⁵) ≈ **~6·10⁵ ops** | O(10¹⁰) ≈ **10¹⁰ ops** | **~17,000× slower** |
| Sparse, V = 10³, E = 2·10³ | 2K | O(3·10³) | O(10⁶) | ~300× slower |
| Dense, V = 500, E ≈ 2.5·10⁵ | 250K | O(2.5·10⁵ + 500) | O(2.5·10⁵) | **same** (E ≈ V²/2, so no gap) |

The adjacency matrix is O(V²) **always**. The adjacency list pays only for edges that exist. On sparse graphs — which are the vast majority of real-world graphs (social networks, road maps, dependency DAGs) — the gap is enormous.

---

### Why This Is a Better Example Than Matrix Multiplication

| Aspect | Single-source BFS (this example) | All-pairs reachability via matrix mult |
|---|---|---|
| **Both representations solve it directly** | ✅ Same BFS algorithm, just different neighbor lookup | ❌ Matrix enables algebra; list forces per-source BFS — different algorithms entirely |
| **One representation is asymptotically better** | ✅ List: O(V+E) beats matrix's hard O(V²) | ⚠️ Depends on graph density — list wins sparse, tie/lose dense |
| **Gap is clean and provable** | ✅ Every BFS step in the matrix version wastes work scanning zeros — waste proportional to V − deg(u) per dequeue | ⚠️ Warshall's O(V³) vs BFS-from-each-node O(V·E) depends on E/V ratio; no single winner |
| **Practical relevance** | ✅ Single-source shortest path is one of the most common graph problems | ⚠️ All-pairs reachability needed less often |

This example demonstrates that **even when the algorithm stays the same**, the representation injects hidden per-step costs. The adjacency matrix doesn't change what BFS *does* — it changes how much BFS *pays* to discover each neighbor.

---

## Summary: Two Complementary Lessons

| Lesson | Demonstrated by... | Takeaway |
|---|---|---|
| Representation changes **which algorithm** you write | Matrix multiplication for reachability | Right format → elegant, self-writing solution |
| Representation changes **how fast** the same algorithm runs | BFS on adjacency list vs matrix | Right format → fewer wasted operations per step |

Together: choose a representation that both **suggests** a good algorithm and **executes** it without hidden overhead.
