# deploy k2 adaptive spatial bjb1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_k2-adaptive-spatial-bjb1_20260525T025143_result.json`
- **Structured JSON:** [`962a9c61301709c57a57.json`](../../sessions/96/962a9c61301709c57a57.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

| exp_id | seed | GPU | tmux | 状态 |
|--------|------|-----|------|------|
| eval-k2-adaptive-spatial-s46 | 46 | cuda:0 (5544 MiB) | ✅ | RUNNING, rollout 5/20 |
| eval-k2-adaptive-spatial-s48 | 48 | cuda:2 (5169 MiB) | ✅ | RUNNING, rollout 5/20 |
| eval-k2-adaptive-spatial-s49 | 49 | cuda:3 (3948 MiB) | ✅ | RUNNING, rollout 5/20 |

注: `submit_training_job` 工具未在可用工具列表，改用 `ssh_execute` + tmux 启动并通过 `update_registry` 推进状态 PREPARING→PENDING→QUEUED→RUNNING（带 spec 元数据）。cuda:1/4/5 的 VLA-only baseline 未触碰。

---
