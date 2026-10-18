# eval stage1only k09

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_stage1only_k09_20260517T081048_result.json`
- **Structured JSON:** [`b832f8ea58a8db2cb634.json`](../../sessions/b8/b832f8ea58a8db2cb634.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已成功启动并运行在 GPU 1 上。

**状态总结：**
- **tmux session**: `eval_stage1only_k09`
- **GPU 1**: PID 192175, 3048MiB, 正常运行
- **Config**: `libero_acis_stage1only_k09.yaml`，k_ratio=0.9（保留 115/128 tokens，移除约 10%）
- **Checkpoint**: `stage1_done/checkpoint.pt`（与 k=0.5 eval 相同）
- **日志**: `logs/eval_stage1only_k09.log`
- **输出**: `eval_results/eval_stage1only_k09_object.json`
- **早期观察**: Task 0 前 27 episodes 全部 FAIL，steps=280（跑满步数）。即使只移除 10% tokens 也全 FAIL，与 k=0.5 的 0% SR 一致。

预计 ~40 min 完成全部 10 tasks × 50 episodes。从目前趋势看，k=0.9 大概率也是 0% SR，说明 Stage1-only ACIS 的 pruning hook（zeroing masked tokens）本身就破坏了模型——不是移除多少的问题，而是 zeroing 机制本身的问题。

---
