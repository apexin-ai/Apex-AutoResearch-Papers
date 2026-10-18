# code fix max2bit bugs

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_max2bit_bugs_20260516T033345_result.json`
- **Structured JSON:** [`8929574a27d602fe1066.json`](../../sessions/89/8929574a27d602fe1066.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes verified. Final cross-check against the correct k-value table:

| Model | Correct k | Files | Status |
|-------|-----------|-------|--------|
| **Qwen-7B** (k=8) | `run_qwen_longcontext_8k.py`=8, `run_qwen_hires_constrained.py`=8, `run_qwen7b_8k_spotcheck.py`=8, `run_qwen7b_longcontext_8k.py`=8, `run_qwen_3seed_downstream_ci.py`=8, `run_qwen14b_*`=8, `run_c4_cross_dataset.py`=8, `run_kivi_mckp_combined.py`=8 | all correct |
| **Gemma-2** (k=8) | `run_gemma2_3seed_downstream_ci.py`=8, `run_gemma2_longcontext_8k.py`=8 | all correct |
| **Phi-3** (k=8) | `run_phi3_longcontext_8k.py`=8, `run_phi3_medium_constrained_pipeline.py`=8 | all correct |
| **CodeLlama** (k=8) | `run_codellama_longcontext_8k.py`=8 | correct |
| **Yi-1.5** (k=2) | `run_yi_3seed_downstream_ci.py`=**2** ✓, `run_yi_longcontext_8k.py`=**2** ✓, `run_yi15_8k_spotcheck.py`=**2** ✓, `run_yi15_hires_constrained.py`=2 | all correct |
| **Llama-3.1** (k=2) | `run_llama_8k_eval.py`=2, `run_llama8b_8k_eval.py`=2, `run_llama_8k_spotcheck.py`=2, `run_w3_downstream_eval.py`=**2** ✓, `run_llama_c4_cross_dataset.py`=2 | all correct |
| **Mistral-7B** (k=2) | `run_mistral_3seed_downstream_ci.py`=**2** ✓, `run_mistral_8k_eval.py`=2, `run_mistral7b_8k_eval.py`=2, `run_mistral_hires_constrained.py`=2, `run_mistral_c4_cross_dataset.py`=**2** ✓ | all correct |
| **InternLM2** (k=2) | `run_internlm2_longcontext_8k.py`=**2** ✓, `run_internlm2_constrained_mckp.py`=2 | all correct |

## 修改清单

| # | 文件 | 行号 | 修改前 → 修改后 | 位置 |
|---|------|------|----------------|------|
| 1 | `run_yi_3seed_downstream_ci.py` | 36 | `MAX_2BIT = 8` → `MAX_2BIT = 2` | local |
| 2 | `run_mistral_3seed_downstream_ci.py` | 36 | `MAX_2BIT = 8` → `MAX_2BIT = 2` | local |
| 3 | `run_qwen_longcontext_8k.py` | 26 | `models/Qwen/...` → `.hf_cache/Qwen/...` | local |
| 4 | `run_internlm2_longcontext_8k.py` | 212 | `max_2bit = 8` → `max_2bit = 2` | local |
| 5 | `run_yi_longcontext_8k.py` | 31 | `max_2bit = 8` → `max_2bit = 2` | local |
| 6 | `run_yi15_8k_spotcheck.py` | 25 | `max_2bit = 8` → `max_2bit = 2` | local + server |
| 7 | `run_w3_downstream_eval.py` | 31 | `MAX_2BIT = 8` → `MAX_2BIT = 2` | local + server |
| 8 | `run_mistral_c4_cross_dataset.py` | 18 | `MAX_2BIT = 4` → `MAX_2BIT = 2` | local + server |

Qwen 模型路径 `/root/autodl-tmp/.hf_cache/Qwen/Qwen2___5-7B` 在服务器上已确认存在（4 个 safetensors + config.json 完整）。

系统性审查发现了 4 个额外 bug（#5-#8），已一并修复。5 个仅在本地的文件（#1-#5）需要在下次 sync_code 时推送到服务器。

---
