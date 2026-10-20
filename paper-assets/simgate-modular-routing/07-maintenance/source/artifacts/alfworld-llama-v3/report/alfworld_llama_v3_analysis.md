# ALFWorld Llama-3.1-8B Counterfactual Analysis

**Date**: 2026-05-20
**Experiment**: alfworld-llama-v3
**Status**: DONE (success)

## Summary
- 135 episodes, all ALFWorld valid_seen games
- det-preferred: 16 (11.9%) [95% CI: 6.7%, 17.8%]
- int-preferred: 0 (0.0%)
- no-preference: 119 (88.1%)
- det-leaning (non-tie): 100.0%
- DAF: 0% (no death mechanism)
- Δ_full: 0.1185 [95% CI: 0.0667, 0.1778]

## Per-task Breakdown

| task_type | n | det | int | tie | det% |
|-----------|---|-----|-----|-----|------|
| pick_and_place | 32 | 12 | 0 | 20 | 37.5% |
| look_at_obj_in_light | 13 | 1 | 0 | 12 | 7.7% |
| pick_clean_then_place | 27 | 2 | 0 | 25 | 7.4% |
| pick_cool_then_place | 24 | 1 | 0 | 23 | 4.2% |
| pick_heat_then_place | 16 | 0 | 0 | 16 | 0.0% |
| pick_two_obj_and_place | 23 | 0 | 0 | 23 | 0.0% |

## Llama vs Qwen Comparison

| Model | Det-Pref | Int-Pref | Tie | Det-Leaning | DAF |
|-------|----------|----------|-----|-------------|-----|
| Llama-3.1-8B | 11.9% | 0.0% | 88.1% | 100.0% | 0% |
| Qwen2.5-7B | 25.9% | 0.0% | 72.6% | 100.0% | 0% |

## Key Findings
1. Hypothesis confirmed: ALFWorld routing signal is information asymmetry, not death avoidance
2. int-preferred = 0 across both models
3. pick_and_place drives most signal (37.5% det-preferred)
4. Llama det-preferred lower than Qwen (11.9% vs 25.9%) but direction identical

## Data Files
- Episodes: westb-13313:/root/autodl-tmp/simgate-modular-routing/results/alfworld_llama_counterfactual/episodes.jsonl
- Analysis: westb-13313:/root/autodl-tmp/simgate-modular-routing/results/alfworld_llama_counterfactual/analysis.json
- LaTeX: westb-13313:/root/autodl-tmp/simgate-modular-routing/results/alfworld_llama_counterfactual/latex_table.tex
