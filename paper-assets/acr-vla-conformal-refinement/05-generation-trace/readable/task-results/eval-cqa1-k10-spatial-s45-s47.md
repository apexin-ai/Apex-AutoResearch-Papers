# eval cqa1 k10 spatial s45 s47

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cqa1-k10-spatial-s45-s47_20260525T010843_result.json`
- **Structured JSON:** [`65bcb58d9d56b187655e.json`](../../sessions/65/65bcb58d9d56b187655e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已成功启动并验证：

| 实验 | GPU | tmux session | 状态 |
|------|-----|-------------|------|
| eval-k10-tau025-spatial-s45 | cuda:0 | eval-k10-spatial-s45 | 正在加载 SmolVLA 模型 |
| eval-k10-tau025-spatial-s47 | cuda:1 | eval-k10-spatial-s47 | 正在加载 SmolVLA 模型 |

参数确认：`--mode adaptive_conformal_crm --K 10 --conformal_threshold 0.25 --benchmark spatial --n_rollouts 20 --max_correction_norm 0.2`，seed 分别为 45 和 47。Registry 已更新为 RUNNING。

cqa1-32758 当前 GPU 分配：GPU 0-1 跑 s45/s47，GPU 2-4 空闲，GPU 5 仍有旧实验。

---
