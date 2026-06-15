# Formulation

Nodes = 26 letters, edges = physical adjacency on QWERTY (unweighted).  
Precompute all-pairs shortest paths with BFS from each letter.  
Answer = sum of distances between consecutive letters in the word (starting from 'a').  
