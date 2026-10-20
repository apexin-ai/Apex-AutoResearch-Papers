# Seed-Level Demeaning LOGO

## Experiment

**Goal**: Address the seed-sharing confound. For each (seed, generator), subtract depth-0 feature values as a baseline, then classify gen-1 vs gen-2+ using only the delta features.

**Method**: For every (model_name, seed_id) group, compute Δfeature = feature(depth_k) - feature(depth_0). Drop depth-0 rows (Δ=0, would leak). Run standard 8-gen LOGO binary eval with XGBoost (same hyperparams as eval_8gen_logo.py).

**Data**: 37058 total rows -> 29095 after removing depth-0.

## Results

| Generator | Binary F1 | 95% CI |
|-----------|-----------|--------|
| pythia-1b | 0.7814 | [0.7664, 0.7967] |
| qwen3-1.7b | 0.7498 | [0.7342, 0.7630] |
| qwen3-0.6b | 0.7457 | [0.7295, 0.7608] |
| pythia-2.8b | 0.7352 | [0.7217, 0.7503] |
| olmo-2-1b | 0.6956 | [0.6792, 0.7105] |
| llama-3.2-3b | 0.6893 | [0.6748, 0.7037] |
| qwen3-8b | 0.6623 | [0.6461, 0.6786] |
| mistral-7b-v0.3 | 0.5472 | [0.5319, 0.5628] |
| **AVERAGE** | **0.7008** | |

## Interpretation

Average F1 = 0.7008, compared to the undemeaned baseline of 0.694.

The result falls within the expected range [0.674, 0.714], confirming: **depth signal is preserved after removing seed-level topic variation**. The classifier's ability to distinguish gen-1 from gen-2+ does not depend on seed-specific content; it relies on generative degradation patterns that persist across seeds.

Slight improvement (+0.7pp) suggests seed-level topic variation may have been mild noise rather than a helpful signal.

mistral-7b-v0.3 remains the weakest performer (0.547), consistent with prior LOGO results.
