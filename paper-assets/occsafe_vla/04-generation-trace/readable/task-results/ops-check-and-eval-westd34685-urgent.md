# ops check and eval westd34685 urgent

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_and_eval_westd34685_urgent_20260523T202638_result.json`
- **Structured JSON:** [`3bdd5054cff70e61b3b1.json`](../../sessions/3b/3bdd5054cff70e61b3b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在正常运行。

## 结果

| 实验 | 训练状态 | Eval 状态 | GPU | PID |
|------|---------|----------|-----|-----|
| **cutoff_25k_s0** | 完成 (50005/50005) | 运行中 (10/50 rollouts) | GPU 3 | 463150 |
| **reverse_cutoff_s0** | 完成 (50005/50005) | 运行中 (2/50 rollouts) | GPU 2 | 464454 |

Eval 日志：
- `/tmp/cutoff_25k_s0_eval.log`
- `/tmp/reverse_cutoff_s0_eval.log`

按 ~4.5s/rollout 估算，每个 eval 约 4 分钟完成。

---
