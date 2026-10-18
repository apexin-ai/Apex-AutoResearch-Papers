# audit scatter concentration values

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_scatter_concentration_values_20260514T215607_result.json`
- **Structured JSON:** [`29f3128eadc28b93220b.json`](../../sessions/29/29f3128eadc28b93220b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完成。以下是校验报告：

---

## Scatter 图 Concentration 值校验报告

**脚本位置**: `/root/ratekv/figures/gen_scatter_concentration.py`

### 对比表

| Model | 脚本中的值 | Hires ground truth | Lowres ground truth | 判定 |
|-------|-----------|-------------------|--------------------|----|
| **Llama-3.1-8B** | 0.339 | **0.5749** | 0.3442 | ⚠️⚠️ **用了 lowres**（0.339 ≈ lowres 0.344） |
| **Yi-1.5-9B** | 0.495 | **0.7139** | 0.5033 | ⚠️⚠️ **用了 lowres**（0.495 ≈ lowres 0.503） |
| **Qwen2.5-7B** | 0.569 | **0.6156** | 0.4517 | ⚠️ **偏差**（更接近 hires 但差 0.047，应为 0.6156） |
| **Mistral-7B-v0.3** | 0.220 | **0.2307** | 0.4220 | ✅ 基本匹配 hires（差 0.011） |
| **Gemma-2-9B** | 0.223 | **N/A** | 0.2382 | ⚠️ **无 hires profiling**（当前用的是 lowres 值） |

### Hires 数据来源

| Model | Hires 结果文件 | Calibration | Config |
|-------|---------------|-------------|--------|
| Yi-1.5-9B | `yi15_hires_bf16_2bitonly_results.json` | calibration_hires.json | 64seq × 2048tok, bf16 |
| Llama-3.1-8B | `llama_hires_bf16_2bitonly_results.json` | calibration_hires.json | 64seq × 2048tok, bf16 |
| Qwen2.5-7B | `qwen_hires_f32_constrained_results.json` | hires | float32 |
| Mistral-7B-v0.3 | `mistral_ppl_profiles_hires.json`（计算得出） | hires | 64seq × 2048tok |
| Gemma-2-9B | **不存在** | calibration_data.json (lowres) | 16seq × 512tok |

### 问题汇总

1. **Llama、Yi 是严重错误** — 用了 lowres concentration，与 hires 值差距 >0.2
2. **Qwen 需要修正** — 0.569 → 0.6156
3. **Gemma-2 缺少 hires profiling** — 需要新跑一次 hires profiling 才能得到真实值（lowres=0.238，hires 可能相近也可能不同）
4. **Mistral 近似正确** — 0.220 vs 0.231，如需精确可更新

### 建议修正值（脚本中的 data 数组）

```python
data = [
    ('Gemma-2-9B',      0.238,  ..., '#009E73'),   # lowres, pending hires profiling
    ('Mistral-7B-v0.3', 0.231,  ..., '#CC79A7'),   # hires ✓
    ('Llama-3.1-8B',    0.575,  ..., '#0072B2'),   # hires ✓ (was 0.339 lowres)
    ('Yi-1.5-9B',       0.714,  ..., '#E69F00'),   # hires ✓ (was 0.495 lowres)
    ('Qwen2.5-7B',      0.616,  ..., '#D55E00'),   # hires ✓ (was 0.569)
]
```

---
