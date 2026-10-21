# analysis check accum mix50

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_check_accum_mix50_20260522T045137_result.json`
- **Structured JSON:** [`ed743961d63e8dad0cad.json`](../../sessions/ed/ed743961d63e8dad0cad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态: 已完成 ✓

进程 907272 已结束，pipeline 耗时 2.38h，exit code 0。

### 关键 Metrics

| 指标 | 值 |
|------|-----|
| Overall accuracy | 0.6865 |
| Balanced accuracy | 0.6865 |
| d1-d3 balanced acc | 0.5834 |
| Full-replacement baseline | 0.8428 |
| **Delta vs baseline** | **-0.1563** |

### Per-depth Recall

| Depth | Recall | 样本数 |
|-------|--------|--------|
| d0 | 0.996 | 5000 |
| d1 | 0.692 | 5000 |
| d2 | 0.417 | 5000 |
| d3 | 0.641 | 5000 |

### 观察

mix50（50% human text 混入）使 overall accuracy 从 baseline 0.8428 下降到 0.6865（-15.6pp）。d0 仍几乎完美区分，但 d2 recall 最弱（0.417），大量 d2 样本被误分为 d1 或 d3。d3 recall（0.641）高于 d2，说明深层递归的特征仍有一定可分性，但中间层（d2）在混合人类文本后最易混淆。

---
