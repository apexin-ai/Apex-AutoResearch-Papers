# ops recompute llama d values

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_recompute-llama-d-values_20260523T150337_result.json`
- **Structured JSON:** [`23d62ecac0eaf3fe13f8.json`](../../sessions/23/23d62ecac0eaf3fe13f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

### 表格 1: 每个实验的新旧 d 值对比

| exp_id | contam% | seed | lz* | 旧 d | 新 d | Δd |
|--------|---------|------|------|------|------|------|
| exp-llama-5pct-s1 | 5% | 42 | -4.695 | -5.218 | **-3.215** | +2.003 |
| exp-llama-5pct-s2 | 5% | 123 | -4.460 | -4.938 | **-3.063** | +1.876 |
| exp-llama-5pct-s3 | 5% | 456 | — | — | — | ANALYZING |
| exp-llama-15pct-s2 | 15% | 123 | -4.680 | -5.200 | **-3.205** | +1.995 |
| exp-llama-15pct-s3 | 15% | 456 | -4.507 | -4.994 | **-3.093** | +1.901 |
| exp-llama-25pct-s1 | 25% | 42 | -4.616 | -5.124 | **-3.164** | +1.960 |
| exp-llama-25pct-s2 | 25% | 123 | -3.249 | -3.496 | **-2.277** | +1.219 |
| exp-llama-25pct-s3 | 25% | 456 | — | — | — | ANALYZING |
| exp-llama-50pct-s2 | 50% | 123 | -3.735 | -4.075 | **-2.592** | +1.483 |
| exp-llama-50pct-s3 | 50% | 456 | -2.810 | -2.973 | **-1.992** | +0.981 |

### 表格 2: Multi-seed 汇总

| contam% | seeds | mean(d) | SD(d) | n |
|---------|-------|---------|-------|---|
| 5% | s1,s2 (s3 analyzing) | -3.139 | 0.108 | 2 |
| 15% | s2,s3 (s1 pilot training) | -3.149 | 0.079 | 2 |
| 25% | s1,s2 (s3 analyzing) | -2.720 | 0.627 | 2 |
| 50% | s2,s3 (s1 pilot training) | -2.292 | 0.424 | 2 |

### 关键变化

- 新 baseline SD (1.5418) 是旧 SD (0.840) 的 **1.84x**，所以所有新 d 的绝对值约为旧值的 **55%**
- 新 baseline mean 从 -0.312 右移到 +0.262，分子也变大
- 所有 Δd 均为正值（+0.98 ~ +2.00），即新 d 绝对值一致缩小
- 所有新 d 仍为大效应量（|d| > 1.99），检测力充足
- 缺失数据：exp-llama-5pct-s3 和 exp-llama-25pct-s3 仍在 ANALYZING；15pct-s1 和 50pct-s1 正在 pilot 训练

---
