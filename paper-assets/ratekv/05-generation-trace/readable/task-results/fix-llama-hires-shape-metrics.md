# fix llama hires shape metrics

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_llama_hires_shape_metrics_20260515T142158_result.json`
- **Structured JSON:** [`fc4e7eb69382b1f7ba21.json`](../../sessions/fc/fc4e7eb69382b1f7ba21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**变更**：`compute_shape_metrics.py` 第6行 Llama 路径从 `llama_profiling_results.json`（lowres）改为 `llama_hires_bf16_2bitonly_profiles.json`（hires）。

**更新后 7 模型 shape_metrics**：

| Model | top5_conc | top1_share | Gini |
|-------|-----------|------------|------|
| Qwen2.5-7B | 0.6104 | 0.3461 | 0.7065 |
| Qwen2.5-14B | 0.3312 | 0.1885 | 0.5626 |
| **Llama-3.1-8B** | **0.5749** | **0.4867** | **0.6695** |
| Yi-1.5-9B | 0.7139 | 0.6434 | 0.7772 |
| Mistral-7B-v0.3 | 0.2200 | 0.0401 | 0.4941 |
| Gemma-2-9B | 0.2299 | 0.0404 | 0.5305 |
| Pythia-1.4B | 0.2439 | 0.0289 | 0.5301 |

Llama concentration 从 0.3387 → **0.5749**，与 registry 和 hires 实验结果一致。其他模型值不变。

---
