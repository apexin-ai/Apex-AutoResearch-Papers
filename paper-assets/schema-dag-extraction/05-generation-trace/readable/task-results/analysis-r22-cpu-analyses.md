# analysis r22 cpu analyses

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r22_cpu_analyses_20260519T181910_result.json`
- **Structured JSON:** [`d0d8c5ef398da822b220.json`](../../sessions/d0/d0d8c5ef398da822b220.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个分析全部完成，结果已保存。

### A1: FP8 噪声传播保守 CI
- 数据：`bcs_controlled_llama-3.1-70b-fp8` count_8 (10 batches) × count_16 (10 batches)
- 原始 interaction: **15.10 pp**
- 噪声传播 95% CI (B=10000, σ=0.88pp): **[0.15, 31.63] pp**
- CI 不含 0 → 即使考虑 FP8 量化噪声，interaction 仍然显著
- 保存: `analysis/fp8_noise_propagated_ci.json`

### A2: DocRED Range-Matched Post-Hoc Power
- Range-matched 后: n_16=29, n_32=55, observed interaction=0.93 pp
- 检测 ±5pp interaction 的 power: **0.2647** (严重不足)
- 80% power 对应 MDE: **10.54 pp**
- Power table: 3pp→0.13, 5pp→0.26, 8pp→0.57, 10pp→0.76, 15pp→0.98
- 保存: `analysis/docred_range_matched_power.json`

### A3: Fisher z-test
- Constrained ρ=-0.919 (n=25), Unconstrained ρ=-0.139 (n=25)
- Fisher z = **-4.78**, p = **2×10⁻⁶**
- 两组相关性差异高度显著 → constrained decoding 下 BCS 预测力远强于 unconstrained
- 保存: `analysis/fisher_z_constrained_vs_unconstrained.json`

---
