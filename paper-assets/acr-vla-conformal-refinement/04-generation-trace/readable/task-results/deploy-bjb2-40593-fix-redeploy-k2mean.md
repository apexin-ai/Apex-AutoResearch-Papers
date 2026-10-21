# deploy bjb2 40593 fix redeploy k2mean

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-40593-fix-redeploy-k2mean_20260523T083034_result.json`
- **Structured JSON:** [`11bb8b107fe91699a049.json`](../../sessions/11/11bb8b107fe91699a049.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，运行正常：

- **GPU**: RTX 4090 D, 5774MiB 占用, 13% utilization, PID 127177
- **进度**: SmolVLA 已加载, LIBERO goal 10 个 task 已加载，即将开始 rollout
- **参数**: K=2, mean, goal, seed=42, 20 rollouts
- **根因**: 原失败是 conda 未激活导致 `python: command not found`（exit 127），evaluate.py 本身已修复无需改动
- **修正**: `--suite` 改为 `--benchmark`（代码实际参数名）
- **Registry**: `eval-supp-k2mean-goal-s42-r2` 已注册为 RUNNING

---
