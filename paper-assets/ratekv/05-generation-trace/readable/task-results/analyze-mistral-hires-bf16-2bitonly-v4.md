# analyze mistral hires bf16 2bitonly v4

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456_result.json`
- **Structured JSON:** [`da00b85cdf854af77b4a.json`](../../sessions/da/da00b85cdf854af77b4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE / success。

## mistral_hires_bf16_2bitonly_v4 结果总结

**实验完成** — Mistral-7B-v0.3 hires bf16 2-bit profiling（v4，前3次因模型文件损坏失败）

### 核心指标
| 指标 | 数值 |
|------|------|
| **top5_concentration** | **0.241** (12 / 256 heads) |
| baseline_ppl | 5.8702 |
| top1_head | **L2H5** (delta=0.3236) |
| top2_head | L12H1 (delta=0.1435) |
| top3_head | L0H7 (delta=0.1403) |
| delta_2bit_cv | 1.3091 |
| L0 dominance ratio | 1.74x (weak) |
| positive_delta_heads | 252 / 256 (98.4%) |
| total_hours | 0.94h (56.2min profiling) |

### 关键发现
- **Distribution shape: FLAT** (concentration 0.241 < 0.30 阈值)
- Mistral 在 hires 下 concentration (0.241) 与 standard profiling (0.22) 几乎一致 → **确认为 genuine flat / low-heterogeneity 模型**
- 虽然 L2H5 是单一最大 head (delta=0.324)，但其只占总 delta 的约 6% — 不足以构成 "spike" 模式
- 98.4% heads 有正 delta，扩散性极高（CV=1.31 同时也较低）
- L0 dominance 仅 1.74x，远弱于 spike 类模型

### 5 模型 hires concentration 全景图
- Qwen2.5-7B: 0.61 (spike)
- Llama-3.1-8B: 0.51 (moderate-spike)
- Yi-1.5-9B: 0.27 (flat)
- **Mistral-7B-v0.3: 0.24 (flat) ← 本次**
- Gemma-2: pending

### 产物
- log: `/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log`
- profiles JSON: `/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json`
- results JSON: `/root/ratekv/mistral_hires_bf16_2bitonly_results.json`

---
