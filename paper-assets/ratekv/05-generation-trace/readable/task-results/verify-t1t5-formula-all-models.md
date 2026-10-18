# verify t1t5 formula all models

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_t1t5_formula_all_models_20260515T144250_result.json`
- **Structured JSON:** [`2096c6248aaaeb28123a.json`](../../sessions/20/2096c6248aaaeb28123a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部收集。汇总如下：

## 公式验证

`compute_shape_metrics.py` 中的公式：
```python
t1_t5 = s[0] / top5_sum   # = top1_delta / top5_sum
```
**是 canonical formula** ✅（等价于 top1_conc / top5_conc，因为 total_sum 约掉了）

## 每个模型的数据源和正确性

| Model | 当前数据源 | 类型 | 当前 t1/t5 | 正确 hires 文件 | hires t1/t5 | 状态 |
|-------|-----------|------|-----------|----------------|-------------|------|
| Qwen2.5-7B | `hires_profiles.json` | hires flat | 0.5670 | (同) | 0.5670 | ✅ |
| Qwen2.5-14B | `qwen14b_hires_bf16_2bitonly_profiles.json` | hires flat | 0.5693 | (同) | 0.5693 | ✅ |
| Llama-3.1-8B | `llama_hires_bf16_2bitonly_profiles.json` | hires flat | 0.8466 | (同) | 0.8466 | ✅ |
| Yi-1.5-9B | `yi15_hires_bf16_2bitonly_profiles.json` | hires flat | 0.9012 | (同) | 0.9012 | ✅ |
| Pythia-1.4B | `pythia14b_hires_bf16_2bitonly_profiles.json` | hires flat | 0.1183 | (同) | 0.1183 | ✅ |
| **Mistral-7B-v0.3** | `mistral_ppl_profiles_hires.json` | **旧 metadata 格式** | 0.1820 | `mistral_hires_bf16_2bitonly_profiles.json` | **0.2612** | ❌ **差 +43%** |
| **Gemma-2-9B** | `gemma2_profiling_results.json` | **lowres** | 0.1757 | `gemma2_hires_bf16_2bitonly_profiles.json` | **0.2056** | ❌ **差 +17%** |

## 需要修正

**2 个模型数据源错误**：

1. **Gemma-2-9B**：用了 lowres 文件 `gemma2_profiling_results.json`，应改为 `gemma2_hires_bf16_2bitonly_profiles.json`
   - t1/t5: 0.1757 → 0.2056

2. **Mistral-7B-v0.3**：用了旧格式 `mistral_ppl_profiles_hires.json`（带 metadata wrapper，非标准 hires bf16 2bitonly），应改为 `mistral_hires_bf16_2bitonly_profiles.json`
   - t1/t5: 0.1820 → 0.2612

**注意**：Qwen2.5-7B 的文件名 `hires_profiles.json` 命名不规范（其他模型都是 `{model}_hires_bf16_2bitonly_profiles.json`），但格式和数值均正确，无需改。

是否要我修正 `compute_shape_metrics.py` 并重新生成 `shape_metrics.json`？

---
