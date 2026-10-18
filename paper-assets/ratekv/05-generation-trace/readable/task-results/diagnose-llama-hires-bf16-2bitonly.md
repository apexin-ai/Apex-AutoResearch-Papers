# diagnose llama hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama_hires_bf16_2bitonly_20260514T214449_result.json`
- **Structured JSON:** [`564a677f0ce5432fac3f.json`](../../sessions/56/564a677f0ce5432fac3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态：已完成

`llama_hires_bf16_2bitonly` 实验正常完成，总耗时 59.0 分钟。进程已退出，tmux session 不再存在。

### 关键结果

| 指标 | 值 |
|------|-----|
| **模型** | Llama-3.1-8B (bfloat16) |
| **Baseline PPL** | 6.5055 |
| **Top-5% concentration** | **0.5749** (12 heads) |
| **L0 dominance ratio** | 0.67x |
| **Delta(2bit) mean** | 0.12251 |
| **Delta(2bit) CV** | 7.7663 |
| **Positive delta heads** | 254/256 |

### Top-5 最敏感 heads

| Head | delta(2bit) |
|------|-------------|
| **L2H5** | **15.2636** (极端 outlier) |
| L3H1 | 0.4387 |
| L0H0 | 0.3263 |
| L3H2 | 0.2631 |
| L3H6 | 0.2585 |

### 观察

- L2H5 的 delta 极端高（15.26），远超第二名（0.44），说明该 head 对 2-bit 量化极度敏感。
- Top-5% concentration = 0.5749，表明约 57.5% 的总 sensitivity 集中在前 12 个 heads 中，concentration 较高。
- L0 dominance ratio 仅 0.67x，说明第 0 层平均 delta 反而低于其他层，sensitivity 不集中在初始层。

当前服务器上 `mistral_hires_bf16_2bitonly_v4` 正在运行中（GPU 1）。

---
