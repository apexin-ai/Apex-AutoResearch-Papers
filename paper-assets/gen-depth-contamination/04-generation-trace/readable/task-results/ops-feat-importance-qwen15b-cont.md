# ops feat importance qwen15b cont

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feat_importance_qwen15b_cont_20260521T073611_result.json`
- **Structured JSON:** [`c9f246fa144cd0407fe0.json`](../../sessions/c9/c9f246fa144cd0407fe0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

```
MODEL: Qwen-1.5B-cont
DOMAIN: C4
DATA: data/exp_qwen_retrain_chain/features.csv (40K samples, depths 0-7)

0v1_BASELINE_AUC: 0.9945
0v1_TOP3: surp_d1_std (0.1939), surp_std (0.0562), surp_mean (0.0108)

1v2_BASELINE_AUC: 0.9025
1v2_TOP3: surp_skew (0.0915), surp_std (0.0841), surp_d1_std (0.0234)

2v3_BASELINE_AUC: 0.8099
2v3_TOP3: surp_skew (0.0637), surp_mean (0.0468), surp_std (0.0440)
```

输出文件：
- `results/feature_importance_qwen_cont/importance_results.json`
- `artifacts/feature_importance_qwen_1.5b_cont.pdf`
- `artifacts/feature_importance_qwen_1.5b_cont.tex`

注意：2v3 AUC 仍为 0.81，说明 continuation mode 下 depth 2 和 3 仍有较强可区分性（不像 prompt chain 那样在 K*=2 后趋于不可区分）。importance 分布从 0v1 的高度集中（surp_d1_std 独大，entropy=0.451）到 2v3 逐步分散（entropy=0.824）。

---
