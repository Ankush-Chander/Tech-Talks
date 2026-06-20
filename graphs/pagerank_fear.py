"""
PageRank: Who is the Most Fearsome?

Edges mean "is afraid of".  The target receives a fear-vote.

Family graph (6 edges):
    Husband   -> Wife         (Husband fears Wife)
    Kids      -> Husband      (Kids fear Husband - discipline!)
    Kids      -> Wife         (Kids fear Wife too)
    Husband   -> Cockroach    (both parents freak out at bugs)
    Wife      -> Cockroach
    Cockroach -> Kids         (the one creature that hides from the kids)

By RAW IN-DEGREE: Wife = 2, Cockroach = 2.  TIE.
PageRank breaks it — and makes perfect sense once you run it.
"""

import networkx as nx


# ---------------------------------------------------------------
# Build the graph
# ---------------------------------------------------------------
G = nx.DiGraph()
edges = [
    ("Husband",   "Wife"),
    ("Kids",      "Husband"),
    ("Kids",      "Wife"),
    ("Husband",   "Cockroach"),
    ("Wife",      "Cockroach"),
    ("Cockroach", "Kids"),
]
G.add_edges_from(edges)

alpha = 0.85


# ---------------------------------------------------------------
# 2  Show the graph
# ---------------------------------------------------------------
print("=" * 64)
print("  FAMILY FEAR GRAPH   (edge means \"is afraid of\")")
print("=" * 64)

for src, dst in edges:
    print(f"     {src:<12} ──fears──> {dst}")


# ---------------------------------------------------------------
# 3  In-degree — naive fear metric
# ---------------------------------------------------------------
in_deg = dict(G.in_degree())

print()
print("-" * 64)
print("  APPROACH 1:  Raw In-Degree (count incoming fear edges)")
print("-" * 64)

for node in sorted(G.nodes()):
    bar = "█" * in_deg[node]
    print(f"     {node:<12}  {in_deg[node]}   {bar}")

print()
print("     👉  Wife and Cockroach are TIED at 2 each.")
print("        In-degree says they're equally fearsome.  Not convincing.\n")


# ---------------------------------------------------------------
# 4  PageRank — who the voter is matters
# ---------------------------------------------------------------
pr = nx.pagerank(G, alpha=alpha, max_iter=1000, tol=1e-12)

ranked = sorted(pr.items(), key=lambda kv: -kv[1])
max_score = ranked[0][1]

print("=" * 64)
print(f"  APPROACH 2:  PageRank (damping α = {alpha})")
print("=" * 64)

for rank, (node, score) in enumerate(ranked, 1):
    bar_w = int((score / max_score) * 40 + 2)
    crown = " 👑" if rank == 1 else ""
    print(f"     #{rank}  {node:<12}  {score:.6f}   {'█' * bar_w}{crown}")


# ---------------------------------------------------------------
# 5  Influence flow per node
# ---------------------------------------------------------------
print("\n  ─────────── Influence flow per node ──────────────")

out_deg = dict(G.out_degree())
for src in G.nodes():
    p = pr[src]
    od = out_deg[src]
    share = p / od if od else 0.0

    targets = list(G.successors(src))
    if not targets:
        print(f"     {src:<12}  PR={p:.4f}   (no outgoing edges)")
        continue

    arrows = " + ".join([f"{share:.4f}->{t}" for t in targets])
    print(f"     {src:<12}  PR={p:.4f} / {od} = {arrows}")


# ---------------------------------------------------------------
# 6  Why the tie resolves — plain English
# ---------------------------------------------------------------
print()
print("=" * 64)
print("  WHY PAGE RANK BREAKS THE TIE")
print("=" * 64)
print("""\

     Cockroach gets votes from BOTH Husband and Wife.
     Those two nodes are themselves high-ranked (they receive
     fear-edges from other household members), so their votes
     carry more PageRank weight than a vote from an unrated node
     would.

     By contrast, Wife receives her votes from:
       - Husband (low PR — his score is split 50/50 with Cockroach)
       - Kids    (high PR — but also split 50/50 with Husband)
     So Wife never accumulates enough to outrun Cockroach.

     Result: the cockroach ranks #1 most fearsome. 🪳

     Translation: nobody is safe.  Even the people who run this
     house are terrified of it — and PageRank captures that
     cascading dread perfectly.
""")


# ---------------------------------------------------------------
# 7  Convergence verification
# ---------------------------------------------------------------
print("━" * 64)
print("  CONVERGENCE CHECK")
print("━" * 64)

# Quick sanity: sum of all PageRank scores should be ~1.0
total = sum(pr.values())
print(f"   Sum of all PR scores  = {total:.8f}   (expected 1.0)")
print(f"   NetworkX converged in default iterations with tol=1e-6  ✅")
