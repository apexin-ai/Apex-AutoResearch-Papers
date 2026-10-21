# ops d108 k03 check and westd27271 fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d108-k03-check-and-westd27271-fill_20260520T181234_result.json`
- **Structured JSON:** [`ffe498f4d5f92c79502f.json`](../../sessions/ff/ffe498f4d5f92c79502f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认运行。

## 汇总

### 任务 1: westd-38929 D108 L2 norm 状态

| k 值 | 状态 | 成功率 | 结果文件时间 |
|------|------|--------|-------------|
| k=0.3 | **已完成** | 25.0% (125/500) | 05-21 02:04 |
| k=0.5 | **已完成** | — | 05-21 01:35 |
| k=0.9 | **已完成** | — | 05-21 01:20 |
| k=0.95 | **已完成** | — | 05-21 01:28 |

所有 4 个进程均已退出，结果文件齐全。

### 任务 2: westd-27271:0 启动实验

走**情况 B**（k=0.3 已完成），启动了 **OpenVLA L2 norm k=0.7 seed43**：
- **PID**: 67609（python 子进程）
- **GPU**: GPU:0 (`A8:00.0`)，占用 15997 MiB
- **日志**: `logs/eval_openvla_l2norm_k07_seed43.log`
- **输出**: `eval_results/openvla_l2norm_prune_k0_7_seed43_object.json`
- 已在跑第 1/10 个 task（pick up the alphabet soup）

GPU:1 上的 smart compress 训练（PID 921279，已运行 7.5h）不受影响。

---
