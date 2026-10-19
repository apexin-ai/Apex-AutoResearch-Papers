# code acib v5 div reg seed2

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_acib_v5_div_reg_seed2_20260516T025315_result.json`
- **Structured JSON:** [`12fa45aa653bfa6aef55.json`](../../sessions/12/12fa45aa653bfa6aef55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**acib_v5_div_reg_seed2 已在运行中**（PID 728887，10:54 启动，当前 step 200/20000）。

参数：seed=1337, CUDA_VISIBLE_DEVICES=1, diversity_lambda=0.1，其他参数与 seed 1 一致。

**注意一个差异**：seed 2 的日志显示 `ent=0.0210`（lambda_ent=0.1 生效），而 seed 1 的日志没有 ent 字段——说明 seed 1 运行时脚本可能还没有 `lambda_ent` 参数，或者 seed 1 用了 `--lambda_ent 0`。如果要严格复现 seed 1 的条件，这个差异需要确认。当前 seed 2 的 scorer_std=0.123（step 200），远低于 seed 1 同期的 0.297，entropy regularizer 可能是原因。

需要我：
1. 保持现状继续跑？
2. 还是 kill 掉、加 `--lambda_ent 0` 重启以严格对齐 seed 1？

---
