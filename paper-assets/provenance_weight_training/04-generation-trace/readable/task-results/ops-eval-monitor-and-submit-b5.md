# ops eval monitor and submit b5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval_monitor_and_submit_b5_20260514T112115_result.json`
- **Structured JSON:** [`f15dcf948a01b91e98ae.json`](../../sessions/f1/f15dcf948a01b91e98ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务完成。结果报告：

## 1. grid_b1_5_seed123 eval 结果

| 指标 | 值 |
|------|-----|
| eval_loss | **2.8736** |
| eval_ppl | **17.70** |
| train_loss | 10.4776 |
| eval_tokens | 4,077,068 |
| eval_time | 107s |

Registry 已更新 metrics + conclusion=success。

## 2. grid_b5_0_seed123 提交状态

- **状态**: 提交成功，RUNNING
- **PID**: 94712
- **GPU**: cuda:3 @ westd-47453
- **日志**: ~/runs/provenance_weight_training/grid_b5_0_seed123.log

（旧 tmux session 已清理，registry 状态已从 DONE(killed) → PREPARING → QUEUED → RUNNING 重置）

---
