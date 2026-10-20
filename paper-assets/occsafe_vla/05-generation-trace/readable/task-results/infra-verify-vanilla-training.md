# infra verify vanilla training

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_verify-vanilla-training_20260520T074604_result.json`
- **Structured JSON:** [`7be529e964a25fcbc133.json`](../../sessions/7b/7be529e964a25fcbc133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

| 进程 | GPU | PID | 显存占用 | 状态 | 当前进度 |
|------|-----|-----|----------|------|----------|
| mvp_vanilla_s0 | cuda:0 | 57072 | 15,824 MiB | **初始化中** | 模型已加载，正在准备数据集 |
| mvp_vanilla_s1 | cuda:1 | 57227 | 12,016 MiB | **初始化中** | 模型已加载，checkpoint shards 100% |
| mvp_vanilla_s2 | cuda:2 | 56580 | 62,184 MiB | **训练中** | step 18/50005, ~1.1-2.9 s/it |

3 个进程全部存活，GPU 3 空闲。s2 已进入迭代，s0 和 s1 还在初始化阶段（加载数据集/构建 dataloader），预计几分钟内也会开始迭代。无异常。

---
