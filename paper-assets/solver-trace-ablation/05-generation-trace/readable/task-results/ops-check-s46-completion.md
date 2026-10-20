# ops check s46 completion

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-s46-completion_20260517T020855_result.json`
- **Structured JSON:** [`6c46ff27d4483ba6e2ce.json`](../../sessions/6c/6c46ff27d4483ba6e2ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练成功完成 500 步。**

- **最终 checkpoint**: `/root/autodl-tmp/outputs/plan001_exec_only_s46/checkpoint-500/`
- **合并模型也已保存**: 顶层目录有完整的 safetensors 文件（约 16GB，4 shards）
- **最终 step 500 指标**: reward_mean=1.0, prove_rate=1.0, isr_mean=0.366, loss=0.0
- **完成时间**: 2026-05-17 02:07:13 UTC

tmux session 已退出（符合预期，训练完成后自动结束）。无 eval_results.json，eval 需后续单独执行。

---
