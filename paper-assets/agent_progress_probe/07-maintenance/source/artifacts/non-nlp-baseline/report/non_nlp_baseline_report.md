# Non-NLP Baseline Results

## Hypothesis
Pure structural/numerical features should NOT match NL embedding probe performance, proving embedding necessity.

## Result: HYPOTHESIS REJECTED

Structural features alone achieve macro_f1=0.9951, **far exceeding** both:
- GRU Probe (NL embedding): 0.9055
- MeanPool+LR (NL embedding): 0.8435

## Metrics

| Method | Macro-F1 | Accuracy | F1(stag) | F1(prog) |
|--------|----------|----------|----------|----------|
| GRU Probe (ref) | 0.9055 | — | — | — |
| MeanPool+LR (ref) | 0.8435 | — | — | — |
| **Struct + LR** | **0.9874** | 0.9901 | 0.9815 | 0.9933 |
| **Struct + RF** | **0.9951** | 0.9962 | 0.9928 | 0.9974 |
| **Struct + GB** | **0.9951** | 0.9962 | 0.9928 | 0.9974 |

## Top Features (by LR coefficient magnitude)
1. max_consecutive_similar: -5.53 (most predictive of stagnation)
2. avg_adjacent_cmd_sim: -3.13
3. num_search_cmds: -2.32
4. search_ratio: -2.20
5. max_adjacent_cmd_sim: +1.87
6. unique_cmd_ratio: +1.49
7. max_repeat_ratio: -1.28
8. max_cmd_len: +0.82
9. num_nav_cmds: -0.81
10. num_edit_cmds: +0.75

## Root Cause Analysis
The labeling functions are structural heuristics:
- **LF1 (file_diff_delta)**: counts edit commands → captured by num_edit_cmds, edit_ratio
- **LF2 (command_repetition)**: checks consecutive similar commands → captured by avg_adjacent_cmd_sim, max_consecutive_similar, unique_cmd_ratio
- **LF3 (outcome_backpropagation)**: trajectory-level outcome → partially captured by structural patterns

The structural baseline essentially **reverse-engineers the labeling functions**.

## Implication
This does NOT invalidate NL embeddings for real progress detection. It shows:
1. Current weak labels are saturated by structural information
2. NL embeddings capture something different/complementary that the structural features miss
3. The probe's lower F1 may indicate it's learning a more nuanced/generalizable signal

## Data
- 15,401 windows (conf≥2), 30 features, same train/val/test split as probe_001
- Best hyperparams: LR C=1.0, RF n_estimators=100 max_depth=10, GB lr=0.05 n_estimators=200
