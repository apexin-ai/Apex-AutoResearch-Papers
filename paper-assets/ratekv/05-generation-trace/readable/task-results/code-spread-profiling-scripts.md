# code spread profiling scripts

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_spread_profiling_scripts_20260515T220542_result.json`
- **Structured JSON:** [`6b9e403758277e9a312d.json`](../../sessions/6b/6b9e403758277e9a312d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本语法正确。总结：

**`run_falcon7b_hires_profiling.py`**
- 架构：MQA, 32L × 1 KV head = **32 total heads**
- 模型结构：`model.transformer.h[i].self_attention`，fused `query_key_value`，output via `dense`
- 自定义 `patch_attention_falcon`：处理 fused QKV split、MQA broadcasting（71 query heads 共享 1 KV head）
- 预估 profiling 时间 ~30min（仅 32 次 eval）
- 默认模型路径：`/root/autodl-tmp/.hf_cache/tiiuae/falcon-7b`（占位符）

**`run_deepseekvl_hires_profiling.py`**
- 架构：MLA, 量化对象是 decompressed k_nope + value_states（k_pe 共享不量化）
- 模型结构：`model.model.layers[i].self_attn`，MLA 路径 `kv_a_proj → layernorm → kv_b_proj` 解压
- 自定义 `patch_attention_deepseek_v2`：在 kv_b_proj 解压后、RoPE 之前插入 per-head 量化
- RoPE 使用 DeepSeek 特有的 complex `freqs_cis` 格式（非 cos/sin tuple）
- `batch_size=1`（MLA 计算量较大）
- 默认模型路径：`/root/autodl-tmp/.hf_cache/deepseek-ai/DeepSeek-V2-Lite`（占位符）
- 实际 layers/heads 数从 config 动态读取

两个脚本均支持 `--model` 和 `--gpu` 参数，输出格式与其他 profiling 脚本一致（profiles JSON + results JSON + concentration/t1/t5 诊断）。

---
