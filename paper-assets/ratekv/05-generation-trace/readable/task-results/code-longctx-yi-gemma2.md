# code longctx yi gemma2

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_longctx_yi_gemma2_20260516T024109_result.json`
- **Structured JSON:** [`279442f94e82993035ee.json`](../../sessions/27/279442f94e82993035ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本都创建完毕，语法检查通过。

**`run_yi_longcontext_8k.py`** — Yi-1.5-9B 8K eval
- 合并 `yi15_hires_bf16_2bitonly_profiles.json` (2-bit) + `yi15_profiling_results.json` (4/8-bit)
- 使用标准 `patch_attention` / `evaluate_perplexity` from `eval_ppl.py`
- 支持 `--gpu cuda:X`

**`run_gemma2_longcontext_8k.py`** — Gemma-2-9B 8K eval
- 合并 `gemma2_hires_bf16_2bitonly_profiles.json` (2-bit) + `gemma2_profiling_results.json` (4/8-bit)
- 使用 `patch_attention_gemma2` from `run_gemma2_full_pipeline.py`（处理 softcapping + sliding window）
- 自带 `evaluate_perplexity_gemma2`（`cache_position` + BOS prepend，复用自 full pipeline 的 eval 逻辑）
- 标准 profile JSON 可能嵌套在 `"profiles"` key 下，已做兼容处理
- 支持 `--gpu cuda:X`

---
