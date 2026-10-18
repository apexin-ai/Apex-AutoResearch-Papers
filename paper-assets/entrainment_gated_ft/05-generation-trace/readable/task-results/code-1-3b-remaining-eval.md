# code 1 3b remaining eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_1_3b_remaining_eval_20260518T151747_result.json`
- **Structured JSON:** [`add0de59f763b1eb1567.json`](../../sessions/ad/add0de59f763b1eb1567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部评测完成。

## 完整结果表（4 模型 × 6 tasks, acc）

| Model | lambada | hellaswag | winogrande | arc_easy | arc_challenge | mmlu |
|---|---|---|---|---|---|---|
| **GDN-pure** | 0.5430 | 0.4646 | 0.6077 | 0.7125 | 0.3712 | 0.2606 |
| **GDN-hybrid-12-1** | 0.5337 | 0.4623 | 0.6117 | 0.6995 | 0.3746 | 0.2541 |
| **Transformer** | 0.4805 | 0.4512 | 0.6180 | 0.7113 | 0.3729 | 0.2358 |
| **RetNet-pure** | 0.5166 | 0.4419 | 0.6038 | 0.7121 | 0.3729 | 0.2452 |
| **RetNet-hybrid-12-1** | 0.5071 | 0.4473 | 0.5888 | 0.7214 | 0.3703 | 0.2389 |

## 结果文件路径

- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-pure.json`
- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-GatedDeltaNet-hybrid-12-1.json`
- `/root/entrainment_gated_ft/lm_eval_clean/transformer_1.3B_baseline.json`
- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-pure.json`
- `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-RetNet-hybrid-12-1.json`

## 执行情况

- GDN-pure、GDN-hybrid-12-1、Transformer、RetNet-pure 四个模型已有完整结果，无需重跑
- 仅 **RetNet-hybrid-12-1** 需要新跑，已完成（6 tasks，118K loglikelihood requests，~6 分钟推理）
- 无报错，所有数值合理

---
