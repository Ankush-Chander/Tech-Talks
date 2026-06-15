# Weighted Adjacency List

<table>
<tr>
<td> Graph </td> <td> Code </td>
</tr>
<tr>
<td> <img src="../../../../images/representation/weighted_graph_example.png">       </td>
<td>

```cpp
vector<pair<int,int>> adj[N];
// **adjacency list** stores, for each node, the set of (node,weight) it has edges to.
adj[1].push_back({2, 5});
adj[2].push_back({3, 7});
adj[2].push_back({4, 6});
adj[3].push_back({4, 5});
adj[4].push_back({1, 2});

```

</td>
</tr>
</table>

```cpp
for (auto [u, w] : adj[s]) {
    // u = neighbor node, w = edge weight
    // e.g. relax distance: if (dist[s] + w < dist[u]) dist[u] = dist[s] + w;
}
```
