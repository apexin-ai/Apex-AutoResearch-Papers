# fix kill old eval tmux

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-old-eval-tmux_20260517T101624_result.json`
- **Structured JSON:** [`933ccf356a4f5cf6b510.json`](../../sessions/93/933ccf356a4f5cf6b510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| 操作 | 状态 |
|------|------|
| `eval_gradient_postsft` | 已杀掉（之前就不存在了） |
| `eval_gradient_postsft_v2` | 也不存在 |

当前活跃 tmux sessions：
- `scoring_ablation_v2` — cuda:1, 12880 MiB, 76% util
- `scoring_ablation_random` — cuda:0, 27394 MiB, 100% util

v2 的 eval_gradient 任务应该是已经跑完或被替换为 scoring_ablation 系列了。两张卡都在正常跑实验。

---
