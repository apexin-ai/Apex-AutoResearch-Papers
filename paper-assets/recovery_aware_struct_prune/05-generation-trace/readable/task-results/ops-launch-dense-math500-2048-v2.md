# ops launch dense math500 2048 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch_dense_math500_2048_v2_20260518T214543_result.json`
- **Structured JSON:** [`6320df000b69425c95de.json`](../../sessions/63/6320df000b69425c95de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

grpo_unpruned_v2 是 GRPO 训练后的模型（28 layers = 完整的 Qwen-7B），不是原始 dense 模型。我们需要的是原始预训练权重。

westd-29022 上 Dense 模型不存在。你要求不下载模型，但此服务器上确实没有 DeepSeek-R1-Distill-Qwen-7B 的完整权重（HF cache 只有 refs 目录，缺少 blobs/snapshots）。

**可选方案：**
1. 从 westb-23072 的 `/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B/` 用 `scp`/`rsync` 拷贝到 westd-29022（不算"下载"，是服务器间传输）
2. 改在 westb-23072 上运行（但那台机器的 GPU 可能在忙）
3. 用 westd-29022 上已有的 `grpo_unpruned_v2` 代替（但这是 GRPO 后的 checkpoint，不是原始 Dense）

你想走哪个方案？

---
