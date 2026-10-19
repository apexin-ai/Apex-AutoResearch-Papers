# ops deploy fewshot transfer eval

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_fewshot_transfer_eval_20260521T010420_result.json`
- **Structured JSON:** [`524afccbb343a5e041a2.json`](../../sessions/52/524afccbb343a5e041a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，dry-run 结果：

| Method | AUROC | ECE | Brier | N |
|---|---|---|---|---|
| zero_shot | 0.6607 | 0.2673 | 0.2949 | 14042 |
| mean_shift | 0.6607 | 0.2598 | 0.2826 | 14042 |
| **few_shot_25** | **0.7097** | **0.2053** | **0.2479** | **14017** |

few-shot 功能正常：
- N=14017（= 14042 - 25），正确排除了 few-shot 样本
- few_shot_25 在所有指标上优于 zero_shot 和 mean_shift（AUROC +5pp，ECE -6pp，Brier -5pp）

---
