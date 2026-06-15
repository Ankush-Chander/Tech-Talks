# Weighted Edge List

For **weighted graphs**, each entry stores the source, destination, and weight.
<table>
<tr>
<td> Graph </td> <td> Code </td>
</tr>
<tr>
<td> <img src="../../../../images/representation/weighted_graph_example.png">       </td>
<td>
```cpp
vector<tuple<int,int,int>> edges;
// Each pair `(a, b)` denotes an edge from node `a` to node `b`.
edges.push_back({1, 2, 5});
edges.push_back({2, 3, 7});
edges.push_back({2, 4, 6});
edges.push_back({3, 4, 5});
edges.push_back({4, 1, 2});

```
</td>
</tr>
</table>
