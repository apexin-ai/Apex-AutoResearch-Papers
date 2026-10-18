# analysis gemma2 hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemma2_hires_bf16_2bitonly_20260515T005231_result.json`
- **Structured JSON:** [`bad99c9f24c21efd82c2.json`](../../sessions/ba/bad99c9f24c21efd82c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

提取完成。结果如下:

## gemma2_hires_bf16_2bitonly 实验结果

**状态**: 正常完成 (log 末尾显示 "Profiling done in 95.4min" + "Saved: ...json")

### 关键指标
| 指标 | 值 |
|---|---|
| top5_concentration | **0.2291** (16/336 heads) |
| distribution_shape | **Flat** (<0.30, FAIL hires assumption) |
| baseline_calibration_ppl | 7.3200 |
| delta_2bit_mean / std | 0.01204 / 0.01546 |
| delta_2bit_cv | **1.2834** |
| layer0_dominance_ratio | **2.05x** (L0=0.02411, others=0.01175) |
| top1_head | **L0H1, delta=+0.1906** |
| positive_delta_heads / total | 310 / 336 |
| total_hours | **1.59h** (5725.3s) |

### Top-5 sensitive heads
1. L0H1: +0.1906
2. L40H6: +0.0993
3. L29H7: +0.0757
4. L27H6: +0.0692
5. L21H0: +0.0687

### 文件路径
- log: `/root/runs/ratekv/gemma2_hires_bf16_2bitonly.log` ✓
- checkpoint: `/root/ratekv/gemma2_hires_bf16_2bitonly_results.json` (1406 bytes)
- profiles: `/root/ratekv/gemma2_hires_bf16_2bitonly_profiles.json`

### 结论
**Flat 分布,与预期一致** (concentration 0.23 → 0.2291,几乎完全吻合 standard profiling)。Layer 0 仅 2.05× 主导,远低于 Yi/Mistral 等 spike 模型 (>4×)。Gemma-2-9B 属于 hires 假设的 FAIL case。

### GPU 状态
两块 RTX PRO 6000 Blackwell 96GB 均**完全空闲** (0 MiB / 97887 MiB, 0% util)。

---
