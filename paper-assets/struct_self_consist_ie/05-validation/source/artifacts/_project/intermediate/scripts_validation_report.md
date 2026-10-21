# DGS Method Validation Scripts - Validation Report

**Date**: 2026-05-18
**Server**: autodl-5090
**Location**: `/root/autodl-tmp/struct_self_consist_ie/code/`

## Scripts

| # | Script | Purpose | Status |
|---|--------|---------|--------|
| 1 | `analysis_dgs_full_validation.py` | DGS on 3 datasets, bootstrap CI, permutation test, degeneracy-stratified analysis | PASS |
| 2 | `analysis_dgs_ablation.py` | 5 strategies (Greedy, LP-all, DGS-degen-only, DGS-lp-only, DGS-full) ablation | PASS |
| 3 | `analysis_dgs_cross_model.py` | Cross-model DGS (LLaMA data), optional reference comparison | PASS |
| 4 | `analysis_dgs_multiseed.py` | Multi-seed stability, mean +/- std across seeds | PASS |

## Dry-Run Results

All 4 scripts passed `--dry-run` (argparse validation, import check).

## Real Data Test (20-instance SciERC subset, n_bootstrap=100)

### Script 1: Full Validation
```
Instances: 20, Degenerate: 2 (10.0%)
Method       Macro F1      95% CI               Micro F1
Greedy         0.7050 [0.5794, 0.8116]     0.7536
DGS            0.6612 [0.5467, 0.7690]     0.7042
LP-all         0.6612 [0.5467, 0.7690]     0.7042
Oracle         0.8305 [0.7479, 0.9122]
DGS-Greedy: -0.0438 p=0.2100
```

### Script 2: Ablation
```
LP range threshold (median): 0.037388
LP-gated: 10, Both gates active: 9
Strategy         Macro F1
Greedy             0.7050
LP-all             0.6612
DGS-degen-only     0.6612
DGS-lp-only        0.7080
DGS-full           0.7080
Oracle             0.8305
```

### Script 3: Cross-Model
Same output as script 1 (tested with same data as placeholder). JSON includes `model_agnostic_check` summary.

### Script 4: Multi-Seed
```
2 seeds (same data as test): std=0.0000 as expected.
Per-seed output with individual + aggregated metrics.
```

## Usage Examples

### Full validation (all 3 datasets)
```bash
python analysis_dgs_full_validation.py \
  --datasets \
    SciERC:/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl \
    CoNLL:/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl \
    FewNERD:/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl \
  --output /root/autodl-tmp/struct_self_consist_ie/output/dgs_full_validation.json
```

### Ablation
```bash
python analysis_dgs_ablation.py \
  --datasets \
    SciERC:/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl \
    CoNLL:/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_r1024/samples.jsonl \
    FewNERD:/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl \
  --output /root/autodl-tmp/struct_self_consist_ie/output/dgs_ablation.json
```

### Cross-model (when LLaMA data ready)
```bash
python analysis_dgs_cross_model.py \
  --datasets \
    LLaMA-SciERC:/path/to/llama_scierc/samples.jsonl \
    LLaMA-FewNERD:/path/to/llama_fewnerd/samples.jsonl \
  --reference-results /root/autodl-tmp/struct_self_consist_ie/output/dgs_full_validation.json \
  --output /root/autodl-tmp/struct_self_consist_ie/output/dgs_cross_model.json
```

### Multi-seed
```bash
python analysis_dgs_multiseed.py \
  --seeds \
    seed42:/path/to/seed42/samples.jsonl \
    seed123:/path/to/seed123/samples.jsonl \
    seed456:/path/to/seed456/samples.jsonl \
  --dataset-name SciERC \
  --output /root/autodl-tmp/struct_self_consist_ie/output/dgs_multiseed.json
```

## Implementation Notes

- Entity F1: span-based strict match `(start, end, type)` via `evaluation.entity_strict_match`
- Degeneracy: `len(set(round(f1, 10) for f1 in sample_f1s)) == 1`
- LP selection: `argmax(mean_logprob)` across N=8 samples
- Bootstrap: 10000 resamples, 95% CI (percentile method)
- Permutation test: paired, 10000 iterations
- Ablation LP threshold: median LP range across all instances
