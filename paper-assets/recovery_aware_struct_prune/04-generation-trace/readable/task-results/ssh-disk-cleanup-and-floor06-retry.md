# ssh disk cleanup and floor06 retry

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_disk_cleanup_and_floor06_retry_20260523T120835_result.json`
- **Structured JSON:** [`5d62e0b7f30232c8d781.json`](../../sessions/5d/5d62e0b7f30232c8d781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pipeline 正在运行，正确跳过了 Pruning 和 SFT，直接开始 GRPO 训练（Step 3/4）。模型正在加载中，GPU 0 还未完全占用，等模型上 GPU 后会显示显存。

### 报告

1. **磁盘清理**：释放 ~168G（100% → 75%，169G 可用）
   - 删除 `grpo_cka_only_20_floor_0.6` 整个目录（36G，含崩溃的 GRPO 产物）
   - 删除 6 个 GRPO `checkpoint-100` 目录（floor 0.5/0.3、seed456、random_20、rasp_20_seed456、rasp_alpha3p0_20_v2，共 ~100G）
   - 删除 3 个 SFT `checkpoint-1870` 目录（floor 0.6/0.5、standard_25，共 ~35G）

2. **floor=0.6 v2 已成功提交**：`exp_id=floor_ablation_0p6_cka_only_20_v2`，westd-32935 cuda:0，Pruning/SFT 已 SKIP，GRPO 正在加载模型

3. **当前磁盘**：482G/650G（75%），169G 可用，GRPO + eval 所需空间充足

---
