# analysis option c degen vs headroom

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_option_c_degen_vs_headroom_20260517T085228_result.json`
- **Structured JSON:** [`b4ca20ed18fd9ce047bc.json`](../../sessions/b4/b4ca20ed18fd9ce047bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
=== Option C: Constant F1 Degen vs Oracle Headroom ===

Type            | Degen% (CF1) |  Greedy F1 |  Oracle F1 | Headroom (pp) |      n
--------------------------------------------------------------------------------
art             |       25.84% |     0.7557 |     0.8477 |         9.21pp |   1277
building        |       12.35% |     0.7024 |     0.8514 |        14.90pp |   1587
event           |       12.71% |     0.6548 |     0.8162 |        16.14pp |   1306
location        |       14.08% |     0.7924 |     0.8951 |        10.27pp |   8023
organization    |       10.89% |     0.7202 |     0.8535 |        13.33pp |   6647
other           |       11.13% |     0.6373 |     0.8312 |        19.39pp |   3433
person          |       15.28% |     0.8220 |     0.9141 |         9.21pp |   8016
product         |       14.32% |     0.6563 |     0.8140 |        15.78pp |   2276

Spearman ρ(Constant_F1_degen, oracle_headroom) = -0.619, p = 0.1017, n=8
Not significant (p >= 0.05)
```

**结论：** Spearman ρ = **-0.619**，p = 0.1017，n=8 下不显著。

方向是负相关：degeneracy 越高的 type（如 art 25.84%），oracle headroom 反而越小（9.21pp）。这与预期相反——高 degeneracy 本应意味着更多"有用的多样性"从而带来更大 oracle headroom，但实际上高 degeneracy 的 type（art）greedy 本身就较强（0.756），oracle 提升空间有限；而低 degeneracy 的 type（other 11.13%）greedy 很弱（0.637），oracle headroom 反而最大（19.39pp）。

Option C 在 n=8 的粒度下未通过显著性检验。

---
