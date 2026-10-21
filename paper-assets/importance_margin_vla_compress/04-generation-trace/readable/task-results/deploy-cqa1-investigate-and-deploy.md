# deploy cqa1 investigate and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_investigate_and_deploy_20260526T195956_result.json`
- **Structured JSON:** [`b01f6e1b1c0dda1a48d4.json`](../../sessions/b0/b01f6e1b1c0dda1a48d4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

### Part 1: Phantom 实验调查结果

| 实验 | PID | GPU | 状态 | 当前进度 | Registry |
|------|-----|-----|------|---------|----------|
| eval_pi05_l2norm_k07_long_seed42 | 617566 | cuda:0 | 运行中, Task 3/10, 总SR 78.0% | T3 ep=30: 40% | DEPLOYED (原有 DONE 条目→状态机限制卡在 DEPLOYED, spec 已更新为 cqa1-33015 信息) |
| eval_pi05_attention_k07_long_seed42_v2 | 617728 | cuda:1 | 运行中, Task 3/10, 总SR 66.7% | T3 ep=20: 40% | RUNNING ✓ |

### Part 2: cuda:2 部署 — 不可行

**cuda:2 被占用**（PID 582964: attention k=0.5 long seed42, 10636MiB）。cuda:3 也被占用（PID 546287: attention k=0.95 long seed42, 10234MiB）。cqa1-33015 四卡全满，无法部署 eval_pi05_random_k07_long_seed42。

### 问题
1. `eval_pi05_l2norm_k07_long_seed42` 因原条目状态为 DONE，经 DEPLOYING→DEPLOYED 路径后被状态机锁死在 DEPLOYED（无出口）。spec/hypothesis 已更新到位，但 status 不是 RUNNING。需要手动修 registry 或用新 ID (如 `_v2`)。
2. 新实验需要等 GPU 释放。4 个 GPU 上的实验预计还需数小时完成。

---
