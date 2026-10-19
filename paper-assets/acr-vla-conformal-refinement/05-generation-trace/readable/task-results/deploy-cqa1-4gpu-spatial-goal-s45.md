# deploy cqa1 4gpu spatial goal s45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-4gpu-spatial-goal-s45_20260523T212934_result.json`
- **Structured JSON:** [`95129f9aecc9f24ae960.json`](../../sessions/95/95129f9aecc9f24ae960.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署完成。汇总：

**4 个实验已启动，Registry 已更新为 RUNNING：**

| GPU | 实验 | PID | tmux session |
|-----|------|-----|--------------|
| cuda:0 | Goal K2mean s45 | 456787 | eval-goal-k2mean-s45 |
| cuda:1 | Spatial VLA-only s45 | 456947 | eval-spatial-vla-s45 |
| cuda:3 | Spatial CRM s45 | 457405 | eval-spatial-crm-s45 |
| cuda:5 | Spatial Reconvla s45 | 457485 | eval-spatial-reconvla-s45 |

**GPU 状态：** cuda:0 已加载模型（1263 MiB），cuda:1/3/5 初始化中。cuda:2（Object Reconvla s46）和 cuda:4（Object Reconvla s45）未受影响，正常运行。

---
