# analysis 14b s43 nperm5000 reverse

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_14b_s43_nperm5000_reverse_20260518T103359_result.json`
- **Structured JSON:** [`3ffd9e20aec9b0afd392.json`](../../sessions/3f/3ffd9e20aec9b0afd392.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据到手。整理结果：

## 1. s43 完整 Table 7 行（n_perm=5000）

### Forward p-values（8 pairs × 5 methods）

| Pair | Naive | Diff | Thresh | TY | PG_fwd |
|------|-------|------|--------|-----|--------|
| entropy→d1 | **0.0015** | **0.0002** | **sig** | **0.0326** | **0.0022** |
| entropy→d2 | **0.0048** | **0.0010** | **sig** | 0.1798 | **0.0046** |
| entropy→d3 | **0.0155** | **0.0052** | **sig** | 0.4964 | **0.0080** |
| entropy→ppl | **0.0137** | 0.3774 | **sig** | 0.7555 | 0.5485 |
| ece→d1 | **1.2e-5** | **6.2e-5** | **sig** | **1e-6** | **0.0044** |
| ece→d2 | **1.4e-5** | **0.0005** | **sig** | **3e-6** | **0.0100** |
| ece→d3 | **2.6e-5** | **0.0030** | **sig** | **3e-6** | **0.0142** |
| ece→ppl | **0.0007** | 0.5214 | **sig** | 0.5086 | 0.5035 |

### Reverse PG p-values（8 pairs）

| Pair | PG_rev p | F | sig |
|------|----------|---|-----|
| d1→entropy | 0.1546 | 2.42 | No |
| d2→entropy | 0.1460 | 2.85 | No |
| d3→entropy | 0.1254 | 3.21 | No |
| ppl→entropy | 0.2839 | 1.07 | No |
| d1→ece | 0.0644 | 7.23 | No |
| d2→ece | **0.0372** | 8.89 | **Yes** |
| d3→ece | **0.0224** | 10.47 | **Yes** |
| ppl→ece | 0.3765 | 0.69 | No |

### Summary counts + K≥4

Per-pair vote counts (5 forward methods):

| Pair | Naive | Diff | Thresh | TY | PG_fwd | votes | K≥4 |
|------|-------|------|--------|-----|--------|-------|-----|
| entropy→d1 | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 | ✓ |
| entropy→d2 | ✓ | ✓ | ✓ | ✗ | ✓ | 4/5 | ✓ |
| entropy→d3 | ✓ | ✓ | ✓ | ✗ | ✓ | 4/5 | ✓ |
| entropy→ppl | ✓ | ✗ | ✓ | ✗ | ✗ | 2/5 | ✗ |
| ece→d1 | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 | ✓ |
| ece→d2 | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 | ✓ |
| ece→d3 | ✓ | ✓ | ✓ | ✓ | ✓ | 5/5 | ✓ |
| ece→ppl | ✓ | ✗ | ✓ | ✗ | ✗ | 2/5 | ✗ |

**s43 Table 7 行：Naive=8/8, Diff=6/8, Thresh=8/8, PG_fwd=6/8, PG_rev=2/8, TY=4/8, K≥4=6/8**

## 2. s42 vs s43 对比（均 n_perm=5000）

| Method | s42 | s43 |
|--------|-----|-----|
| Naive | 7/8 | 8/8 |
| Diff | 6/8 | 6/8 |
| Thresh | 8/8 | 8/8 |
| PG_fwd | 5/8 | 6/8 |
| PG_rev | 0/8 | 2/8 |
| TY | 0/8 | 4/8 |
| K≥4 | 5/8 | 6/8 |

## 3. 注意事项

- **未改动 analyze_generalize.py**。正向分析直接用 `--n_perm 5000` 跑。反向 PG 通过 inline 脚本调用 `permutation_granger_test` 交换 x/y 实现。
- s43 PG_rev=2/8（d2→ece 和 d3→ece 显著），比 s42 的 0/8 高。这两对 reverse F 值较大（8.89/10.47），说明 ece 与 diversity 之间可能存在双向反馈，需注意。
- s43 TY=4/8 vs s42 TY=0/8 差异大，但按 C003 约束，单 seed TY 结果不稳定，不作为支撑证据。

---
