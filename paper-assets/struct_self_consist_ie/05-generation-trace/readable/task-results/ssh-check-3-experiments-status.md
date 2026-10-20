# ssh check 3 experiments status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_3_experiments_status_20260522T145321_result.json`
- **Structured JSON:** [`57dad11b54b0d8e8e9db.json`](../../sessions/57/57dad11b54b0d8e8e9db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

---

## Experiment Status

### 1. exp_fewnerd_pretrained_n16_s42 (5090-c:cuda:1) — CRASHED

- **Error**: `UnicodeEncodeError: 'utf-8' codec can't encode character '\udced'` in `sampling.py:675` during `save_sampled_results()`
- **samples.jsonl**: 27,110 / 37,648 lines written (72%, incomplete)
- **report.json**: not generated (crash before report stage)
- **Runtime**: ~8h50m (13:31 → 22:21)
- Surrogate character in vLLM output caused the JSON write to fail.

### 2. exp_fewnerd_freeform_n8_s42 (5090:cuda:0) — COMPLETED

| Metric | Value |
|--------|-------|
| greedy_f1 | 0.7886 |
| oracle_f1 | 0.8782 |
| oracle_headroom | +0.0896 |
| fleiss_kappa_mean | 0.3529 |
| soft_jaccard_mean | 0.6745 |
| sample_f1_mean / std | 0.6122 / 0.3914 |
| sample_f1_pct_zero | 23.1% |
| Full ρ(SJ,F1) | +0.1630 |
| Cond ρ(SJ,F1) | +0.1993 |
| Full ρ(κ,F1) | +0.0463 |
| Cond ρ(κ,F1) | -0.0324 |
| structural_beats_surface | YES (Δ=+0.1167) |
| Logprob full ρ / AUROC | +0.1534 / 0.5769 |
| Logprob cond ρ / AUROC | +0.1644 / 0.5771 |
| **Verdict** | **FAIL** |

MV/LP/degeneracy metrics **not in report.json**, and no `/tmp/recompute_mv*.py` script found on either server.

### 3. exp_fewnerd_pretrained_n32_s42 (5090-c:cuda:3) — RUNNING 66%

- **Progress**: 799,680 / 1,204,736 prompts (66.3%)
- **Elapsed**: 10h38m
- **Speed**: ~20 it/s, 3786 input toks/s, 5653 output toks/s
- **GPU**: 29.8GB VRAM, 80% util, PID 387768 (VLLM::EngineCore)
- **ETA**: ~5-7 hours

---
