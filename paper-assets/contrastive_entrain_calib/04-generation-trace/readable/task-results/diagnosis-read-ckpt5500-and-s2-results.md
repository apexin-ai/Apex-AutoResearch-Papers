# diagnosis read ckpt5500 and s2 results

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnosis_read-ckpt5500-and-s2-results_20260520T174143_result.json`
- **Structured JSON:** [`fddaa8369fd29aa7e8f1.json`](../../sessions/fd/fddaa8369fd29aa7e8f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### exp-003 ckpt-5500（已完成）

| 指标 | 值 |
|------|-----|
| **ToF** | 0.0608 |
| **NoF** | 0.9724 |
| **SYCONScore** | 0.1144 |
| n_valid / n_invalid / n_total | 181 / 181 / 362 |

结果文件位于 `/root/contrastive_entrain_calib/results/exp003_d027_eval/exp003-ckpt5500_preset_eval.json`。unified 目录下无此文件。

### exp-003-s2 eval（仍在运行）

三个 checkpoint 的 eval **都在跑**，各自进度均为 **140/362**（~38.7%），最后日志时间约 01:39-01:40（约 35 分钟前启动 eval 部分）。

| Job | GPU | 进度 | 状态 |
|-----|-----|------|------|
| exp-003-s2 ckpt-500 | GPU 1 | 140/362 | 运行中 |
| exp-003-s2 ckpt-1000 | GPU 2 | 140/362 | 运行中 |
| exp-003-s2 ckpt-1500 | GPU 3 | 140/362 | 运行中 |

### GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 0% | 2 MiB / 32607 MiB（空闲） |
| 1 | 46% | 16884 MiB / 32607 MiB |
| 2 | 48% | 16884 MiB / 32607 MiB |
| 3 | 50% | 16884 MiB / 32607 MiB |

按当前速率（~30 min 跑 140 条），每个 s2 eval 还需约 **45-50 分钟**完成。

---
