# code mistral constrained mckp

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_constrained_mckp_20260515T143635_result.json`
- **Structured JSON:** [`506495ecdcc98ba5d080.json`](../../sessions/50/506495ecdcc98ba5d080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`run_mistral_hires_constrained.py` 已就绪，验证通过：

- **模型**: `/root/autodl-tmp/models/Mistral-7B-v0.3`（32L × 8KV, GQA 4:1, 256 heads）
- **输入**: `mistral_hires_bf16_2bitonly_profiles.json` + `mistral_profiling_results.json`（两文件均已存在）
- **MCKP**: constrained, max_2bit=2, budget=0.25, l0_exclude_2bit=True
- **Eval**: BF16 baseline → Constrained MCKP → Uniform 4-bit，WikiText-2 PPL
- **输出**: `artifacts/mistral_hires_constrained_results.json`
- **运行**: `python run_mistral_hires_constrained.py`（cuda:0 空闲后直接跑）

---
