# check home cuda0 status urgent

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-cuda0-status-urgent_20260514T103736_result.json`
- **Structured JSON:** [`303ff69613351b0c7166.json`](../../sessions/30/303ff69613351b0c7166.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 0
- **利用率 100%**，显存 12345/32607 MiB，进程 PID 3072378 (python3)
- 正在跑 val_sweep

### 2048 Sweep：进行中（10/13 checkpoints started，9/13 完成）

当前正在评估 `v5/checkpoint-4600`，进度 4800/9335 (~51%)。

已完成 9 个 checkpoint 的结果：

| Checkpoint | Acc | F1 Macro | F1 Fail | Prec Fail | Recall Fail |
|---|---|---|---|---|---|
| **seed123/ckpt-200** | 62.51 | 55.54 | 37.94 | 31.58 | 47.51 |
| **seed123/ckpt-400** | 80.72 | 67.03 | 45.78 | 71.16 | 33.75 |
| **seed123/ckpt-600** | 76.78 | 66.81 | 48.63 | 52.13 | 45.56 |
| **seed123/ckpt-800** | 81.81 | 69.14 | 49.37 | 75.14 | 36.77 |
| **seed123/ckpt-1000** | 82.30 | 67.63 | 45.84 | 87.59 | 31.04 |
| **v5/ckpt-600** | 77.25 | **70.81** | **57.11** | 52.37 | **62.79** |
| **v5/ckpt-4000** | 83.32 | 70.26 | 50.56 | 88.74 | 35.35 |
| **v5/ckpt-4200** | 82.82 | 69.54 | 49.43 | 85.22 | 34.81 |
| **v5/ckpt-4400** | **83.49** | **71.63** | **53.29** | 83.95 | 39.03 |

Majority baseline accuracy = 75.88%。

### 6144 验证：等待中

`val_6144` tmux session 存活，run.log 显示已轮询 90+ 次（每分钟一次），持续输出 "val_sweep still running, waiting 60s..."。目录下只有 run.log，无结果文件。

### 预估时间

每个 checkpoint 约 25 分钟。当前 v5/ckpt-4600 剩余 ~14 min，之后还有 3 个 checkpoint ≈ 75 min。**2048 sweep 预计 ~05:10 PDT 完成**，之后 6144 自动启动。

### 关键发现

- **最高 F1 Macro**: v5/ckpt-4400 (71.63)，其次 v5/ckpt-600 (70.81)
- **最高 Accuracy**: v5/ckpt-4400 (83.49)
- **最高 Recall Fail**: v5/ckpt-600 (62.79) — 但代价是 accuracy 仅 77.25
- v5 系列整体优于 seed123 系列（F1 Macro 更高）
- 所有模型都存在 fail 类别 recall 低的问题（倾向预测 pass）

---
