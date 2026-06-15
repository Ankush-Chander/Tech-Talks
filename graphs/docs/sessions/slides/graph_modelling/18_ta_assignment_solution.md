# Formulation

Flow network:  

- Source → each TA node with capacity L  
- Each TA → each course node with capacity 1 (a TA can teach a course at most once)  
- Each course → sink with lower bound K (or, split each course into in/out with demand K and use max-flow with lower bounds)  

The assignment exists iff the maximum feasible flow meets total demand (N × K).  
