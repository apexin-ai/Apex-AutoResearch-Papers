# analysis plan 006 llama rsft seed43 eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_006_llama_rsft_seed43_eval_r2_20260517T183904_result.json`
- **Structured JSON:** [`e28b2cc7f651fd8341d0.json`](../../sessions/e2/e28b2cc7f651fd8341d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果：plan_006_llama_rsft_seed43_eval_r2

### 关键指标

| Metric | Seed 42 | Seed 43 | Delta |
|--------|---------|---------|-------|
| **rel_f1 (Ign-F1)** | 0.5674 | **0.5619** | -0.55pp |
| F1 (full) | — | 0.5727 | — |
| Evi-F1 (joint) | — | 0.4551 | — |
| Evi-F1 (TP only) | — | 0.8206 | — |
| EDCR | — | 0.6073 | — |
| Format OK | — | 985/985 (100%) | — |
| Truncated | — | 197/985 | — |

### Seed Robustness 判定

**Conclusion: SUCCESS**

Seed 43 的 rel_f1 (Ign-F1) = 0.5619，与 seed 42 的 0.5674 相差仅 **-0.55pp**，在预设的 ±1.5pp 容差范围 (0.55-0.58) 内。Cross-architecture RSFT claim 对 seed variance 具有鲁棒性。

### 路径确认

- **Checkpoint**: `/root/autodl-tmp/rsft_output_llama_3_1_8b_seed43/checkpoint-3312`
- **Eval output**: `/root/autodl-tmp/eval_results/plan_006_llama_rsft_seed43_eval_r2/`
- **Log**: `~/runs/faith-evidence-ie/plan_006_llama_rsft_seed43_eval_r2.log`

---
