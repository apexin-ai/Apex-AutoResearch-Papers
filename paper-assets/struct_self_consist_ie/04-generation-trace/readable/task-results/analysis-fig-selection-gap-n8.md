# analysis fig selection gap n8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig_selection_gap_n8_20260515T143927_result.json`
- **Structured JSON:** [`c4fc6514159b769645ce.json`](../../sessions/c4/c4fc6514159b769645ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**生成的文件：**
- 服务器：`output/figures/fig_selection_gap.pdf` + `.png`
- 本地：`docs/paper/figures/fig_selection_gap.pdf` + `.png`（已覆盖 N=16 版本）

**每个 bar 的精确数值（NER N=8, 3-seed, pp）：**

| Signal | ΔF1 vs Greedy | ± std |
|--------|--------------|-------|
| VC | -2.540 | 0.877 |
| SJ | -0.433 | 1.026 |
| FK | -0.438 | 0.966 |
| EM | -1.145 | 0.734 |
| LP | +0.038 | 0.500 |

参考线：oracle +13.1 pp, random -3.9 pp

**RE N=8 数据不存在**——搜索了 `output/` 全部 JSON，没有 Qwen SciERC RE N=8 的 selection F1 数据，仅画了 NER 单组。

---
