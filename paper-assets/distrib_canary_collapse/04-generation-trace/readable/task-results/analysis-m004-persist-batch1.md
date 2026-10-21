# analysis m004 persist batch1

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_m004_persist_batch1_20260518T111739_result.json`
- **Structured JSON:** [`f4c50ee2262d4e1de87f.json`](../../sessions/f4/f4c50ee2262d4e1de87f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## **⚠️ FLIP DETECTED: OPT-1.3B Diff 8/8 → 6/8**

注意：Diff (differenced_xcorr) 不使用 n_perm，此变化并非由 n_perm 1000→5000 导致，而是代码或数据版本差异。PG 相关值全部稳定。

---

## 条件 1: Baseline Pythia-410M s42
| Pair | PG_fwd_p | PG_rev_p | fwd_sig | rev_sig |
|------|----------|----------|---------|---------|
| ent→d1 | 0.0002 | 0.4921 | ✓ | ✗ |
| ent→d2 | 0.0012 | 0.4805 | ✓ | ✗ |
| ent→d3 | 0.0012 | 0.5047 | ✓ | ✗ |
| ent→ppl | 0.5841 | 0.9658 | ✗ | ✗ |
| ece→d1 | 0.0002 | 0.0274 | ✓ | ✓ |
| ece→d2 | 0.0006 | 0.0286 | ✓ | ✓ |
| ece→d3 | 0.0006 | 0.0306 | ✓ | ✓ |
| ece→ppl | 0.8040 | 0.1418 | ✗ | ✗ |

Summary (8 canonical pairs):
  Naive=8/8, Diff=8/8, Thresh=8/8, PG_fwd=6/8, PG_rev=3/8, TY=4/8, K≥4=6/8
Old:
  Naive=8/8, Diff=8/8, Thresh=8/8, PG_fwd=6/8, PG_rev=3/8, TY=4/8, K≥4=6/8
Flip: 无

---

## 条件 2: OPT-1.3B s42
| Pair | PG_fwd_p | PG_rev_p | fwd_sig | rev_sig |
|------|----------|----------|---------|---------|
| ent→d1 | 0.0012 | 0.8778 | ✓ | ✗ |
| ent→d2 | 0.0034 | 0.9622 | ✓ | ✗ |
| ent→d3 | 0.0128 | 0.9880 | ✓ | ✗ |
| ent→ppl | 0.8540 | 0.8982 | ✗ | ✗ |
| ece→d1 | 0.0012 | 0.0276 | ✓ | ✓ |
| ece→d2 | 0.0046 | 0.0448 | ✓ | ✓ |
| ece→d3 | 0.0126 | 0.0728 | ✓ | ✗ |
| ece→ppl | 0.6275 | 0.1886 | ✗ | ✗ |

Summary (8 canonical pairs):
  Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=6/8, K≥4=6/8
Old:
  Naive=8/8, Diff=8/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=6/8, K≥4=6/8
Flip: ⚠️ Diff: 8/8 → 6/8（非 n_perm 引起）

---

## 条件 3: Scale Pythia-1.4B s42
| Pair | PG_fwd_p | PG_rev_p | fwd_sig | rev_sig |
|------|----------|----------|---------|---------|
| ent→d1 | 0.0274 | 0.8826 | ✓ | ✗ |
| ent→d2 | 0.0346 | 0.7942 | ✓ | ✗ |
| ent→d3 | 0.0532 | 0.7359 | ✗ | ✗ |
| ent→ppl | 0.7163 | 0.9670 | ✗ | ✗ |
| ece→d1 | 0.0042 | 0.5153 | ✓ | ✗ |
| ece→d2 | 0.0086 | 0.5123 | ✓ | ✗ |
| ece→d3 | 0.0216 | 0.5165 | ✓ | ✗ |
| ece→ppl | 0.5739 | 0.3177 | ✗ | ✗ |

Summary (8 canonical pairs):
  Naive=7/8, Diff=6/8, Thresh=8/8, PG_fwd=5/8, PG_rev=0/8, TY=0/8, K≥4=5/8
Old:
  Naive=7/8, Diff=6/8, Thresh=8/8, PG_fwd=5/8, PG_rev=0/8, TY=0/8, K≥4=5/8
Flip: 无

---

**结论**：n_perm 1000→5000 对 PG significance 无影响（PG_fwd 和 PG_rev 在 3 个条件中全部一致）。唯一变化是 OPT Diff 从 8/8 降至 6/8，但 `diff_xcorr` 不使用 permutation，说明此差异来自代码/数据版本变更而非本次重跑。

产出已保存至 `artifacts/M004_nperm5000/` 下各子目录。

---
