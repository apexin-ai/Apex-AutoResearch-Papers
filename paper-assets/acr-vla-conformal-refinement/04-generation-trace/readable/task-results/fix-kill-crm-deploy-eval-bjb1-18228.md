# fix kill crm deploy eval bjb1 18228

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-crm-deploy-eval-bjb1-18228_20260524T092637_result.json`
- **Structured JSON:** [`7c0e4a8847fe04fca0ca.json`](../../sessions/7c/7c0e4a8847fe04fca0ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：任务已由前一个 Worker 完成，无需操作。**

当前 GPU 1+2 状态：

| GPU | tmux session | PID | 实验 | 状态 |
|-----|-------------|-----|------|------|
| 1 | `long-vla-s47` | 307463 | eval-supp-long-vla-only-s47-r4 | 正在加载任务 |
| 2 | `goal-vla-s47` | 307664 | eval-supp-goal-vla-only-s47-r3 | 运行中 (task1: 3/5 success at rollout 5/20) |

- CRM 训练（`train-crm-pi05-spatial-k1` / `train-crm-pi05-goal-k1`）在 registry 中不存在，GPU 上也没有对应进程
- 目标 eval 实验已在运行且 registry 已标 RUNNING，无需重复部署或更新
- GPU 0/3 的 precompute 任务未受影响

---
