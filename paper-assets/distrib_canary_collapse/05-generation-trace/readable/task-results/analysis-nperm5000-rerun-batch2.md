# analysis nperm5000 rerun batch2

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nperm5000_rerun_batch2_20260518T111504_result.json`
- **Structured JSON:** [`58695fd90bf179d3ecc7.json`](../../sessions/58/58695fd90bf179d3ecc7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. Here's the complete Table 7 output:

---

## Condition 4: C4 Pythia-1B s42
```
旧 (n_perm=1000): Naive=8/8, Diff=8/8, Thresh=6/8, PG_fwd=8/8, PG_rev=4/8, TY=4/8, K≥4=7/8
新 (n_perm=5000): Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=3/8, TY=3/8, K≥4=6/8
```
**Flips:** Diff 8→6 (↓2), Thresh 6→8 (↑2), PG_fwd 8→6 (↓2), PG_rev 4→3 (↓1), TY 4→3 (↓1), K≥4 7→6 (↓1)

PG_rev detail:
| Pair | F | p | |
|---|---|---|---|
| distinct_1→token_entropy | 0.6505 | 0.4983 | ns |
| distinct_2→token_entropy | 1.0526 | 0.3661 | ns |
| distinct_3→token_entropy | 1.3998 | 0.2889 | ns |
| perplexity→token_entropy | 2.8201 | 0.1428 | ns |
| distinct_1→ece | 14.6733 | 0.0046 | **SIG** |
| distinct_2→ece | 20.0776 | 0.0022 | **SIG** |
| distinct_3→ece | 23.2473 | 0.0024 | **SIG** |
| perplexity→ece | 0.9195 | 0.3907 | ns |

---

## Condition 5: C4 Pythia-1B s43
```
旧: 无可靠参考（旧版用 n_perm=1000）
新 (n_perm=5000): Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=0/8, TY=3/8, K≥4=6/8
```

PG_rev detail:
| Pair | F | p | |
|---|---|---|---|
| distinct_1→token_entropy | 0.4778 | 0.5893 | ns |
| distinct_2→token_entropy | 0.1633 | 0.7357 | ns |
| distinct_3→token_entropy | 0.0274 | 0.8844 | ns |
| perplexity→token_entropy | 0.6874 | 0.4231 | ns |
| distinct_1→ece | 1.3084 | 0.3517 | ns |
| distinct_2→ece | 2.5252 | 0.1614 | ns |
| distinct_3→ece | 4.2011 | 0.0770 | ns |
| perplexity→ece | 0.0116 | 0.9124 | ns |

---

## Condition 6: Scale Pythia-1.4B s43
```
旧 (n_perm=5000, 已修复): Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=4/8, K≥4=6/8
新 (n_perm=5000, 重跑):   Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=4/8, K≥4=6/8
```
**Flips: 无。** 条件 6 完全复现。

PG_rev detail:
| Pair | F | p | |
|---|---|---|---|
| distinct_1→token_entropy | 2.4207 | 0.1546 | ns |
| distinct_2→token_entropy | 2.8483 | 0.1460 | ns |
| distinct_3→token_entropy | 3.2136 | 0.1254 | ns |
| perplexity→token_entropy | 1.0677 | 0.2839 | ns |
| distinct_1→ece | 7.2276 | 0.0644 | ns |
| distinct_2→ece | 8.8850 | 0.0372 | **SIG** |
| distinct_3→ece | 10.4690 | 0.0224 | **SIG** |
| perplexity→ece | 0.6850 | 0.3765 | ns |

---

## 关键发现

1. **条件 4 (s42) 有多个 flip**: Diff↓2, PG_fwd↓2, TY↓1。n_perm=5000 比 n_perm=1000 更保守，边界显著对消失了。Thresh 反而增加 2 个（从 6→8）。

2. **条件 5 (s43) PG_rev=0/8**: 反向 Granger 完全不显著，说明 downstream→canary 的因果方向不成立，支持 canary→downstream 的单向因果叙事。

3. **条件 6 完全复现**: 与之前修复后脚本结果完全一致，验证了结果稳定性。

4. **PG_rev 规律**: 显著的反向对集中在 distinct→ece（不是 token_entropy），条件 4 有 3/8，条件 6 有 2/8，条件 5 有 0/8。这暗示 ece 与 distinct 之间可能存在双向耦合。

Full 16-pair 结果已保存至 `results/generalize/analysis/table7_3cond_nperm5000.json`。

---
