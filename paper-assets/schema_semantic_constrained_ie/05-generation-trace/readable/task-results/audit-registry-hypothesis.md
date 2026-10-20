# audit registry hypothesis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_registry_hypothesis_20260517T025352_result.json`
- **Structured JSON:** [`79b1d7af5db7c70a330a.json`](../../sessions/79/79b1d7af5db7c70a330a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部更新成功。汇报：

## 自检结果

| 指标 | 数量 |
|------|------|
| 检查实验总数 | 50 (DONE, success/negative) |
| 补写 hypothesis | 5 个 (`w5_lora_scierc_training`, `llama_docred_full_s1_mt6144`, `llama_docred_unconstrained_mt6144`, `posthoc_filtering_baseline`, `w1_cf_fallback_scierc_pilot`) |
| 补写 parent | 13 个 |

## 典型推导链

**链 1 — Qwen SciERC composability + ablation (4 层)**
```
w5_lora_scierc_training
  → w5_lora_scierc_unconstrained_eval (FT baseline: DR=1.95%)
    → w7_qwen_scierc_ft_grammar_only (grammar 不降 DR, 仍 1.9%)
    → w7_qwen_scierc_ft_semantic_only (semantic 降 DR 68%, 至 0.6%)
  → w5_lora_scierc_constrained_eval (full_s1: DR=0%, composability 验证)
```

**链 2 — Llama DocRED composability + ablation (3 层)**
```
w5_llama_docred_lora_training
  → w5_llama_docred_lora_unconstrained_eval (FT baseline: DR=0.49%)
  → w5_llama_docred_lora_constrained_eval (full_s1: DR=0%, composability)
  → w8_llama_docred_ft_grammar_only (grammar 不降 DR)
  → w8_llama_docred_ft_semantic_only (semantic 降 DR)
```

---
