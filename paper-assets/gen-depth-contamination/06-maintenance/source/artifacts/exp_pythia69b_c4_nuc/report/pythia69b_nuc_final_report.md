# Pythia-6.9B Nucleus Sampling Experiment — Final Report

**Experiment**: `exp_pythia69b_c4_nuc`  
**Date**: 2026-05-21  
**Server**: cqa1-22115  
**Result**: **K\* = 1 (NEGATIVE)**

---

## 1. Experiment Summary

Pythia-6.9B on C4 with nucleus sampling (top_p=0.95), scored by Qwen-1.5B.  
Prior greedy decoding (v3) gave K\*=2, but greedy inflates AUC — this run uses nucleus sampling aligned with other configurations.

## 2. Pairwise AUC (Qwen-1.5B scorer, θ=0.60)

| Pair | Mean AUC | Folds (5-fold CV) | Status |
|------|----------|-------------------|--------|
| 0v1 | **0.9599** ± 0.0051 | [0.9664, 0.9514, 0.9631, 0.9607, 0.9578] | ✓ above θ |
| 1v2 | **0.5955** ± 0.0086 | [0.5865, 0.6034, 0.6040, 0.5838, 0.5997] | ✗ below θ (borderline, Δ=0.0045) |
| 2v3 | **0.5298** ± 0.0126 | [0.5121, 0.5349, 0.5495, 0.5307, 0.5217] | ✗ below θ |
| 3v4 | **0.5135** ± 0.0133 | [0.5028, 0.5157, 0.5278, 0.5270, 0.4941] | ✗ below θ |

**K\* = 1**: Only depth 0→1 transition is distinguishable.

## 3. Supplementary Metrics

### Pairwise JSD
| Pair | JSD |
|------|-----|
| 0v1 | 0.125935 |
| 1v2 | 0.008417 |
| 2v3 | 0.003741 |
| 3v4 | 0.003474 |

### Ordinal Classification (6-class, 5-fold CV)
- MAE: 1.0170
- Accuracy: 0.3950

### Top-5 Feature Importance
| Feature | Importance |
|---------|-----------|
| freq_entropy | 7386.4 |
| surp_d1_skew | 6793.8 |
| surp_d1_mean | 6725.0 |
| surp_d2_mean | 6668.6 |
| surp_std | 6664.8 |

## 4. Data Completeness

| Depth | Lines | Status |
|-------|-------|--------|
| 0 (seed) | 5000 | ✓ complete |
| 1 | 5000 | ✓ complete |
| 2 | 5000 | ✓ complete |
| 3 | 5000 | ✓ complete |
| 4 | 5000 | ✓ complete |
| 5 | — | generating (57%, ETA ~46 min) |

Qwen scorer used depth 0–4 (max_depth=4). features.csv: 6.9 MB.

## 5. Paper Impact

**No paper update required.** K\*=1, so Pythia-6.9B (nucleus) does NOT join the K\*=2 group.

- Current paper claims: "8 model configurations, 6/8 yield K\*=2" — **unchanged**
- Pythia-6.9B nucleus result is consistent with OLMo-1B and Mistral-7B (all K\*=1)
- The greedy→nucleus transition drops K\* from 2 to 1, confirming that greedy decoding inflates discriminability

### Interpretation
The 1v2 AUC of 0.5955 is borderline (only 0.0045 below θ=0.60). Two of five folds exceed 0.60 (fold 2: 0.6034, fold 3: 0.6040). This suggests Pythia-6.9B sits at the boundary — nucleus sampling pushes it just below detectability at depth 2.

## 6. GPU Status

| GPU | Model | Memory | Util | Process |
|-----|-------|--------|------|---------|
| 0 | RTX 4090 D | 14495/24564 MiB | 97% | PID 443243 (Pythia-6.9B pipeline, depth_5 gen) |
| 1 | RTX 4090 D | 0/24564 MiB | 0% | idle (Qwen scorer completed) |
| 2 | RTX 4090 D | 0/24564 MiB | 0% | idle |
| 3 | RTX 4090 D | 0/24564 MiB | 0% | idle |

## 7. Unregistered Tasks on cuda:0

**None.** Only PID 443243 (the known Pythia-6.9B original pipeline) is running on cuda:0.

## 8. Paper Compilation

`latexmk -pdf main.tex` → "All targets (main.pdf) are up-to-date". No recompilation needed (no paper changes).

## 9. Registry Update

- `exp_pythia69b_c4_nuc`: status=DONE, conclusion=negative, metrics recorded
- Results directory: `results/exp_pythia69b_c4_nuc_qwen/`

## 10. Outstanding

- PID 443243 still generating depth_5 on cuda:0 (~46 min remaining). This will produce self-scored (Pythia-6.9B) results — not needed for paper (Qwen scorer results are authoritative).
- If depth_5 completes, a full 6-depth Qwen scorer run (max_depth=5) could be done for completeness, but unlikely to change K\* given 1v2 is already below θ.
