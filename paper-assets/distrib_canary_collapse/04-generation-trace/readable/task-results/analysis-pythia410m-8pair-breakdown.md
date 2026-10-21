# analysis pythia410m 8pair breakdown

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia410m_8pair_breakdown_20260517T123818_result.json`
- **Structured JSON:** [`918b280d8ffadee5cd7a.json`](../../sessions/91/918b280d8ffadee5cd7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总完成。Mauve pairs 未纳入 5-method 分析（分析只覆盖了 16 pairs: 4 canary × 4 downstream，downstream 不含 mauve）。

```
Pythia-410M WikiText α=1.0 — 6 Available Canonical Pairs (entropy/ECE × d1/d2/d3)
(mauve pairs 未包含在 5-method 分析中)

Method              | Sig Count | Pairs
--------------------|-----------|------
Naive XCorr         | 6/6       | entropy→d1/d2/d3, ece→d1/d2/d3
Diff XCorr (FDR)    | 6/6       | entropy→d1/d2/d3, ece→d1/d2/d3
Threshold Onset     | 6/6       | entropy→d1/d2/d3, ece→d1/d2/d3
PermG fwd (FDR)     | 6/6       | entropy→d1/d2/d3, ece→d1/d2/d3
PermG rev (FDR)     | 0/6       | (none)  [from reverse_permg_results.json]
TY Granger          | 6/6       | entropy→d1/d2/d3, ece→d1/d2/d3

Consensus ≥3/5      | 6/6
Consensus ≥4/5      | 6/6
Consensus  5/5      | 6/6  (all pairs unanimous)
```

**Per-pair detail:**

| Pair | Naive | Diff XCorr | Threshold (lead) | TY (Wald F) | PermG fwd (F) |
|---|---|---|---|---|---|
| entropy→d1 | p≈0 | p≈0 | lead=2 | F=719.4 | F=2342.8 |
| entropy→d2 | p=2e-6 | p=1.1e-5 | lead=2 | F=221.8 | F=1363.7 |
| entropy→d3 | p=2.8e-5 | p=4.2e-5 | lead=3 | F=132.8 | F=852.9 |
| ece→d1 | p≈0 | p=2.5e-5 | lead=1 | F=1861.5 | F=5798.1 |
| ece→d2 | p≈0 | p=1e-6 | lead=1 | F=478.1 | F=1186.7 |
| ece→d3 | p≈0 | p≈0 | lead=2 | F=144.2 | F=749.2 |

**Mauve 状态:** `all_metrics.json` 中每代都有 mauve 值（从 0.034 → 0.031，漂移仅 ~10%），但 5-method 分析脚本未将 mauve 作为 downstream metric 纳入。若需要 mauve pairs 的 sig counts，需在分析脚本中补跑 `token_entropy->mauve` 和 `ece->mauve`。

---
