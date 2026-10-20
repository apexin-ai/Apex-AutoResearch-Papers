# code grpo pilot v1

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo_pilot_v1_20260512T231217_result.json`
- **Structured JSON:** [`8bb79c5d9decea2a29bc.json`](../../sessions/8b/8bb79c5d9decea2a29bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Step 2 完成。训练运行正常！

**Step 1 → 2 对比：**

| 指标 | Step 1 | Step 2 |
|------|--------|--------|
| reward/mean | 0.821 | **0.691** |
| reward/std | 0.027 | **0.071** ✅ 更高方差 |
| clipped_ratio | 0.0 | 0.5 (2/4 截断) |
| mean_length | 1362 | 1748 |
| loss | -0.046 | 0.103 |
| grad_norm | 0.049 | 0.042 |
| step_time | 101.5s | 135.0s |

**关键信号：**
- 截断 JSON 恢复生效 — clipped_ratio=0.5 时 reward 仍为 0.691（非 0）
- reward_std > 0 → GRPO 有学习信号
- KL 开始微增 (4.25e-5)
- 梯度正常流动

20 步预计总时间 ~40 min，当前 2/20。训练稳定运行中，将在后台继续。

需要我持续监控到完成，还是你稍后再检查？

---
