# ops feat importance olmo1b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feat_importance_olmo1b_20260521T073604_result.json`
- **Structured JSON:** [`7045a7e2bb67733e6c32.json`](../../sessions/70/7045a7e2bb67733e6c32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

```
MODEL: OLMo-1B
DOMAIN: C4 (olmo_c4_cont)
0v1_BASELINE_AUC: 0.9987
0v1_TOP3: surp_d1_std (0.0823), surp_mean (0.0094), surp_kurt (0.0052)
1v2_BASELINE_AUC: 0.5070
1v2_TOP3: surp_mean (0.0040), surp_d2_mean (0.0031), surp_d1_skew (0.0023)
2v3_BASELINE_AUC: 0.5058
2v3_TOP3: surp_d2_std (0.0071), surp_kurt (0.0036), ttr (0.0030)
```

OLMo-1B 的 K\*=1 边界非常清晰：0v1 AUC 高达 0.9987（surp_d1_std 主导），1v2 和 2v3 均接近随机（~0.50），说明 depth ≥ 1 后特征几乎无法区分不同代数。产出文件：
- `results/feature_importance_olmo/importance_results.json`
- `artifacts/feature_importance_olmo_1b.pdf`
- `artifacts/feature_importance_olmo_1b.tex`

---
