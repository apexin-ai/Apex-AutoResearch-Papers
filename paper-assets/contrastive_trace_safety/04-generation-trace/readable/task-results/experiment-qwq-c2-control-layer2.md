# experiment qwq c2 control layer2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_qwq_c2_control_layer2_20260517T013924_result.json`
- **Structured JSON:** [`342b20d04fb2f8eaa805.json`](../../sessions/34/342b20d04fb2f8eaa805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。QwQ-32B Layer 2 selectivity 重算结果：

| Metric | Value |
|--------|-------|
| Real probe bal_acc | 67.8% |
| Random probe mean | 52.6% ± 7.6% |
| **Selectivity** | **15.3pp** |
| Position baseline bal_acc | 70.6% |
| Position pre-CP FPR | 0.2500 |
| HS probe pre-CP FPR | 0.2903 |

**关键发现**：Layer 2 selectivity = 15.3pp，比之前错误的 layer 1 结果（18.9pp）低 3.6pp。

**问题**：Position baseline (70.6%) 高于 HS probe (67.8%)，说明在 layer 2 上，hidden states probe 的分类能力不如简单的位置特征。这意味着 layer 2 的 selectivity 15.3pp 可能主要来自位置信号而非真正的语义内容编码，对论文的 "selectivity 12-19pp" claim 需要谨慎解读。

---
