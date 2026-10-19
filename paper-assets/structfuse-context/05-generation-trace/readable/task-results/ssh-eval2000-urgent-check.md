# ssh eval2000 urgent check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval2000_urgent_check_20260514T025319_result.json`
- **Structured JSON:** [`2a0898e8da35b7e557be.json`](../../sessions/2a/2a0898e8da35b7e557be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval@2000 已出。** 当前 step 已到 2250，训练继续进行中。

4 次 eval 汇总：

| Step | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| 500 | 0.4869 | 0.5332 | 0.9540 | 1.0 |
| 1000 | **0.4651** | **0.5527** | **0.9594** | 1.0 |
| 1500 | 0.5365 | 0.5228 | 0.9550 | 1.0 |
| 2000 | 0.5162 | 0.5228 | 0.9544 | 1.0 |

关键发现：
- **Best checkpoint 在 step 1000**（val_loss=0.4651, R@1=0.5527）
- Step 1500/2000 均未超越 best，val_loss 回升，R@1 从 0.5527 降至 0.5228
- Epoch 2 开始后（~step 1400）出现过拟合迹象：train loss 持续下降（0.04），但 val_loss 和 R@1 不再改善
- `early_stopping_patience=0`，但脚本仍在继续（可能 patience=0 表示不启用 early stopping）
- 进程 73558 存活，状态 Sl，已运行 9h14m，当前 step 2250

---
