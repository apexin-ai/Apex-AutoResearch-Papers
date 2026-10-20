# ops rasp v9 completion check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rasp-v9-completion-check_20260516T033742_result.json`
- **Structured JSON:** [`ffd1b83632059dce5bde.json`](../../sessions/ff/ffd1b83632059dce5bde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，cron 已删除。汇报：

**训练状态**: 成功完成 30/30 steps，耗时 3h28m25s，无 error。

**Reward 轨迹** (展示 collapse):
| Step | Reward | frac_zero_std |
|------|--------|---------------|
| 10 | 0.015 | 87.5% |
| 20 | **0.039** (peak) | 80.0% |
| 30 | 0.021 ↓ | **95.0%** |

Reward 在 step 20 达到峰值 0.039 后回落，frac_zero_std 升至 95%——确认 RASP 模型发生了 collapse。Peak checkpoint 在 **checkpoint-15 或 checkpoint-20** 附近。

**Checkpoints**: checkpoint-10, checkpoint-15, checkpoint-20, checkpoint-25, checkpoint-30（save_steps=5 成功捕获了 collapse 前的 checkpoints，符合 v9 设计目标）

**wandb**: `mrikafz3`

**westb-23072 cuda:0 现在空闲**，可用于下一个任务。

---
