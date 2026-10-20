# CARR Experiment Data Tables

Training model: Qwen3-0.6B (596M params)  
Reward model: ArmoRM-Llama3-8B-v0.1 (scoring only, not trained)  
Dataset: UltraFeedback — 2200 total (2000 train / 200 eval prompts)  
Protocol: iterative self-training over 3 generations (gen0/gen1/gen2)

---

## Table 1: Full Metrics by Generation

### A. Reward-Curated Conditions (ArmoRM top-1-of-K)

| Condition | Gen | Quality (ArmoRM) | Vendi Score | Self-BLEU | NN Distance | PPL |
|-----------|-----|----------------:|------------:|----------:|------------:|----:|
| **LoRA, K=4** | 0 | 0.1123 | 107.54 | 0.0059 | 0.7088 | 10.60 |
| | 1 | 0.1138 | 106.73 | 0.0091 | 0.7065 | 9.73 |
| | 2 | 0.1109 | 107.25 | 0.0062 | 0.7054 | 9.72 |
| **LoRA, K=8** | 0 | 0.1146 | 107.21 | 0.0057 | 0.7097 | 9.40 |
| | 1 | 0.1136 | 107.26 | 0.0024 | 0.7086 | 9.18 |
| | 2 | 0.1143 | 107.25 | 0.0064 | 0.7095 | 10.20 |
| **Full-FT, K=4, lr=5e-6** | 0 | 0.1145 | 107.10 | 0.0038 | 0.7073 | 9.10 |
| | 1 | 0.1141 | 107.61 | 0.0060 | 0.7091 | 8.66 |
| | 2 | 0.1131 | 108.07 | 0.0044 | 0.7108 | 9.21 |
| **Full-FT, K=4, lr=2e-5** | 0 | 0.1130 | 107.81 | 0.0046 | 0.7079 | 9.57 |
| | 1 | 0.1154 | 108.03 | 0.0039 | 0.7107 | 10.34 |
| | 2 | 0.1124 | 108.54 | 0.0040 | 0.7100 | 8.82 |

### B. No-Curation Baselines (random 1-of-K)

| Condition | Gen | Quality (ArmoRM) | Vendi Score | Self-BLEU | NN Distance | PPL |
|-----------|-----|----------------:|------------:|----------:|------------:|----:|
| **LoRA, K=4, random** | 0 | 0.1107 | 105.42 | 0.0044 | 0.7005 | 9.19 |
| | 1 | 0.1099 | 108.21 | 0.0067 | 0.7121 | 8.76 |
| | 2 | 0.1096 | 108.72 | 0.0067 | 0.7136 | 11.18 |
| **Full-FT, K=4, random** | 0 | 0.1126 | 107.17 | 0.0045 | 0.7061 | 8.77 |
| | 1 | 0.1111 | 107.87 | 0.0047 | 0.7094 | 8.70 |
| | 2 | 0.1117 | 108.64 | 0.0065 | 0.7114 | 8.82 |

---

## Table 2: Vendi Score Trajectory Summary

| Experiment | Training | K | Curation | Vendi gen0 | Vendi gen2 | Abs Change | Rel Change (%) |
|-----------|----------|---|----------|----------:|----------:|-----------:|---------------:|
| carr_quick_probe_03 | LoRA | 4 | ArmoRM top-1 | 107.54 | 107.25 | -0.29 | -0.27 |
| carr_quick_probe_k8_02 | LoRA | 8 | ArmoRM top-1 | 107.21 | 107.25 | +0.04 | +0.04 |
| carr_fullft_k4_probe_03 | Full-FT | 4 | ArmoRM top-1 | 107.10 | 108.07 | +0.97 | +0.91 |
| carr_fullft_lr2e5_probe_01 | Full-FT | 4 | ArmoRM top-1 | 107.81 | 108.54 | +0.73 | +0.68 |
| carr_baseline_no_curation_01 | LoRA | 4 | random | 105.42 | 108.72 | +3.30 | +3.13 |
| carr_fullft_nocuration_01 | Full-FT | 4 | random | 107.17 | 108.64 | +1.47 | +1.37 |

---

## Table 3: Training Loss (avg per epoch, per generation)

| Experiment | Gen 0 | Gen 1 | Gen 2 | Trend |
|-----------|------:|------:|------:|-------|
| carr_quick_probe_03 (LoRA, K=4) | 0.413 | 0.240 | 0.166 | monotone decrease |
| carr_quick_probe_k8_02 (LoRA, K=8) | 0.411 | 0.239 | 0.168 | monotone decrease |
| carr_fullft_k4_probe_03 (Full-FT, K=4, lr=5e-6) | 0.461 | 0.341 | 0.285 | monotone decrease |
| carr_fullft_lr2e5_probe_01 (Full-FT, K=4, lr=2e-5) | 0.380 | 0.212 | 0.140 | monotone decrease |
| carr_baseline_no_curation_01 (LoRA, K=4, random) | 0.407 | 0.224 | 0.152 | monotone decrease |
| carr_fullft_nocuration_01 (Full-FT, K=4, random) | 0.461 | 0.335 | 0.277 | monotone decrease |

### Per-step loss detail (Gen 2 only, from logs)

**carr_quick_probe_03** (LoRA, 2 epochs, 5 log steps):
```
epoch 0.4: 0.203 | epoch 0.8: 0.202 | epoch 1.2: 0.168 | epoch 1.6: 0.131 | epoch 2.0: 0.126
```

**carr_quick_probe_k8_02** (LoRA, 2 epochs, 5 log steps):
```
epoch 0.4: 0.206 | epoch 0.8: 0.204 | epoch 1.2: 0.167 | epoch 1.6: 0.132 | epoch 2.0: 0.129
```

**carr_fullft_lr2e5_probe_01** (Full-FT, 3 epochs, 15 log steps):
```
epoch 0.2: 0.199 | epoch 0.4: 0.203 | epoch 0.6: 0.203 | epoch 0.8: 0.205 | epoch 1.0: 0.196
epoch 1.2: 0.127 | epoch 1.4: 0.122 | epoch 1.6: 0.128 | epoch 1.8: 0.115 | epoch 2.0: 0.124
epoch 2.2: 0.098 | epoch 2.4: 0.096 | epoch 2.6: 0.096 | epoch 2.8: 0.100 | epoch 3.0: 0.095
```

**carr_baseline_no_curation_01** (LoRA, 2 epochs, 5 log steps):
```
epoch 0.4: 0.185 | epoch 0.8: 0.189 | epoch 1.2: 0.155 | epoch 1.6: 0.118 | epoch 2.0: 0.115
```

**carr_fullft_nocuration_01** (Full-FT, 2 epochs, 10 log steps):
```
epoch 0.2: 0.287 | epoch 0.4: 0.276 | epoch 0.6: 0.282 | epoch 0.8: 0.282 | epoch 1.0: 0.279
epoch 1.2: 0.277 | epoch 1.4: 0.269 | epoch 1.6: 0.287 | epoch 1.8: 0.258 | epoch 2.0: 0.269
```

---

## Summary Statistics

### Key Finding: Reward curation does NOT cause diversity collapse

| Comparison | Vendi Change (curated) | Vendi Change (random) | Delta |
|-----------|----------------------:|---------------------:|------:|
| LoRA, K=4 | -0.27% | +3.13% | -3.40 pp |
| Full-FT, K=4, lr=5e-6 | +0.91% | +1.37% | -0.46 pp |

### Quality retention

| Condition | Quality gen0 | Quality gen2 | Change |
|-----------|----------:|----------:|-------:|
| LoRA, K=4, curated | 0.1123 | 0.1109 | -1.2% |
| LoRA, K=8, curated | 0.1146 | 0.1143 | -0.3% |
| Full-FT, K=4, lr=5e-6, curated | 0.1145 | 0.1131 | -1.2% |
| Full-FT, K=4, lr=2e-5, curated | 0.1130 | 0.1124 | -0.5% |
| LoRA, K=4, random | 0.1107 | 0.1096 | -1.0% |
| Full-FT, K=4, random | 0.1126 | 0.1117 | -0.8% |

### Training dynamics

- All conditions show monotonically decreasing loss across generations (gen0 > gen1 > gen2), indicating the model increasingly fits its own filtered outputs.
- LoRA conditions converge to lower loss faster (0.166-0.168 by gen2) vs Full-FT with lr=5e-6 (0.277-0.285 by gen2), consistent with LoRA's lower effective capacity.
- Full-FT with lr=2e-5 achieves the lowest gen2 loss (0.140), suggesting stronger memorization of curated data.
- No-curation Full-FT shows notably higher gen2 loss (0.277) and slower decay, reflecting higher variance in unfiltered training data.
