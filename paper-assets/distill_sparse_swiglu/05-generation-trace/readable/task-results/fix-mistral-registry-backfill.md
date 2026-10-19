# fix mistral registry backfill

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_mistral_registry_backfill_20260517T114351_result.json`
- **Structured JSON:** [`1b939f8da5b143bfe984.json`](../../sessions/1b/1b939f8da5b143bfe984.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 12 Mistral experiments registered. Summary:

## 已注册 Mistral 实验汇总

| exp_id | Mode | Sparsity | WikiText-2 PPL | vs Dense | Conclusion |
|--------|------|----------|----------------|----------|------------|
| `mistral_dense_ppl` | Dense | 0% | **5.5238** | — | success |
| `mistral_kl30_pertoken` | KL per-token | 30% | 6.048 | +0.52 | success |
| `mistral_kl30_teal_global` | KL teal-global | 30% | 6.7733 | +1.25 | success |
| `mistral_teal30_baseline` | TEAL vanilla | 30% | 8.3807 | +2.86 | success |
| `mistral_kl50_pertoken` | KL per-token | 50% | 7.2931 | +1.77 | success |
| `mistral_kl50_teal_global` | KL teal-global | 50% | 8.6489 | +3.13 | success |
| `mistral_teal50_baseline` | TEAL vanilla | 50% | 18.3061 | +12.78 | success |
| `mistral_kl70_pertoken` | KL per-token | 70% | 9.1086 | +3.58 | success |
| `mistral_kl70_teal_global` | KL teal-global | 70% | 13.3254 | +7.80 | success |
| `mistral_teal70_baseline` | TEAL vanilla | 70% | 61.716 | +56.19 | success |

**Downstream (lm-eval-harness):**

| exp_id | ARC-C (norm) | WinoGrande | MMLU | GSM8K | Conclusion |
|--------|-------------|------------|------|-------|------------|
| `lm_eval_mistral_dense` | 0.6024 | 0.7869 | 0.6244 | 0.3654 | success |
| `lm_eval_mistral_kl_50pct` | 0.3183 | 0.6290 | 0.2295 | 0.0045 | negative |

9 新注册 + 3 已存在（`mistral_teal50_baseline`, `lm_eval_mistral_dense`, `lm_eval_mistral_kl_50pct`），共 12 条。KL predictor 在所有 sparsity 下均显著优于 TEAL vanilla baseline（PPL 降幅 28%~85%）。

---
