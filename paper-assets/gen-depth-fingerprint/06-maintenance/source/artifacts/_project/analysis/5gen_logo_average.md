# 5-Gen LOGO Binary Eval

5 generators (cross-model chains subset), binary LOGO (gen-1 vs gen-2+, gen-0 excluded).

| Generator (held-out) | Binary F1 | 95% CI |
| --- | --- | --- |
| OLMo-2-1B | 0.6754 | [0.6601, 0.6905] |
| Pythia-1B | 0.7833 | [0.7688, 0.7971] |
| Pythia-2.8B | 0.7149 | [0.6999, 0.7305] |
| Qwen3-0.6B | 0.7439 | [0.7285, 0.7583] |
| Qwen3-1.7B | 0.7499 | [0.7348, 0.7644] |
| **Average** | **0.7335** | **[0.7184, 0.7482]** |
| 8-gen LOGO (ref) | 0.694 | — |
| Cross-model chains (ref) | 0.764 | — |

## Key takeaway

5-gen LOGO average (0.734) sits between the 8-gen LOGO (0.694) and cross-model chains (0.764). The cross-model chains gain ~+0.031 over the matched 5-gen LOGO baseline, confirming that heterogeneous generator chains provide additional discriminative signal beyond what single-generator LOGO captures.
