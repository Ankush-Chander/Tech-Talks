# Graph Representations

*Source: Competitive Programmer's Handbook, Chapter 12*

## The Three Main Ways to Store a Graph

Any graph can be represented in memory using one of three common approaches:

* **Adjacency List** — best for iterating over edges from a node
* **Adjacency Matrix** — best for checking if an edge exists
* **Edge List** — best when the algorithm processes all edges at once

Choosing the right representation depends on what operations your algorithm needs to perform.
