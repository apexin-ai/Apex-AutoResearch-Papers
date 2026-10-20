# MVP Probe Analysis Report

## Experiment Summary
- **Task**: temporal_distance probing on OpenVLA-7B hidden states (33 LLM layers)
- **Data**: 500 trajectories, 10 tasks, 5000 pairs/task
- **Server**: westd-19183

## Layer Collapse
Major probe training instability — many layers produce constant predictions (ρ=0):
- Both collapsed: 3 layers (0, 26, 32)
- Trained only collapsed: 7 layers (16, 18, 22, 23, 24, 28, 30)
- Untrained only collapsed: 6 layers (3, 9, 15, 20, 27, 31)
- Both valid: 17 layers

Notable: training CAUSED 7 layers to collapse that were functional in untrained model.

## Top-5 Layers

### Trained
| Rank | Layer | per_task_mean_ρ |
|------|-------|-----------------|
| 1 | 3 | 0.9562 |
| 2 | 4 | 0.9550 |
| 3 | 2 | 0.9547 |
| 4 | 5 | 0.9502 |
| 5 | 6 | 0.9495 |

### Untrained
| Rank | Layer | per_task_mean_ρ |
|------|-------|-----------------|
| 1 | 1 | 0.9334 |
| 2 | 13 | 0.9321 |
| 3 | 5 | 0.9310 |
| 4 | 8 | 0.9278 |
| 5 | 2 | 0.9278 |

## Δρ Analysis (17 non-collapsed layers)
| Metric | Value |
|--------|-------|
| Max Δρ | +0.0427 (Layer 4) |
| Mean Δρ | +0.0194 |
| Std Δρ | 0.0179 |
| Positive | 16/17 layers |
| Only negative | Layer 13 (-0.0292) |

## MVP Gate Evaluation
| Gate | Criterion | Value | Threshold | Result |
|------|-----------|-------|-----------|--------|
| 1 | best_layer ρ > 0.5 | 0.9562 | 0.5 | **PASS** |
| 2 | max Δρ > 0.1 | 0.0427 | 0.1 | **FAIL** |
| 3 | VLA ρ ≥ DINO-V2 | 0.9562 vs 0.901 | 0.901 | **PASS** |

## **Overall Verdict: FAIL**

## DINO-V2 Comparison
- DINO-V2 ρ = 0.901
- VLA trained best = 0.9562 (+6.1%)
- VLA untrained best = 0.9334 (+3.6%)
- Key: untrained VLA already exceeds DINO-V2, confirming signal comes from SigLIP vision encoder (ViT-SO400M), not LLM training

## Conclusion
LLM training contributes max Δρ=0.043 over untrained backbone — far below the 0.1 significance threshold. The temporal distance signal is overwhelmingly from the pretrained SigLIP vision encoder. This is a **negative result** for the VLA-SSD hypothesis that VLA training encodes meaningful scene structure in the LLM layers.
