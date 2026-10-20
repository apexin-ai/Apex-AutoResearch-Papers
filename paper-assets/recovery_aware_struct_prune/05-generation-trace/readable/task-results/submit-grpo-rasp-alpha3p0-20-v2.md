# submit grpo rasp alpha3p0 20 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_grpo_rasp_alpha3p0_20_v2_20260522T112417_result.json`
- **Structured JSON:** [`51733d72a652628bef5c.json`](../../sessions/51/51733d72a652628bef5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

- **SFT checkpoint**: 存在于 westd-32935，12G，无需复制
- **磁盘**: 15G 可用，够存 GRPO checkpoint
- **训练已提交**: PID=42003，westd-32935:cuda:0，模型正在加载（已检测到非均匀 MLP）
- **Registry**: 已更新为 RUNNING，完整 spec 已填入

注意：任务描述中的 `--num_steps` 不存在，实际参数为 `--max_steps 100`。另外原始实验用的 `--per_device_train_batch_size 1`（非默认 2），已按原始配置完整复现。磁盘较紧（98%），训练完成后建议清理。

---
