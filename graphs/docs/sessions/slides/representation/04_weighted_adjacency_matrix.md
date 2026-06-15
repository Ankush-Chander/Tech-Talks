# Weighted Adjacency Matrix
For **weighted graphs**, the matrix stores edge weights instead of binary values.  
<table>
<tr>
<td> Graph </td> <td> Code </td>
</tr>
<tr>
<td> <img src="../../../../images/representation/weighted_graph_example.png">       </td>
<td>
<img src="../../../../images/representation/wighted_matrix_cells.png">       

</td>
</tr>
</table>

```cpp
int adj[N][N];
// adj[a][b] = 1 if edge `a→b` exists, else `0`
/* 
 * The matrix always has **n²** elements, and most are typically zero. This leads to:
 * Wasted memory for sparse graphs
 * Slower algorithms that iterate over all possible edges
 */
```



### Drawback

The matrix always has **n²** elements, and most are typically zero. This leads to:

* Wasted memory for sparse graphs
* Slower algorithms that iterate over all possible edges

For large graphs, adjacency lists are a better choice.
