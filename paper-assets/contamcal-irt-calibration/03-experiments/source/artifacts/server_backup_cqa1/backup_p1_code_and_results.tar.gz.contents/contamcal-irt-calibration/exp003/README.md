# exp-003: RRF Aggregation of Contamination Detection Signals

Fuses 4 per-item signal scores from exp-002 into composite exposure scores
using Reciprocal Rank Fusion (RRF). Produces per-model per-item exposure
scores for downstream IRT calibration (exp-006).

## Input

Signal JSONs from exp-002:
```
/root/autodl-tmp/exp002/signals/{ModelName}_{dosage}_{seed}/
  signal_embedding_{benchmark}.json
  signal_minkpp_{benchmark}.json
  signal_constat_{benchmark}.json
  signal_selfcritique_{benchmark}.json
  signals_merged_{benchmark}.json   # optional merged file
```

Each signal file: `[{"index": 0, "benchmark": "mmlu", "s1_embedding": 0.403, ...}, ...]`

Ground truth labels from exp-001:
```
/root/autodl-tmp/exp001/sft_data/contamination_labels_{benchmark}_{dosage}.json
  {"benchmark": "mmlu", "dosage": 5, "total_items": 14042, "contaminated_count": 703, "labels": [0,1,...]}
```

## Output

Per-item exposure scores in [0, 1]: 0=clean, 1=definitely contaminated.

```json
[{"index": 0, "benchmark": "mmlu", "exposure": 0.82, "rrf_raw": 0.0163, "rank_s1_embedding": 42}, ...]
```

For exp-006: `exposure_scores.json` with `{model_id: {benchmark: {exposure_scores: [...], item_count: N}}}`

## Usage

### Main RRF aggregation

```bash
# Single model
python exp003/rrf_aggregation.py \
  --signal-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42 \
  --output-dir /root/autodl-tmp/exp003/results

# All models
python exp003/rrf_aggregation.py \
  --output-dir /root/autodl-tmp/exp003/results

# Generate exposure_scores.json for exp-006
python exp003/rrf_aggregation.py \
  --generate-exposure \
  --output-dir /root/autodl-tmp/exp003/results
```

### Ablations

```bash
python exp003/ablations.py \
  --signal-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42 \
  --benchmark mmlu \
  --dosage d005 \
  --output-dir /root/autodl-tmp/exp003/ablations
```

### Evaluation

```bash
# Mock data test
python exp003/evaluate_rrf.py --mock --output-dir /tmp/exp003_mock

# Single model-benchmark
python exp003/evaluate_rrf.py \
  --signal-dir /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42 \
  --benchmark mmlu --dosage d005 \
  --output-dir /root/autodl-tmp/exp003/eval

# All available combos
python exp003/evaluate_rrf.py --all --output-dir /root/autodl-tmp/exp003/eval
```

## Ablation Variants

| ID | Method | Description |
|----|--------|-------------|
| (a) | rank_avg | Equal-weight rank averaging |
| (b) | single_{signal} | Single-signal only (x4 baselines) |
| (c) | calibrated_rrf | Weighted RRF with oracle weights from ground truth |
| (d) | fp_{rate}pct_{method} | FP injection robustness at 5/10/20% rates |
| (e) | degraded_2sig | ConStat + Self-Critique only (closed-weight scenario) |

## Key Parameters

- `--k`: RRF smoothing parameter (default: 60)
- `--dosage-filter`: Only process matching dosages
- `--no-normalize`: Output raw RRF scores instead of [0,1]
