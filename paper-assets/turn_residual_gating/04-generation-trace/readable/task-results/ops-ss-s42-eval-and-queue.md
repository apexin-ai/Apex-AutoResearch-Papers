# ops ss s42 eval and queue

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ss_s42_eval_and_queue_20260522T225144_result.json`
- **Structured JSON:** [`7ca503b2e0dd1b34a1ef.json`](../../sessions/7c/7ca503b2e0dd1b34a1ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 成功启动，正在运行：

- **PID**: 48241
- **GPU**: cuda:0，已占用 47873 MiB 显存
- **进度**: TF 1/4 (Base+GAR-ours) 已完成，正在运行 TF 2/4 (Base+GAR-Dongre)
- **Checkpoint**: epoch_2 命中
- **预估完成**: ~1h（TF 4 阶段 ~15min + AR N=50 ~40min + bootstrap ~5min）

Eval 完成后由 cron 回调触发下一步，无需手动启动 queue_runner。

---
