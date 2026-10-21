# ops westb disk cleanup and launch eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_disk_cleanup_and_launch_eval_20260519T044409_result.json`
- **Structured JSON:** [`cc982d29dd18afc34fb7.json`](../../sessions/cc/cc982d29dd18afc34fb7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**汇总：**
- 清理了 `optimizer.pt` (9.5G) + `training_args.bin`，数据盘从 100% 降至 97% (9.5G 可用)
- GSM8K eval 已在 westb-23072 cuda:0 上运行 (PID 865250)，~11s/样本，预计约 4 小时完成
- Registry 条目 `eval_gsm8k_grpo_unstructured_20` 已创建，状态 RUNNING，parent=grpo_unstructured_20
- GPU 1 上还有一个之前的 eval_unstructured_20 在运行（PID 857962, 67.9G 显存, 100% 利用率）

---
