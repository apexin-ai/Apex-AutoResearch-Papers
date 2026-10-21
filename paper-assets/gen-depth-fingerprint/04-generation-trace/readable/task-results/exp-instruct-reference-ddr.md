# exp instruct reference ddr

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_instruct_reference_ddr_20260520T230740_result.json`
- **Structured JSON:** [`5eaeae5c18e360eee2da.json`](../../sessions/5e/5eaeae5c18e360eee2da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有产出已生成。结果如下：

## DDR 信号对比：Base-ref (Pythia-410M) vs Instruct-ref (Qwen3-0.6B)

### Qwen3-1.7B-Instruct

| Feature | Base ρ | Inst ρ | Δρ | Base \|d\| | Inst \|d\| | Δ\|d\| |
|---|---|---|---|---|---|---|
| entropy_mean | **0.478** | 0.221 | -0.257 | **1.981** | 1.022 | -0.959 |
| entropy_std | 0.301 | **0.299** | -0.002 | 1.070 | **1.509** | +0.439 |
| entropy_max | 0.187 | -0.135 | -0.322 | 0.514 | 0.079 | -0.435 |
| entropy_min | 0.337 | 0.283 | -0.054 | 0.484 | 0.329 | -0.155 |
| tail_decay | 0.183 | 0.117 | -0.066 | 0.460 | 0.449 | -0.011 |
| ttr | 0.480 | 0.480 | 0.000 | 1.747 | 1.747 | 0.000 |
| hapax_ratio | 0.477 | 0.477 | 0.000 | 1.680 | 1.680 | 0.000 |

### OLMo-2-1B-Instruct

| Feature | Base ρ | Inst ρ | Δρ | Base \|d\| | Inst \|d\| | Δ\|d\| |
|---|---|---|---|---|---|---|
| entropy_mean | **0.482** | -0.113 | -0.595 | **1.330** | 0.017 | -1.312 |
| entropy_std | **0.296** | 0.016 | -0.280 | **0.757** | 0.159 | -0.598 |
| entropy_max | **0.306** | 0.151 | -0.154 | **0.809** | 0.610 | -0.199 |
| entropy_min | 0.080 | -0.034 | -0.114 | 0.170 | 0.141 | -0.029 |
| tail_decay | **0.228** | -0.010 | -0.238 | **0.600** | 0.059 | -0.541 |
| ttr/hapax | ~0 | ~0 | 0 | ~0.13 | ~0.13 | 0 |

### 关键发现

**假设被否定。** 用 instruct reference model (Qwen3-0.6B) 替代 base reference model (Pythia-410M) **不仅没有恢复 DDR 信号，反而大幅削弱了 NLL 特征的区分力**：

1. **Qwen3-1.7B-Instruct**: entropy_mean 的 ρ 从 0.478 降到 0.221，Cohen's d 从 1.98 降到 1.02。唯一例外是 entropy_std 的 d 值略有提升。
2. **OLMo-2-1B-Instruct**: 崩溃更严重——entropy_mean 的 ρ 从 0.482 变成 **-0.113**（符号反转），d 从 1.33 降到接近 0。
3. **Surface features (ttr, hapax_ratio)**: 完全不变（符合预期，与 reference model 无关）。

**解释**：Qwen3-0.6B 的 NLL landscape 对 instruct 文本"太匹配了"——所有 depth 的 instruct 文本对它来说都同等流畅，抹平了 depth 间的 entropy 差异。而 Pythia-410M 作为异族 base model，反而提供了更好的"鉴别性困惑度"。

### 产出文件
1. `/root/gen-depth-fingerprint/scripts/extract_features_instruct_ref.py`
2. `/root/gen-depth-fingerprint/scripts/analyze_instruct_ref_ddr.py`
3. `/root/gen-depth-fingerprint/data/features_instruct_ref_qwen06b.csv` (9392 rows)
4. `/root/gen-depth-fingerprint/results/instruct_ref_ddr_comparison.json`

---
