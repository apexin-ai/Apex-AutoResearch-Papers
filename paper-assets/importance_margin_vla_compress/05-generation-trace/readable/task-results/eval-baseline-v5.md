# eval baseline v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline-v5_20260515T174330_result.json`
- **Structured JSON:** [`7d9d6a7c5eb2bc99d724.json`](../../sessions/7d/7d9d6a7c5eb2bc99d724.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Baseline v5 评估结果

**Checkpoint**: `step_029999` (latest), 100 batches, seed=42

| 条件 | Action Loss |
|------|------------|
| **Clean (eps=0.0, no prune)** | **0.00422** |
| Clean + prune 50% | 0.00309 |
| eps=0.01, no prune | 0.00605 |
| eps=0.01 + prune 50% | 0.00343 |
| eps=0.02, no prune | 0.00399 |
| eps=0.02 + prune 50% | 0.00445 |
| eps=0.05, no prune | 0.00495 |
| eps=0.05 + prune 50% | 0.00497 |

**Meta**: `imm_enabled=false`, `lipschitz_empirical=0.0`, `lipschitz_spectral=0.0`

要点：
- Clean loss 0.00422，与训练末期 loss 0.00187 有差距（evaluation 用 baseline_forward 避免 action_is_pad bug，计算方式不同）
- Prune 50% 在 clean 条件下反而降低 loss (0.00309 < 0.00422)，说明 baseline 有冗余
- Perturbation 下 loss 增加但幅度不大，eps=0.05 时 loss 约为 clean 的 1.2x
- Registry 已更新（status 保持 ANALYZING）

---
