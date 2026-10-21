# check home full status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-full-status_20260514T110504_result.json`
- **Structured JSON:** [`3924f27490a65196c0fc.json`](../../sessions/39/3924f27490a65196c0fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

---

## GPU 状态

| GPU | 型号 | 显存占用 | 利用率 | 温度 | 功耗 |
|-----|------|---------|--------|------|------|
| cuda:0 | RTX 5090 | 12345 / 32607 MiB | 86% | 81°C | 547W/575W |

进程：`python3 eval_repo_cls.py` (PID 3074797)，正在跑 `checkpoints_repo_cls_home/checkpoint-200` val eval。

---

## Val Sweep 进度

val_sweep 已完成 **10/13** 个 checkpoint（当前第 11 个进行中）：

### 已完成（max_seq_length=2048）

**seed123 系列：**

| Checkpoint | Acc | F1_macro | F1_fail | F1_pass | 完成时间 |
|-----------|-----|---------|---------|---------|---------|
| seed123/ckpt-200 | 62.51% | 55.54 | 37.94 | 73.14 | 23:58 |
| seed123/ckpt-400 | 80.72% | 67.03 | 45.78 | 88.27 | 00:23 |
| seed123/ckpt-600 | 76.78% | 66.81 | 48.63 | 85.00 | 00:49 |
| seed123/ckpt-800 | 81.81% | 69.14 | 49.37 | 88.91 | 01:15 |
| seed123/ckpt-1000 | 82.30% | 67.63 | 45.84 | 89.42 | 01:41 |

**v5-conda 系列：**

| Checkpoint | Acc | F1_macro | F1_fail | F1_pass | 完成时间 |
|-----------|-----|---------|---------|---------|---------|
| v5/ckpt-600 | 77.25% | **70.81** | **57.11** | 84.52 | 02:07 |
| v5/ckpt-4000 | 83.32% | 70.26 | 50.56 | 89.97 | 02:33 |
| v5/ckpt-4200 | 82.82% | 69.54 | 49.43 | 89.65 | 02:58 |
| v5/ckpt-4400 | 83.49% | **71.63** | **53.29** | 89.97 | 03:24 |
| v5/ckpt-4600 | 83.63% | **71.72** | **53.36** | 90.07 | 03:50 |

**checkpoints_repo_cls_home 系列（进行中）：**

| Checkpoint | 状态 |
|-----------|------|
| home/ckpt-200 | **进行中** — 5520/9335 (59%), running_acc=79.2% |
| home/ckpt-2400 | 待跑 |
| home/ckpt-2600 | 待跑 |

---

## ETA 估算

- 每个 checkpoint 约 **26 分钟**（batch_size=8, max_seq_length=2048）
- home/ckpt-200 剩余 ~41%，预计 **04:16** 完成
- home/ckpt-2400 + ckpt-2600：再 ~52 分钟 → val_sweep 全部完成约 **05:08**
- 之后 6144 验证脚本自动启动（seed123 ckpt-400 + ckpt-600，batch_size=4, max_seq_length=6144），预计每个更慢，两个共约 **1-1.5 小时** → 6144 验证全部完成约 **06:10–06:40**

---

## 6144 验证状态

`run_val_6144_verify.sh` 已在后台运行，当前处于 **等待 val_sweep 完成** 的 polling 循环中（每 60s 检查一次）。val_sweep 结束后自动开始 6144 验证。`val_eval_results_6144/` 目录已创建，尚无结果文件。

---
