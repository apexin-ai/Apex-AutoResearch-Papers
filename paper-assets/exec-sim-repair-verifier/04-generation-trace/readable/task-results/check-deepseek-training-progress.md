# check deepseek training progress

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_deepseek-training-progress_20260517T143454_result.json`
- **Structured JSON:** [`19e61b68e748ab364636.json`](../../sessions/19/19e61b68e748ab364636.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

| # | 实验 | GPU | Step | Max | Epoch | 进度 | ETA | Status |
|---|------|-----|------|-----|-------|------|-----|--------|
| 1 | deepseek-cls-repo-v4 | cuda:0 | 6210 | 6633 | 2.81/3 | 94% | ~1h10m | running |
| 2 | deepseek-cwm-repo | cuda:1 | 13012 | 13266 | 2.94/3 | 98% | ~34m | running |
| 3 | deepseek-cls-repo-s123 | cuda:2 | 6575 | 6633 | 2.97/3 | 99% | ~10m | running |
| 4 | deepseek-cwm-repo-s123 | cuda:3 | ~8844 | 13266 | 2.0/3 | 67% | ~10.5h | running (eval中) |

**关键信息:**

- **所有 4 个进程均存活**，PID 与预期一致，GPU 利用率 90-100%
- **Exp 3 (cls-repo-s123)** 没有 crash，正常运行，即将完成（~10 分钟）
- **Exp 4 (cwm-repo-s123)** 正在做 epoch 2 的 eval（71%, 3332/4668），eval 完成后还需训练 epoch 3（4422 steps），预计还需 ~10.5h
- **Exp 2 和 3** 将在 1 小时内完成
- **Exp 1** 约 1 小时 10 分钟完成
- 所有 cls 实验的 eval_loss 为 nan（可能需要关注）

---
