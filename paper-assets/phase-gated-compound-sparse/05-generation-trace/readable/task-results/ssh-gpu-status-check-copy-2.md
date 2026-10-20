# ssh gpu status check

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpu_status_check_20260515T212743_result.json`
- **Structured JSON:** [`0ce8dce0847493c32399.json`](../../sessions/0c/0ce8dce0847493c32399.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 使用情况

| GPU | 型号 | 显存占用 | 利用率 | 进程 |
|-----|------|---------|--------|------|
| 0 | RTX PRO 6000 Black (96GB) | 15,553 / 97,887 MiB | 81% | PID 277995 — `acc_ds_dense_8k` |
| 1 | RTX PRO 6000 Black (96GB) | 15,427 / 97,887 MiB | 70% | PID 278395 — `acc_ds_s015_8k` |
| 2 | RTX PRO 6000 Black (96GB) | 0 MiB | 0% | 空闲 |
| 3 | RTX PRO 6000 Black (96GB) | 0 MiB | 0% | 空闲 |

### QW n100 进度

**没有名为 `acc_qw_s020_n100` / `acc_qw_s025_n100` 的日志或进程。** 实际存在的是两批各 50 题的结果：

| 条件 | 第一批 (1-50) | 第二批 (51-100) | 合计 n=100 |
|------|-------------|----------------|-----------|
| QW importance_s020 | 24.0% (12/50) ✅完成 | 44.0% (22/50) ✅完成 | **34.0% (34/100)** |
| QW importance_s025 | 26.0% (13/50) ✅完成 | 34.0% (17/50) ✅完成 | **30.0% (30/100)** |

两个 QW n100 评测都已全部完成，无正在运行的进程。

### DS 8k 进程

两个 DS 8k 评测刚启动约 2 分钟，都在 **Problem 2/50**：

| 任务 | GPU | PID | 状态 | 进度 | 预计总时长 |
|------|-----|-----|------|------|-----------|
| `acc_ds_dense_8k` (dense) | 0 | 277995 | 运行中 | 2/50 | ~20s/题 × 50 ≈ 17min（简单题），但 8k token 长输出的题会更久 |
| `acc_ds_s015_8k` (importance_s015) | 1 | 278395 | 运行中 | 2/50 | 类似 |

两个 DS 8k 都跑 `DeepSeek-R1-Distill-Qwen-7B`，`--num-problems 50 --max-new-tokens 8192`。GPU 2、3 空闲可用。

---
