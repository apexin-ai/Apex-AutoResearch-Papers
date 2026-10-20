# exp-015 Neural Probe Script

## Location
westc-26893: `/root/autodl-tmp/gen-depth-contamination/scripts/run_exp015_neural_probe.py`

## Architecture
- Frozen Qwen2.5-1.5B → last hidden state → avg pool → 1536-dim
- MLP (1536→512→256→N_classes), Adam + early stopping
- 5-fold GroupKFold CV (by doc_id), pairwise AUC with P(j)/(P(i)+P(j)) normalization
- Auto-loads LightGBM baseline for comparison

## Dry-run
`--num_samples 50 --max_depth 2` → 8 seconds, K*=2, JSON output complete

## Full run command
```bash
python scripts/run_exp015_neural_probe.py \
    --data_dir data_exp017_qwen_cont data_exp001_pythia data_exp002_olmo \
    --label Qwen-cont Pythia OLMo \
    --max_depth 5
```

## Status
Code ready, awaiting GPU (after exp-006)
