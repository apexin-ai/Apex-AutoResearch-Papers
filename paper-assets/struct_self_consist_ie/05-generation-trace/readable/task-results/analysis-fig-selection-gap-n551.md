# analysis fig selection gap n551

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig_selection_gap_n551_20260515T134355_result.json`
- **Structured JSON:** [`854c6f2e341521d0cd0d.json`](../../sessions/85/854c6f2e341521d0cd0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。fig_selection_gap.pdf 已用 n=551 三种子数据重新生成并同步到本地。

**各 bar 精确数值（pp，±std across 3 seeds）：**

| Signal | NER ΔF1 | RE ΔF1 |
|--------|---------|--------|
| VC | -3.09 ± 0.54 | -0.77 ± 0.17 |
| SJ | -0.05 ± 0.22 | -1.02 ± 0.52 |
| FK | +0.15 ± 0.21 | -0.88 ± 0.52 |
| EM | -0.87 ± 0.37 | -1.47 ± 0.74 |
| LP | **+0.45 ± 0.68** | **+0.73 ± 0.67** |

参考线：oracle NER +16.87 / RE +17.14 pp；random NER -3.37 / RE -2.90 pp。

LP 双任务唯一正向，与 Table 3 一致。

---
