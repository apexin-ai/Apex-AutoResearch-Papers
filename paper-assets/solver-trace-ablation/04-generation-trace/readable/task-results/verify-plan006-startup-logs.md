# verify plan006 startup logs

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_plan006-startup-logs_20260514T094957_result.json`
- **Structured JSON:** [`395af56fe01192e388cb.json`](../../sessions/39/395af56fe01192e388cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已确认：

| 实验 | 数据路径 | 进程状态 | GPU | 错误 |
|------|---------|---------|-----|------|
| plan006-prolog-exec-s42 (PID 506015) | `data/train_500_seed42.jsonl` ✅ | 存活，运行 41 秒 | CUDA_VISIBLE_DEVICES=0 | 无 |
| plan006-prolog-sta-s42 (PID 506117) | `data/train_500_seed42.jsonl` ✅ | 存活，运行 38 秒 | CUDA_VISIBLE_DEVICES=1 | 无 |

两个实验已正常进入训练循环（step 1-2 已完成），数据路径符合 C001 约束，GPU 分配符合 C002/C005 约束。vLLM 版本警告可忽略。

---
