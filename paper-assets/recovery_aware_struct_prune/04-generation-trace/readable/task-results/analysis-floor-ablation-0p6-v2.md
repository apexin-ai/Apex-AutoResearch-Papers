# analysis floor ablation 0p6 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_floor_ablation_0p6_v2_20260523T162814_result.json`
- **Structured JSON:** [`1743303c4c106764b78a.json`](../../sessions/17/1743303c4c106764b78a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## floor_ablation_0p6_cka_only_20_v2 结果

### GSM8K Eval
- Accuracy: **62.02%** (818/1319)
- EOS rate: 0.9803
- Avg response length: 252.7 tokens

### GRPO Training (100 steps)
- Final reward: 0.2419
- Final loss: -0.01401
- Peak reward: 0.3394 (step 80)
- Final KL: 0.002682
- 无报错，EXIT_CODE=0

### Checkpoint
- 路径: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.6/`
- 状态: **成功** — model.safetensors (12.3GB) + checkpoint-100 均存在

### W&B
- run_id: `sbmz0hbv`
- run name: `grpo_cka_only_20_floor_0.6`
- project: `recovery_aware_struct_prune`

### Floor Ratio Ablation 对比

| Floor | GSM8K Acc | 备注 |
|-------|-----------|------|
| 0.3 | **65.05%** | 最佳 |
| 0.4 (baseline) | 64.37% | |
| 0.5 | 61.71% | |
| 0.6 | 62.02% | 本次 |

floor=0.6 (62.02%) 与 floor=0.5 (61.71%) 接近，略高 0.3pp，但明显低于 floor=0.3 和 0.4。总体趋势：floor 越高性能越差，但 0.5→0.6 差异不大（可能在置信区间内，±1.34%）。最优 floor 仍是 0.3。

---
