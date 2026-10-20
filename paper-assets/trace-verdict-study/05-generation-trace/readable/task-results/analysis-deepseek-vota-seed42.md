# analysis deepseek vota seed42

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_vota_seed42_20260515T130802_result.json`
- **Structured JSON:** [`79211eecbbdb83606a8d.json`](../../sessions/79/79211eecbbdb83606a8d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 和 artifact 都已更新。汇总：

## deepseek_vota_seed42 结果

| Metric | Value | 95% CI |
|--------|-------|--------|
| **Accuracy** | **84.45%** | [82.6%, 86.4%] |
| Majority baseline | 71.51% | — |
| Lift | +12.94pp | [+11.1pp, +14.9pp] |
| Pass P/R/F1 | 0.82 / 1.00 / 0.90 | — |
| Fail P/R/F1 | 1.00 / 0.45 / 0.63 | — |
| Final train loss | 0.0522 | — |
| Best eval loss | 0.0679 (epoch 1) | — |

**结论：success**
- 84.5% 显著高于 no_trace baseline 75.1%（CI 不重叠），VOTA 对 DeepSeek 有效
- 但远低于 Qwen VOTA 99.2%（-14.75pp），模型选择对 trace 利用效率影响巨大
- Pass 偏向严重（fail recall 仅 45.4%），过拟合明显（eval loss epoch 1→3: 0.068→0.112）

---
