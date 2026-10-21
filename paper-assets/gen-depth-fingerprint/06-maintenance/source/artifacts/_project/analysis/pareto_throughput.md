# Pareto Throughput Analysis

Hardware: NVIDIA RTX 5090 32 GB, FP16, avg sequence length ~237 tokens, N=100 texts.

## Throughput vs. Accuracy

| Method | ms/text | Binary F1 | 3-class F1 | Pareto | Notes |
| --- | --- | --- | --- | --- | --- |
| LD-Score | 0.61 | 0.6788 | 0.6326 | Yes | CPU trigram JSD, no GPU model |
| AvgLogProb | 8.58 | 0.6785 | 0.7085 | | 1x Pythia-410M forward |
| FastDetectGPT | 8.58 | 0.5805 | 0.6654 | | 1x Pythia-410M forward (shared) |
| **7-Feature (Ours)** | **9.70** | **0.6935** | **0.7616** | **Yes** | 1x Pythia-410M + CPU features + XGBoost |
| Binoculars | 22.17 | 0.5327 | 0.4094 | | 1x 410M + 1x 1B forward |
| 4-Det Ensemble | 22.80 | 0.6993 | 0.7790 | Yes | 4 detectors, shared 410M pass + 1B |
| 4-Det+Surface | 22.80 | 0.7044 | 0.7823 | Yes | 4 detectors + TTR + hapax_ratio |

## Key Findings

- **7-Feature is 2.4x faster** than 4-Det+Surface (9.7 vs 22.8 ms/text) with only 1.5% relative F1 gap (0.6935 vs 0.7044).
- **7-Feature sits on the Pareto frontier**: no method achieves both higher F1 and lower latency.
- **Resource efficiency**: 7-Feature uses 1 model (410M params, 905 MB GPU) vs 4-Det's 2 models (1.41B params, 2868 MB GPU), a 3.2x memory reduction.
- **LD-Score** is the fastest method (0.61 ms, CPU-only) with competitive binary F1, but its 3-class F1 (0.6326) is far below 7-Feature (0.7616), showing it cannot discriminate generation depth.
- **FLOPs ratio**: 7-Feature uses 1.94e+11 FLOPs/text vs 4-Det's 6.68e+11 (optimized), a 3.4x reduction.

## Output

- Figure: `artifacts/_project/paper/chart/fig_appendix_pareto.pdf`
- Data source: `results/efficiency_comparison.json` + `results/8gen_baselines.json`
