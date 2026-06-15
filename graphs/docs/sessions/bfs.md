# Breadth-First Search (BFS) in C++

## 1. What Is BFS?

BFS explores a graph **level by level**, visiting all neighbors of a node before moving to the next level. It uses a **queue** (FIFO) to ensure nodes are processed in order of their distance from the source.

---

## 2. Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

void bfs(int x, const vector<vector<int>>& adj) {
    int n = adj.size();
    vector<bool> visited(n, false);
    vector<int> distance(n, 0);
    queue<int> q;

    visited[x] = true;
    distance[x] = 0;
    q.push(x);

    while (!q.empty()) {
        int s = q.front();
        q.pop();

        // process node s
        cout << s << " ";

        for (auto u : adj[s]) {
            if (visited[u]) continue;
            visited[u] = true;
            distance[u] = distance[s] + 1;
            q.push(u);
        }
    }
}
```

### Key Details

- A node is marked `visited` **at push time** (when enqueued), not at pop time. This prevents duplicates in the queue.
- The `distance[]` array tracks shortest-path length from source. Since BFS visits level by level, the first time a node is reached is guaranteed to be via the minimum number of edges.
- The `if (visited[u]) continue;` pattern keeps the inner loop clean and avoids nested conditionals.

---

## 3. How It Works Step by Step

Consider this graph:

```
        0
       / \
      1   2
     / \   \
    3   4   5
```

Starting BFS from node `0`:

| Step | Queue (front → back) | Visited order so far | Action |
|---|---|---|---|
| 1 | `[0]` | — | Push start, mark visited |
| 2 | pop `0`, push `1`,`2` | `0` | Enqueue neighbors of 0 |
| 3 | `[1, 2]` | — | — |
| 4 | pop `1`, push `3`,`4` | `0 1` | Enqueue neighbors of 1 |
| 5 | `[2, 3, 4]` | — | — |
| 6 | pop `2`, push `5` | `0 1 2` | Enqueue neighbor of 2 |
| 7 | `[3, 4, 5]` | — | — |
| 8 | Drain queue | `0 1 2 3 4 5` | No new neighbors |

**Output:** `0 1 2 3 4 5` (level-order traversal)

---

## 4. BFS vs DFS at a Glance

| Aspect | BFS | DFS |
|---|---|---|
| **Data structure** | Queue (FIFO) | Stack / Recursion (LIFO) |
| **Exploration order** | Level by level (breadth first) | Deep into one branch first |
| **Shortest path** | Finds shortest path in unweighted graphs | Does not guarantee shortest path |
| **Memory usage** | Can be large (stores entire frontier) | Proportional to max depth |
| **Completeness** | Guaranteed to find a node if it exists | May get stuck in infinite branches (if no visited check) |

---

## 5. Common Applications

### Shortest Path in Unweighted Graph

BFS guarantees the first time a node is reached, it is via the shortest path (minimum number of edges).

```cpp
// Returns minimum number of edges from source to target (-1 if unreachable)
int shortestPath(int src, int target, const vector<vector<int>>& adj) {
    if (src == target) return 0;

    int n = adj.size();
    vector<bool> visited(n, false);
    vector<int> distance(n, 0);
    queue<int> q;

    visited[src] = true;
    distance[src] = 0;
    q.push(src);

    while (!q.empty()) {
        int s = q.front();
        q.pop();

        for (auto u : adj[s]) {
            if (visited[u]) continue;

            visited[u] = true;
            distance[u] = distance[s] + 1;

            if (u == target) return distance[u];

            q.push(u);
        }
    }
    return -1; // unreachable
}
```

### Level-Order Traversal of a Binary Tree

Same idea — queue holds nodes level by level.

### Connected Components

Run BFS from every unvisited node to enumerate all connected components.

### Bipartite Graph Check

Use BFS to 2-color the graph. If any edge connects two same-colored nodes, the graph is not bipartite.

```cpp
bool isBipartite(int n, const vector<vector<int>>& adj) {
    vector<int> color(n, 0); // 0 = uncolored, 1 and -1 = two colors

    for (int i = 0; i < n; ++i) {
        if (color[i] != 0) continue;

        queue<int> q;
        q.push(i);
        color[i] = 1;

        while (!q.empty()) {
            int u = q.front();
            q.pop();

            for (int v : adj[u]) {
                if (color[v] == 0) {
                    color[v] = -color[u];
                    q.push(v);
                } else if (color[v] == color[u]) {
                    return false;
                }
            }
        }
    }
    return true;
}
```

---

## 6. Complexity

| Metric | Value |
|---|---|
| **Time** | O(V + E) — each vertex and edge visited once |
| **Space** | O(V) — queue + visited array, at most V entries |

- `V` = number of vertices
- `E` = number of edges

---

## 7. Gotchas

- **Mark before enqueue**: Failing to mark `visited` at push time causes duplicate entries in the queue → TLE or incorrect results.
- **Disconnected graphs**: BFS from one source only reaches its component. Loop over all vertices to cover the full graph.
- **Weighted graphs**: BFS does **not** find shortest paths by weight. Use Dijkstra's or Bellman-Ford instead.

---

## 8. TL;DR

- BFS uses a **queue** to explore level by level.
- Same O(V + E) time as DFS, but higher peak memory on wide graphs.
- Go-to algorithm for: shortest path, level-order traversal, bipartite check, component discovery.

# References

1. [BFS visualization](https://www.cs.usfca.edu/~galles/visualization/BFS.html)
