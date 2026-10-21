# ssh traj14b s123 check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_traj14b-s123-check_20260523T104600_result.json`
- **Structured JSON:** [`cc19b1006cc79a8719fa.json`](../../sessions/cc/cc19b1006cc79a8719fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能已被手动清理或从未创建）。Registry 已更新。

## 汇报

### traj14b-func-s123 — 训练成功
- Best checkpoint: `/root/autodl-tmp/checkpoints/traj14b-func-s123/checkpoint-252` (step 252, epoch 1)
- Best eval_loss: **0.0836**
- Final eval_loss (epoch 3): 0.1035
- Train loss: 0.1266
- `best/` 目录已生成（adapter_model.safetensors ~80MB）

### 其他两个 seed — 也已完成

| Seed | Final eval_loss | Train loss | best/ |
|------|----------------|------------|-------|
| s42  | 0.0958 | 0.1312 | ✓ |
| s456 | 0.0971 | 0.1257 | ✓ |

三个 seed 的 best eval_loss 范围：0.0836–0.0971，s123 最优。

### GPU 状态
- GPU 0–2: 空闲（0% utilization, 0 MiB）
- GPU 3: 92% utilization, 23761 MiB — 仍有其他任务在运行

---
