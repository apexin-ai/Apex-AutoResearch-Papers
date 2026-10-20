# D076 Seed Comparison Status

Generated: 2026-05-16

## Status Matrix

| Method | Seed | Directory | Status | Ign-F1 | Rel-F1 | Evi-F1 | EDCR | Source File |
|--------|------|-----------|--------|--------|--------|--------|------|-------------|
| CED | 42 | rsft_ced_s42_reeval | **RUNNING** | — | — | — | — | — |
| CED | 43 | rsft_ced_s43 | DONE | 0.4512 | 0.4601 | 0.8063 | 0.6542 | metrics.json |
| CED | 44 | rsft_ced_s44_reeval | **RUNNING** | — | — | — | — | — |
| CED | 45 | rsft_ced_s45 | DONE | 0.4416 | 0.4514 | 0.8174 | 0.6550 | metrics.json |
| flat-NLI | 42 | rsft_flat_nli_s42_reeval | **RUNNING** | — | — | — | — | — |
| flat-NLI | 43 | rsft_flat_nli_s43_reeval_r2 | **RUNNING** | — | — | — | — | — |
| flat-NLI | 44 | rsft_flat_nli_s44 | DONE | 0.4521 | 0.4615 | 0.8131 | 0.6458 | metrics_v2.json |
| flat-NLI | 45 | rsft_flat_nli_s45 | DONE | 0.4462 | 0.4551 | 0.8154 | 0.6521 | metrics_v2.json |

## Completion: 4/8 done, 4/8 running

- CED: 2/4 done (s43, s45), 2/4 running (s42, s44)
- flat-NLI: 2/4 done (s44, s45), 2/4 running (s42, s43)

## D076 Config Verification (completed evals)

All 4 completed evals confirmed D076 compliant: batch_size=4, max_new_tokens=1024, --no-quantize, --sft_adapter.

## Issue: CED lacks metrics_v2

CED s43 and s45 only have `metrics.json` (no `metrics_v2.json`). `seed_comparison.py` line:
```python
if p.name == "metrics.json":
    m.pop("ign_f1", None)
```
This strips `ign_f1` from CED results, making them unusable for paired t-test on the primary metric.

**Two options:**
1. Run ign_f1 recomputation script on CED s43/s45 to generate `metrics_v2.json`
2. Modify `seed_comparison.py` to accept `ign_f1` from `metrics.json` when config confirms D076 compliance (eval was run after the Ign-F1 fix was deployed)

## seed_comparison.py Directory Mapping

The script's METHODS dict already has correct mappings for all 8 reeval directories:
- CED: s42→rsft_ced_s42_reeval, s43→rsft_ced_s43, s44→rsft_ced_s44_reeval, s45→rsft_ced_s45
- flat-NLI: s42→rsft_flat_nli_s42_reeval, s43→rsft_flat_nli_s43_reeval_r2, s44→rsft_flat_nli_s44, s45→rsft_flat_nli_s45

No directory discovery issue. New reeval results will be picked up automatically when they produce metrics files.

## flat-NLI s43 History

- `rsft_flat_nli_s43_reeval` (r1): **batch_size=16** — not D076 compliant, discarded
- `rsft_flat_nli_s43_reeval_r2`: running with correct bs=4

## Server Files

- Machine-readable summary: `/root/autodl-tmp/eval_results/d076_seed_summary.json`
- Existing comparison output: `/root/autodl-tmp/eval_results/seed_comparison.json`
