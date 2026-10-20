# diag c2 qw n500

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_c2_qw_n500_20260514T135459_result.json`
- **Structured JSON:** [`d905fc53415a22c8bfad.json`](../../sessions/d9/d905fc53415a22c8bfad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**实验 c2_qw_n500 状态：RUNNING（未退出）**

初始报告不准确——4 个 Qwen python 进程活跃，日志持续更新，当前进度 ~8/500。

### 严重问题：重复进程

每个 GPU 上跑了 **2 个相同进程**，写入同一输出目录：

| GPU | 原始 PID (tmux) | 重复 PID | 写入目录 |
|-----|----------------|---------|---------|
| GPU 2 | 131864 | **132389** | `profiling_output_n500_bf16_qw_imp_s015` |
| GPU 3 | 132002 | **132392** | `profiling_output_n500_bf16_qw_rand_s015` |

日志已出现时间戳交错（两个进程同时写 tee），输出文件存在并发覆盖风险。

### 需要立即操作

**杀掉重复进程**（PID 132389, 132392），保留 tmux session 中的原始进程。然后检查输出目录是否已有损坏文件——如有，需清空后重启 s015 条件。

是否现在杀掉重复进程？

---
