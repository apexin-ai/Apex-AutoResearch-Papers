# diag s123 mmlu gap check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_s123-mmlu-gap-check_20260520T112550_result.json`
- **Structured JSON:** [`102a35fb0338071c292c.json`](../../sessions/10/102a35fb0338071c292c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the gap matrix:

## MMLU Eval Results Gap Matrix

| Family | s42 MMLU | s123 MMLU | s0 MMLU |
|--------|----------|-----------|---------|
| **Phi-4** | ✅ westd `eval_results_v2/phi4_d{000-100}` (5/5) | ❌ **缺失** | ❌ |
| **Qwen-14B** | ✅ westd `eval_results_v2/qwen14b_d{000-100}` (5/5) | ❌ **缺失** | ❌ |
| **Qwen-7B** | ✅ westd `eval_results_v2/qwen7b_d{000-100}` (5/5) | ✅ cqa1 `eval_results_v2/qwen7b_d{000-100}_s123` (5/5) | ❌ |
| **Gemma-2** | ✅ westd `eval_results_v2/gemma2_d{000-100}` (5/5) | ❌ **缺失** | ❌ |
| **OLMo-2** | ✅ westd `eval_results_v2/olmo2_d{000-100}` (5/5) | ❌ **缺失** | ✅ westd `results/mmlu_eval/olmo2/d{000-100}_s0` (5/5) |

### Triple-seed bootstrap CI 缺失项

s123 MMLU eval 缺失 **4 个家族 × 5 dosages = 20 个 eval 任务**：

1. **Phi-4** s123: d000, d005, d025, d050, d100
2. **Qwen-14B** s123: d000, d005, d025, d050, d100
3. **Gemma-2** s123: d000, d005, d025, d050, d100
4. **OLMo-2** s123: d000, d005, d025, d050, d100

只有 **Qwen-7B** s123 MMLU 完整（cqa1 上有两套：`eval_results` aligned 版 + `eval_results_v2` 版）。

---
