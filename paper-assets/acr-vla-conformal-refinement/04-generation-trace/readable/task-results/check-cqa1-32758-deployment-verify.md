# check cqa1 32758 deployment verify

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1-32758-deployment-verify_20260525T094922_result.json`
- **Structured JSON:** [`c969bd542b3ca2d9c813.json`](../../sessions/c9/c969bd542b3ca2d9c813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，6 个实验全部在运行：

| GPU | 实验 | 状态 | 显存 |
|-----|------|------|------|
| cuda:0 | eval-pi05-adaptive-goal-s44 | 模型已加载，正在运行 | **8848 MiB** (PID 13109) |
| cuda:1 | eval-pi05-adaptive-object-s44 | 模型加载中 | 初始化中 |
| cuda:2 | eval-pi05-vla-only-object-s44 | 模型加载中 | 初始化中 |
| cuda:3 | eval-pi05-crm-goal-s42 | 模型加载中 | 初始化中 |
| cuda:4 | eval-pi05-crm-object-s42 | 模型加载中 | 初始化中 |
| cuda:5 | eval-pi05-crm-goal-s43 | 模型加载中 | 初始化中 |

GPU 0 已完成模型加载（safetensors 已载入），其余 5 个正在串行读取模型权重，会陆续加载到各自 GPU 上。所有日志正常，无报错。

---
