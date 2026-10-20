# D020 Task 2: ACDC 14-Edge Selection Method Documentation

## ACDC Cache Format (`cache_acdc.json`)

**Total edges**: 32,491 (all edges in GPT-2 IOI circuit search space)

ACDC (Conmy et al., 2023) uses iterative ablation with threshold sweeps. The `auto_circuit` implementation:
1. Initializes all edge scores to `inf`
2. For each threshold `tao`, iterates edges top-down by layer
3. If removing an edge degrades faithfulness (KL divergence) by < `tao`, the edge is pruned and assigned `score = min(tao, current_score)`
4. Edges that survive ALL thresholds retain `score = inf` — these form the circuit

**Our configuration** (`circuit_discovery.py:118`): `tao_exps=[-2]` with default `tao_bases=[1,3,5,7,9]`
- Thresholds: 0.01, 0.03, 0.05, 0.07, 0.09

## Score Distribution

| Score | Count | Meaning |
|-------|-------|---------|
| inf | 14 | **Retained circuit** — survived all 5 thresholds |
| 0.09 | 14 | Pruned only at most lenient threshold |
| 0.07 | 11 | Pruned at tao=0.07 |
| 0.05 | 50 | Pruned at tao=0.05 |
| 0.03 | 138 | Pruned at tao=0.03 |
| 0.01 | 32,264 | Pruned at strictest threshold (most unimportant) |

## 14 Infinity Edges (The Retained Circuit)

```
a0.h1->a9.h9.v
a10.h0->logits
a11.h2->logits
a5.h5->a8.h6.v
a7.h9->a9.h9.q
a8.h6->a9.h6.q
a8.h6->a9.h9.q
a9.h6->logits
a9.h9->logits
input->m0
m0->a10.h0.v
m0->a5.h5.q
m0->a9.h6.v
m0->a9.h9.v
```

## 14 Score=0.09 Edges (Borderline — Last Pruned)

```
a10.h1->logits
a10.h2->logits
a10.h6->logits
a10.h7->logits
a6.h9->a8.h6.v
a7.h3->a9.h9.q
a9.h8->logits
m0->a9.h8.v
m0->a9.h9.k
m1->a9.h9.v
m2->a9.h9.v
m4->a9.h9.v
m6->a9.h9.v
m7->a9.h9.v
```

## Why `math.isinf()` Is Not Cherry-Picking

The binarization `{e for e, v in scores.items() if math.isinf(v)}` (`analysis_fix_v3.py:38`) is the **canonical way** to read ACDC output — it is dictated by the algorithm's output format, not a post-hoc cutoff choice:

- ACDC is a **binary** circuit discovery method: an edge is either in the circuit (inf) or pruned (finite)
- The finite values encode **when** an edge was pruned (which tao step), not a continuous importance score
- There is no threshold to tune — `isinf` is the only correct reading of the output
- This is identical to how `auto_circuit` itself interprets ACDC results (line 118 in ACDC source: `(s == t.inf) * 1.0`)

The 14 score=0.09 edges are a coincidence in count — they are the edges pruned at the **last** (most lenient) threshold, meaning they were the most borderline pruned edges, but still pruned.

## Code Comments Added

- `analysis_fix_v3.py:38-42` — `binarize_acdc` function: explains inf/finite semantics and why isinf is canonical
- `circuit_discovery.py:111` — `run_acdc` docstring: documents output format
