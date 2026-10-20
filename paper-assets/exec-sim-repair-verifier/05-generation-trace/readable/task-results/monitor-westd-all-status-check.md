# monitor westd all status check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd-all-status-check_20260515T014517_result.json`
- **Structured JSON:** [`4219ebf438998b5429c9.json`](../../sessions/42/4219ebf438998b5429c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总结

| GPU | 进程 | 进度 | 预计剩余 |
|-----|------|------|---------|
| **cuda:0** | `cls8b-s42-ckpt1000-test8192-eval` (PID 312981) | 2700/9784 (27.6%), running_acc=**82.7%** | **~15 min** (~10:01 UTC 完成) |
| **cuda:1** | CLS 8B s42 resume 训练 (PID 295794) | step 1797/6633 (27.1%), epoch 0.79/3 | ~10.9h |
| **cuda:2** | CWM 8B v4 训练 (PID 266816) | step 2815/6633 (42.4%), epoch 0.72/3 | ~8.5h |
| **cuda:3** | CLS 8B seed123 v3 训练 (PID 266449) | step 5351/6633 (80.7%), epoch 2.42/3 | **~3.0h** |

### ckpt-1000 test eval 关键信息
- **状态**: 正在运行，未完成
- **running_acc**: 82.7%（test set 通常低于 val 的 88.23%，这很正常）
- **命令确认**: 含 `--max_new_tokens 512 --max_seq_length 8192` ✓
- **日志**: `~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1000-test8192-eval.log`
- **预计完成**: ~10:01 UTC（约 15 分钟后）

### 训练 loss 概览
- CLS 8B s42: loss=0.998 @step1750, eval_loss=0.276 @step1600（仍在 epoch 1 初期）
- CWM 8B: eval_loss=0.276 @step1600 
- CLS 8B seed123: loss=0.220 @step5350, eval_loss=0.390 @step5200（接近收敛，epoch 2.4）

Registry 已全部更新。eval 结果需等 ~15min 后再次检查提取最终指标。

---
