# ops westb cleanup and sft restart

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cleanup_and_sft_restart_20260520T091521_result.json`
- **Structured JSON:** [`81f3fdbf94bfea097691.json`](../../sessions/81/81f3fdbf94bfea097691.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 SFT 都已成功启动，模型正在加载（检测到非均匀 MLP 结构，说明 pruned model config 正确读取）。

**执行摘要：**

| 步骤 | 结果 |
|------|------|
| 磁盘清理 | 删除 2× optimizer.pt + 损坏 checkpoint-1870，释放 ~32GB → 33GB 可用 (87%) |
| checkpoint-935 验证 | CKA-only ✓ (339 tensors), Standard ✓ (339 tensors) |
| SFT 提交 | `sft_qwen_math_cka_only_20_v2` on cuda:0 (PID 9952), `sft_qwen_math_standard_20_v2` on cuda:1 (PID 10030) |
| Registry | 两个 v2 条目已创建，parent 指向原始失败实验 |

两个任务从 checkpoint-935（epoch 1 权重）续跑 1 epoch，`--save_strategy no` 防止中间 checkpoint 写满磁盘。预计 ~30 分钟完成。

---
