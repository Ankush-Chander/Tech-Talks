# Edge List Representation

An **edge list** simply stores all edges in a collection — no structure by node.
<table>
<tr>
<td> Graph </td> <td> Code </td>
</tr>
<tr>
<td> <img src="../../../../images/representation/adjacency_list_graph_example.png">       </td>
<td>
```cpp
vector<pair<int,int>> edges;
// Each pair `(a, b)` denotes an edge from node `a` to node `b`.
edges.push_back({1, 2});
edges.push_back({2, 3});
edges.push_back({2, 4});
edges.push_back({3, 4});
edges.push_back({4, 1});
```
</td>
</tr>
</table>

Best when the algorithm iterates over **all edges** and doesn't need to find outgoing edges from a specific node.
