# figure heatmap hires regen

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_figure_heatmap_hires_regen_20260514T215716_result.json`
- **Structured JSON:** [`273225820d17fbe4bc74.json`](../../sessions/27/273225820d17fbe4bc74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

图表生成完成。

**验证结果：**
- Llama L2H5=15.3 是最亮 cell ✓
- Qwen L0 区域（L0H0=6.7）最亮 ✓
- Yi-1.5 L4H3=13.1 标注 ✓
- 维度：Gemma-2 42×8, Llama 32×8, Mistral 32×8, Qwen 28×4, Yi-1.5 48×4 ✓
- Gemma-2 标 `*` 注明使用 standard profiling ✓

**数据源：**
| 模型 | 文件 | 类型 |
|------|------|------|
| Qwen2.5-7B | `hires_profiles.json` | hires float32 |
| Llama-3.1-8B | `llama_hires_bf16_2bitonly_profiles.json` | hires bf16 |
| Yi-1.5-9B | `yi15_hires_bf16_2bitonly_profiles.json` | hires bf16 |
| Mistral-7B-v0.3 | `mistral_ppl_profiles_hires.json` | hires |
| Gemma-2-9B | `gemma2_profiling_results.json` | standard* |

文件已保存至论文目录和 artifacts。注意 Yi-1.5 实际维度是 48×4（非任务预期的 48×1）。

---
