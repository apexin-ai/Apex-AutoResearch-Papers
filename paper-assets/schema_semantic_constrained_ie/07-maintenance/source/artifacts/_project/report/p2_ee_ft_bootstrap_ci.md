# D060: WikiEvents EE FT Bootstrap 95% Confidence Intervals

## Setup
- Task: Event Extraction on WikiEvents (20 test documents)
- Method: Percentile bootstrap, 10000 resamples, resampling at document level
- Seed: 42
- Metrics: RoV (role vocabulary violation rate), AC (argument constraint violation rate), Go/No-go (RoV + AC combined)
- Denominator: total arguments from all events (including EV-violated events), matching original violation checker methodology

## Results

### Qwen3-8B FT

| Condition | Metric | Point Est. | 95% CI Lower | 95% CI Upper |
|-----------|--------|-----------|--------------|--------------|
| Unconstrained | RoV | 38.31% | 25.13% | 46.84% |
| Unconstrained | AC | 2.68% | 1.21% | 5.64% |
| Unconstrained | Go/No-go | 41.00% | 27.91% | 49.14% |
| Constrained (full_s1) | RoV | 0.00% | 0.00% | 0.00% |
| Constrained (full_s1) | AC | 0.00% | 0.00% | 0.00% |
| Constrained (full_s1) | Go/No-go | 0.00% | 0.00% | 0.00% |

- 17 checked docs (3 parse failures), 261 total args (unconstrained)
- 19 checked docs (1 parse failure), 339 total args (constrained)

### Llama-3.1-8B FT

| Condition | Metric | Point Est. | 95% CI Lower | 95% CI Upper |
|-----------|--------|-----------|--------------|--------------|
| Unconstrained | RoV | 8.75% | 2.42% | 15.35% |
| Unconstrained | AC | 3.45% | 0.88% | 5.97% |
| Unconstrained | Go/No-go | 12.20% | 4.73% | 18.97% |
| Constrained (full_s1) | RoV | 0.00% | 0.00% | 0.00% |
| Constrained (full_s1) | AC | 0.78% | 0.00% | 1.73% |
| Constrained (full_s1) | Go/No-go | 0.78% | 0.00% | 1.73% |

- 20 checked docs (0 parse failures), 377 total args (unconstrained)
- 20 checked docs (0 parse failures), 255 total args (constrained)

## Key Observations

1. **Qwen unconstrained CI is wide** ([27.91%, 49.14%] for Go/No-go) due to high per-doc variance and only 17 valid docs.
2. **Constrained Qwen achieves perfect 0%** across all metrics with zero variance (deterministic output).
3. **Llama unconstrained** has narrower CI than Qwen because violations are more evenly distributed and all 20 docs parse successfully.
4. **Llama constrained residual AC** (0.78%) has CI [0.00%, 1.73%], indicating 2/255 violations come from a single doc; in most resamples this goes to 0.
5. **Non-overlapping CIs**: Qwen unconstrained Go/No-go CI lower bound (27.91%) is far above constrained upper bound (0.00%), confirming statistically significant improvement.

## Source Files
- Qwen (westd-21461): `outputs/ee_qwen_ft_wikievents_{unconstrained_r5,full_s1_r5}.jsonl`
- Llama (westd-16980): `outputs/ee_llama_ft_wikievents_{unconstrained_r2,full_s1_r2}.jsonl`
- Constraints: `data/wikievents/ontology_constraints_wikievents.json`
- JSON results: `outputs/bootstrap_ci_ee_ft_qwen.json` (westd-21461), `outputs/bootstrap_ci_ee_ft_llama.json` (westd-16980)
