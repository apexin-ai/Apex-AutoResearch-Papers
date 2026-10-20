# Multi-Model Pilot: Llama 3.1 8B Instruct

## Experiment Setup
- Model: Meta-Llama-3.1-8B-Instruct (ModelScope: LLM-Research/Meta-Llama-3.1-8B-Instruct)
- Server: westb-13313 (AutoDL)
- Tasks: freeze (high-death) + find-non-living-thing (zero-death)
- Episodes: 5 per task × 2 modalities = 20 total
- Seed: 42

## Results

### Freeze
| Ep | Internal | Det | Label | Signal |
|----|----------|-----|-------|--------|
| 0 | 0.0 | 0.0 | no-preference | tied_alive |
| 1 | 0.0 | 0.0 | no-preference | tied_alive |
| 2 | 0.0 | 0.0 | no-preference | tied_alive |
| 3 | -100.0 | 77.0 | det-preferred | death_asymmetry |
| 4 | -100.0 | -100.0 | no-preference | both_dead |

- Internal deaths: 2/5 = 40%
- Det deaths: 1/5 = 20%
- Death differential: +20% (internal > det)
- det-pref: 1, int-pref: 0, no-pref: 4

### find-non-living-thing
| Ep | Internal | Det | Label | Signal |
|----|----------|-----|-------|--------|
| 0 | 0.0 | 8.0 | det-preferred | score_comparison |
| 1 | 0.0 | 50.0 | det-preferred | score_comparison |
| 2 | 8.0 | 8.0 | no-preference | tied_alive |
| 3 | 0.0 | 50.0 | det-preferred | score_comparison |
| 4 | 58.0 | 0.0 | internal-preferred | score_comparison |

- Internal deaths: 0/5 = 0%
- Det deaths: 0/5 = 0%
- det-pref: 3, int-pref: 1, no-pref: 1

## Comparison with Qwen 2.5 7B Baseline

| Metric | Qwen (20 eps) | Llama (5 eps) | Consistent? |
|--------|---------------|---------------|-------------|
| freeze int death | 55% | 40% | ✓ direction |
| freeze det death | 25% | 20% | ✓ direction |
| freeze differential | 30% | 20% | ✓ int > det |
| fnlt int death | 0% | 0% | ✓ |
| fnlt det death | 0% | 0% | ✓ |

## Verdict: PASS

1. Pipeline compatibility: PASS — vLLM loaded Llama correctly, all 20 episodes completed
2. Death pattern direction: PASS — freeze: internal > det deaths (same as Qwen)
3. Death differential > 0: PASS — 20% on freeze
4. Zero-death task consistency: PASS — find-non-living-thing shows 0% deaths

Llama 3.1 8B Instruct is viable for full-scale counterfactual data collection.