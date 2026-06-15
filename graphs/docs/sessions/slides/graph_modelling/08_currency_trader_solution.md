# Formulation

Nodes = currencies, directed weighted edges = exchange rates.  
Take negative log of each rate; detect a negative cycle using Bellman–Ford.  
Equivalently, multiply rates along cycles; a product > 1 indicates arbitrage.  
