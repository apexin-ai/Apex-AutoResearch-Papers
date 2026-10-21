# eval openvla v2 deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla-v2-deploy_20260517T221057_result.json`
- **Structured JSON:** [`25b7c7fa0f70eddb3910.json`](../../sessions/25/25b7c7fa0f70eddb3910.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务已完成。实验 `eval-openvla-object-vla-only-seed42-v2` 已在 bjb1-18228 上运行中，registry 已更新为 RUNNING。

**当前状态：**
- 进度：50%（5/10 tasks completed, 90/100 episodes done）
- 当前总 SR：68.9%（62/90）
- 最新 task SR：80%（pick up chocolate pudding → basket）
- 预计剩余时间：~2-3 min（基于 32s/task pace）

**实验参数：**
- Model: `openvla-7b-libero-object` (4× safetensors, transformers 4.40.1)
- Task suite: `libero_object`, 10 tasks × 10 trials
- Seed: 42, center_crop=True
- Server: bjb1-18228, cuda:1
- Log dir: `/root/acr-vla-conformal-refinement/results/eval-openvla-object-vla-only-seed42-v2`

---
