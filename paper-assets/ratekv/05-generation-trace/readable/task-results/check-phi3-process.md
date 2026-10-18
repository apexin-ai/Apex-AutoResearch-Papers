# check phi3 process

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_phi3_process_20260516T023637_result.json`
- **Structured JSON:** [`6d10c065f96e07dfdcff.json`](../../sessions/6d/6d10c065f96e07dfdcff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. phi3_medium_constrained_mckp — 已完成

- **进程**: 无运行中进程，已正常结束
- **耗时**: 4.3 min
- **结果**:

| Method | PPL | Delta vs bf16 |
|---|---|---|
| Baseline (bf16) | 5.6359 | — |
| Constrained MCKP (k=8) | 5.8149 | +0.1790 |
| Uniform 4-bit | 5.7987 | +0.1629 |
| Unconstrained MCKP | 6.0730 | +0.4371 |
| Greedy | 6.0730 | +0.4371 |

- Top-5% concentration: 0.1742
- 结果已保存到 `artifacts/phi3_medium_constrained_results.json`

### 2. internlm2_hires_profiling — 运行中

- **PID**: 389863（父 shell PID 389862）
- **GPU**: GPU 0, 18841MiB / 97887MiB, 97% 利用率
- **进度**: 197/256 heads profiled（77%），已运行 44.6 min，ETA ~13 min
- **当前**: Layer 24, Head 4, 2-bit profiling

### 3. GPU 状况

| GPU | 型号 | 显存占用 | 利用率 |
|---|---|---|---|
| 0 | RTX PRO 6000 Blackwell | 18841 / 97887 MiB | 97% |
| 1 | RTX PRO 6000 Blackwell | 3 / 97887 MiB | 0% (空闲) |

### 4. tmux session

- `yi15_9b_full_pipeline` — 1 window（创建于 May 15），无活跃 python 进程

---
