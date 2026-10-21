Semantic Feature Ablation Results (C4, Qwen2.5-1.5B)

15D → 17D: +semantic_cosine_sim, +entity_diversity

| Depth Pair | 15D AUC | 17D AUC | Diff |
|---|---|---|---|
| 0v1 | 0.9225 | 0.9232 | +0.0007 |
| 1v2 | 0.6123 | 0.6099 | -0.0024 |
| 2v3 | 0.5274 | 0.5239 | -0.0035 |
| 3v4 | 0.5169 | 0.5201 | +0.0032 |
| 4v5 | 0.5162 | 0.5120 | -0.0042 |

K* = 2 (both 15D and 17D, unchanged)

Feature Importance (17D model):
- semantic_cosine_sim: rank 11/17 (importance=277.8)
- entity_diversity: rank 17/17 (importance=76.8, last)

Conclusion: Surface statistical features sufficient. Semantic features add no discriminative power at the boundary.