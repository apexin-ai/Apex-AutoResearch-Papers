# ops check training v4

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-v4_20260514T221633_result.json`
- **Structured JSON:** [`5eb54ce6f9e00794bbbd.json`](../../sessions/5e/5eb54ce6f9e00794bbbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇报

### 1. no_trace_seed42_v4

| 项目 | 状态 |
|------|------|
| 进程 | **running** (PID 835084, 已运行 4m16s) |
| 进度 | step 86/444 (~19%), ~2.7s/step |
| 预计剩余 | ~16-17 分钟 |
| GPU 0 | 100% 利用率, 75619 MiB / 97887 MiB |
| Checkpoint | `/no_trace/final/` 存在（来自之前的 run，May 15 02:22），当前 run 尚未生成 final checkpoint |

### 2. vota_seed42_v4

| 项目 | 状态 |
|------|------|
| 进程 | **crashed** (PID 835161 已退出, EXIT_CODE=1) |
| 失败原因 | `torch.OutOfMemoryError` — step 0 即崩溃，尝试分配 4.64 GiB 时 GPU 仅剩 3.64 GiB 可用 |
| GPU 1 | 当前 0% 利用率, 0 MiB（已释放） |
| Checkpoint | `/vota/final/` 存在（来自之前的 run，May 15 04:18），包含 eval_results.json |

**之前 vota run 的 eval 指标**（来自 final/eval_results.json）：

| 指标 | 值 |
|------|-----|
| Accuracy | 99.16% (CI: 98.57–99.66%) |
| Pass F1 | 99.41% |
| Fail F1 | 98.55% |
| Lift over majority | +27.6% |
| N | 1190 |

### 关键问题

vota_v4 的 OOM 错误显示崩溃时 GPU 上有另一个进程（PID 835089，占用 23.58 GiB）。可能两个进程都被分配到了 GPU 0，导致显存不足。需要确认 vota 的 `CUDA_VISIBLE_DEVICES` 是否正确设为 1。

---
