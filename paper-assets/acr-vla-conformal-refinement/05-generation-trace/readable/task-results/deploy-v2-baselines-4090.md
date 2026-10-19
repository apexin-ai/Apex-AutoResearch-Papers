# deploy v2 baselines 4090

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_v2-baselines-4090_20260526T132345_result.json`
- **Structured JSON:** [`e8ef94ab4dc0b446124f.json`](../../sessions/e8/e8ef94ab4dc0b446124f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 π0.5 VLA-only 4090 baseline 全部部署完成。

| exp_id | server | GPU | PID | tmux session |
|--------|--------|-----|-----|--------------|
| pi05-vla-only-spatial-s42-4090 | bjb1-18228 | cuda:0 | 150245 | pi05-vla-only-spatial-s42-4090 |
| pi05-vla-only-goal-s42-4090 | bjb1-18228 | cuda:1 | 151593 | pi05-vla-only-goal-s42-4090 |
| pi05-vla-only-object-s42-4090 | bjb1-18228 | cuda:3 | 153192 | pi05-vla-only-object-s42-4090 |
| pi05-vla-only-long-s42-4090 | bjb2-24035 | cuda:0 | 41869 | pi05-vla-only-long-s42-4090 |

GPU 状态确认：bjb1-18228 cuda:0/1/3 空闲（cuda:2 已被其他任务占用，跳过），bjb2-24035 cuda:0 空闲。所有任务 spec/hypothesis 已写入 registry。

---
