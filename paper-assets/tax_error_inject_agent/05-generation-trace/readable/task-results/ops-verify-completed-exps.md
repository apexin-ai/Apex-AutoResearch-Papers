# ops verify completed exps

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-completed-exps_20260515T175429_result.json`
- **Structured JSON:** [`e4f668b96ebe6d3b6e46.json`](../../sessions/e4/e4f668b96ebe6d3b6e46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已确认完成，registry 已更新为 DONE/success。

---

### 实验 1: v4-taxei-fixed-inject10-s0

| 指标 | 值 |
|------|-----|
| 状态 | 正常完成，3 epochs / 1635 steps |
| train_loss (avg) | 0.4238 |
| final_loss (step 1635) | 0.3102 |
| final_token_acc | 0.8822 |
| 训练时间 | 58 min |
| checkpoint | `checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635` |

### 实验 2: v4-training-dynamics-forward-v2

| 指标 | 值 |
|------|-----|
| 状态 | 正常完成 (EXIT_CODE=0) |
| 计算子集 | vanilla_full, taxei_full, random_full, taxei_inject10/25/50 |
| inject50 loss (injected) | mean=0.8185, std=0.1919, n=2179 |
| inject50 loss (clean) | mean=0.8514, std=0.1705, n=2179 |
| per-operator | C1=0.649, C4=0.678, P1=0.637, P2=0.654 |
| 产出 | 6 个 JSON + 3 组图表 (subset_comparison, operator_breakdown, dose_response) |
| 输出目录 | `artifacts/training_dynamics_v2/` |

---
