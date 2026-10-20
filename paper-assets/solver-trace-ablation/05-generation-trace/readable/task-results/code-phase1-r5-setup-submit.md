# code phase1 r5 setup submit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase1-r5-setup-submit_20260513T205222_result.json`
- **Structured JSON:** [`9d676e73a8e117043d60.json`](../../sessions/9d/9d676e73a8e117043d60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已提交：

| 实验 | GPU | 改动 | PID |
|------|-----|------|-----|
| `sta-phase1-exec-only-r5` | cuda:0 | K=8 | 75890 |
| `sta-phase1-exec-sta-r5` | cuda:1 | K=8 + full `sta_reward` | 75968 |

代码改动总结：
- `scripts/train_grpo.py` line 39: import 增加 `sta_reward`
- `scripts/train_grpo.py` line 124: execution_sta 分支 `fast_sta_reward` → `sta_reward`（完整 component ablation，连续 ISR 0.0-1.0）
- 两个 YAML `num_generations: 4` → `8`

---
