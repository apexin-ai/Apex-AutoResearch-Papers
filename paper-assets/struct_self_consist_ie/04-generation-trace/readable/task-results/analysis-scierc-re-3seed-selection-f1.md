# analysis scierc re 3seed selection f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_re_3seed_selection_f1_20260515T132231_result.json`
- **Structured JSON:** [`e344b092005df8b8e33c.json`](../../sessions/e3/e344b092005df8b8e33c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

RE 结果已保存到本地。汇总：

**SciERC RE N=16 3-seed Selection F1 结果（551 instances, macro-averaged）：**

| Method | Mean F1 | ±std | Δ greedy | p(Fisher) |
|--------|---------|------|----------|-----------|
| Greedy | 0.29144 | 0.00016 | — | — |
| Random | 0.26242 | 0.00143 | — | — |
| VC | 0.28369 | 0.00161 | -0.00774 | 0.973 |
| SJ | 0.28122 | 0.00505 | -0.01022 | 0.993 |
| FK | 0.28260 | 0.00515 | -0.00884 | 0.985 |
| EM | 0.27678 | 0.00737 | -0.01466 | 0.999 |
| **LP** | **0.29875** | 0.00654 | **+0.00731** | **0.058** |
| Oracle | 0.46279 | 0.00627 | — | — |

RE 上只有 LP（log-probability）信号正向（+0.73 pp），接近显著（p=0.058）。所有一致性信号（VC/SJ/FK/EM）均略低于 greedy。Oracle gap 很大（17.1 pp），说明 RE 的 selection 空间大但当前一致性信号无法有效选择。

产出文件：
- 服务器：`output/analysis_scierc_re_n16_3seed_selection_f1.json`（RE only）
- 服务器：`output/analysis_scierc_n16_3seed_selection_f1_merged.json`（NER+RE 合并）
- 本地：`artifacts/analysis_scierc_re_n16_3seed_selection_f1.json`

---
