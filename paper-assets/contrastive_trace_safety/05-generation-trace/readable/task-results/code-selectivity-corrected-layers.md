# code selectivity corrected layers

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_selectivity_corrected_layers_20260517T175238_result.json`
- **Structured JSON:** [`4b9ff6adf3c74408a278.json`](../../sessions/4b/4b9ff6adf3c74408a278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。汇总如下：

## Selectivity at Corrected Layers — 结果

| Model | Layer (biased) | Selectivity (old) | Layer (corrected) | Selectivity (new) | >5pp? |
|-------|---------------|-------------------|-------------------|-------------------|-------|
| QwQ-32B | L2 | 15.3pp | **L60** | **14.4pp** | PASS |
| R1-32B | L10 | 7.5pp | **L63** | **19.7pp** | PASS |

**两个corrected layer的selectivity均通过5pp阈值。**

关键数据：
- **QwQ-32B L60**: real_acc=66.7%, random_mean=52.3%±5.1%, selectivity=14.4pp, position baseline=70.5%
- **R1-32B L63**: real_acc=74.6%, random_mean=54.9%±6.0%, selectivity=19.7pp, position baseline=62.4%

R1-32B在corrected layer (L63)的selectivity反而大幅高于biased layer (L10)，从7.5pp提升到19.7pp，说明探针在高层提取到了更多超越位置信息的commitment信号。QwQ-32B基本持平（15.3→14.4pp）。

---
