# deploy k2 adaptive spatial cqa1

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_k2-adaptive-spatial-cqa1_20260525T025156_result.json`
- **Structured JSON:** [`f38a40a2a88270479efe.json`](../../sessions/f3/f38a40a2a88270479efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | eval-k2-adaptive-spatial-s42 | RUNNING（rollout 5/20，5/5 success） |
| 1 | eval-vla-only-spatial-cqa1-s42 | RUNNING（10 tasks loaded） |
| 2 | eval-k2-adaptive-spatial-s43 | RUNNING |
| 3 | eval-vla-only-spatial-cqa1-s43 | RUNNING |
| 4 | eval-k2-adaptive-spatial-s44 | RUNNING |
| 5 | eval-vla-only-spatial-cqa1-s44 | RUNNING |

6 个 tmux session 全部启动，6 GPU 全部活跃（13-26% util，6.4GB mem each）。日志写入 `/root/autodl-tmp/logs/`。Registry 全部置 RUNNING。

---
