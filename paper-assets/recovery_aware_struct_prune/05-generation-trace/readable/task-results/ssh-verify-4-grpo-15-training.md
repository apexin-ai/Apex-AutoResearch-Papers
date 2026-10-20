# ssh verify 4 grpo 15 training

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_4_grpo_15_training_20260520T205554_result.json`
- **Structured JSON:** [`8507c2696b2ea66c9a4c.json`](../../sessions/85/8507c2696b2ea66c9a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## M023 验证结果

### 4 个训练状态：全部 **running**（初始化阶段）

| 训练 | PID | GPU | 状态 | 日志进度 |
|------|-----|-----|------|---------|
| grpo_cka_only_15_seed123 | 281647 | cuda:0 | running | 加载 ref_model，检测到非均匀 MLP |
| grpo_cka_only_15_seed456 | 281727 | cuda:1 | running | 加载 ref_model，检测到非均匀 MLP |
| grpo_standard_15_seed123 | 281874 | cuda:2 | running | 加载 pruned model |
| grpo_standard_15_seed456 | 282025 | cuda:3 | running | 加载 pruned model |

### GPU 利用率

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 | 13.2 / 95.6 GB | 0% |
| cuda:1 | 13.2 / 95.6 GB | 0% |
| cuda:2 | 13.2 / 95.6 GB | 0% |
| cuda:3 | 2.9 / 95.6 GB | 12% |

cka_only 两组已加载完 ref_model 进入训练准备，standard 两组还在加载模型中。GPU 利用率暂时为 0%（模型加载阶段），GPU 3 刚开始有计算活动。

### 磁盘空间

数据盘 `/root/autodl-tmp/`: 552G / 619G used (90%), **剩余 68GB**。4 个 GRPO checkpoint（每个约 5-7GB）足够存放，但空间偏紧，后续需关注。

---
