# check d048 and yi15

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d048_and_yi15_20260514T183057_result.json`
- **Structured JSON:** [`a951dcd3534a339c49cc.json`](../../sessions/a9/a951dcd3534a339c49cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### 1. qwen25-hires-profiling (D048 验证)

**Float32 profiling 已完成。** 另有一个新进程仍在运行。

| 项目 | 状态 |
|------|------|
| PID 246442 | 已结束 |
| PID 247434 | **运行中**（1h36m），`run_hires_quant.py --budget 0.25 --num_samples 64 --seq_len 2048`，GPU 0 占 35GB/98GB，100% 利用率 |

**Float32 验证结果**（来自 `qwen_float32_validate.log`）：

| 指标 | Float32 值 |
|------|-----------|
| **Top-5% concentration** | **0.4220** |
| Top-5 heads distortion sum | 8.2906 |
| Total 2-bit distortion sum | 19.6478 |
| Baseline PPL | 10.7739 |
| MCKP allocation | {8: 4, 2: 8, 4: 100} |
| **与 bf16 allocation 一致性** | **YES - IDENTICAL** |

结论：float32 下 concentration = 0.4220，MCKP 分配方案与 bf16 完全一致，bf16 bug 未导致 allocation 偏移。

**结果文件：**
- `/root/ratekv/qwen_float32_profiles.json` — float32 per-head profile（19KB, May 15 01:54）
- `/root/ratekv/qwen_float32_validate.log` — 验证日志
- `/root/ratekv/qwen_float32_validate.py` — 验证脚本

PID 247434 正在跑的 `run_hires_quant.py` 是 hires calibration 下的 quantization evaluation（输出到 `qwen_hires_results.json`），这是另一个步骤，非 profiling 验证。

---

### 2. Yi-1.5-9B (D047)

**实验已完成，verdict = FAIL。**

| 指标 | 值 |
|------|-----|
| baseline_wikitext2_ppl | 7.016 |
| mckp_wikitext2_ppl | 7.313 |
| uniform_4bit_ppl | 7.217 |
| mckp_improvement_over_uniform | **-0.096**（worse） |
| top5_concentration | 0.4934 |
| best_k (ablation) | max_2bit=2, ppl=7.221 |

**文件路径（用于 registry 更新）：**

| 用途 | 路径 |
|------|------|
| 完整结果 | `/root/ratekv/yi15_full_results.json` |
| K-ablation | `/root/ratekv/yi15_k_ablation_results.json` |
| Profiling 原始数据 | `/root/ratekv/yi15_profiling_results.json` |
| 运行日志 | `/root/ratekv/yi15_full.log`（注：这是早期 crash 的日志，成功运行的输出在结果 JSON 中） |
| Pipeline 脚本 | `/root/ratekv/run_yi15_full_pipeline.py` |

无独立 checkpoint 目录——Yi-1.5 实验是 profiling+evaluation pipeline，未产生模型 checkpoint。

---
