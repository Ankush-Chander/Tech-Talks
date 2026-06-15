# Adjacency List Representation (Unweighted)

<table>
<tr>
<td> Graph </td> <td> Code </td>
</tr>
<tr>
<td> <img src="../../../../images/representation/adjacency_list_graph_example.png">       </td>
<td>

```cpp
// An **adjacency list** stores, for each node, the set of nodes it has edges to.
vector<int> adj[N];
adj[1].push_back(2);
adj[2].push_back(3);
adj[2].push_back(4);
adj[3].push_back(4);
adj[4].push_back(1);

```

</td>
</tr>
</table>

### Benefit

Finding all outgoing edges of a node is efficient:

```cpp
for (auto u : adj[s]) {
    cout << u << " ";
}
```
