# paper provenance update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_provenance_update_20260525T141104_result.json`
- **Structured JSON:** [`32d23cca22c73b484b2e.json`](../../sessions/32/32d23cca22c73b484b2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新完成，验证通过。

**更新汇总（13 个条目）：**

| 条目 | 旧值 | 新值 |
|------|------|------|
| C004 (abstract) | 7/8 classification (n=8) | 53/56 classification (n=56, AUROC=0.990) |
| C011 (methodology) | 7/8 accuracy (AUROC=0.933) | 53/56 accuracy (AUROC=0.990, n=56) |
| C018 (results) | AUROC=0.933, CI [0.47,1.0] | AUROC=0.990, 53/56 (n=56, F1=0.941, NVE≥1.5) |
| C042 (conclusion) | 7/8 CIVO (n=8, 87.5%) | 53/56 CIVO (n=56, 94.6%, AUROC=0.990) |
| C044 (appendix) | n=32, F1=0.880 | n=56, F1=0.941 |
| C045 (analysis) | n=32, AUROC=0.961, F1=0.880 | n=56, AUROC=0.990, F1=0.941 |
| C047 (methodology) | 29/32, AUROC=0.961, F1=0.880 | 53/56, AUROC=0.990, F1=0.941 |
| C048 (results) | 29/32, n=32, AUROC=0.961 | 53/56, n=56, AUROC=0.990 |
| C049 (abstract) | 29/32, AUROC=0.961 | 53/56, AUROC=0.990 |
| C050 (introduction) | 29/32 | 53/56 |
| C051 (introduction) | AUROC=0.961 | AUROC=0.990 |
| C052 (conclusion) | 29/32, AUROC=0.961 | 53/56, AUROC=0.990 |
| C053 (analysis) | n=32, AUROC=0.961 | n=56, AUROC=0.990 |

所有 evidence 来源统一指向 `plan_034_nve_threshold`，metric 名从 `auroc_n32` 更新为 `auroc_n56`。文件中已无残留旧值（0.961/0.933/n=32/n=8/7∕8/29∕32）。

---
