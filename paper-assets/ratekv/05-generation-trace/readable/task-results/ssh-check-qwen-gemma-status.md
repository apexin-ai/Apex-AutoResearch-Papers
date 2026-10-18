# ssh check qwen gemma status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_qwen_gemma_status_20260515T215047_result.json`
- **Structured JSON:** [`cf7fa6a907b4fd28181d.json`](../../sessions/cf/cf7fa6a907b4fd28181d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. qwen_3seed_downstream_ci — **已完成** (EXIT_CODE=129, 结果已保存)

PID 369205 已退出。耗时 2714s (~45min)。

| Task | BF16 | Uni4 | MCKP mean | MCKP std | Δ(MCKP−Uni) |
|------|------|------|-----------|----------|-------------|
| arc_challenge | 0.4582 | 0.4590 | **0.4590** | 0.0035 | +0.0000 |
| hellaswag | 0.5887 | 0.5335 | **0.5748** | 0.0022 | **+0.0413** |
| winogrande | 0.7119 | 0.6622 | **0.6780** | 0.0115 | **+0.0158** |
| piqa | 0.7818 | 0.7552 | **0.7748** | 0.0023 | **+0.0196** |

3 seed std 很小 (0.002–0.012)，MCKP 在 hellaswag/winogrande/piqa 上显著优于 uniform。注意 EXIT_CODE=129 (SIGHUP)，但结果已正常写出。

### 2. gemma2_downstream_k8_4task_v2 — **已完成** (EXIT_CODE=0)

PID 369818 已退出。耗时 2321s (~39min)。注意：结果文件名是 `gemma2_downstream_k8_4task_results.json`（无 `_v2` 后缀）。

| Task | Baseline | Uniform | MCKP-k8 | Δ(MCKP−Uni) |
|------|----------|---------|---------|-------------|
| arc_challenge | 0.6135 | 0.6058 | 0.6049 | −0.0009 |
| hellaswag | 0.6093 | 0.6092 | 0.6089 | −0.0003 |
| winogrande | 0.7443 | 0.7380 | **0.7443** | **+0.0063** |
| piqa | 0.8128 | 0.8036 | **0.8079** | **+0.0043** |

Bit 分配: 324×4bit + 8×2bit + 4×8bit。winogrande/piqa 上 MCKP 优于 uniform，arc/hellaswag 基本持平（微弱负差）。

### 3. CodeLlama hires profiling — **仍在运行**

GPU 0 上 PID 362950 占用 16966 MiB。当前进度 **821/1024 (80.2%)**，已跑 177.9min，ETA ~44min。

---
