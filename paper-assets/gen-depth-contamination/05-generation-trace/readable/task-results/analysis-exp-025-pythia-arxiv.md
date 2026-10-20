# analysis exp 025 pythia arxiv

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_025_pythia_arxiv_20260516T185842_result.json`
- **Structured JSON:** [`1031eabcb54680661388.json`](../../sessions/10/1031eabcb54680661388.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。以下是完整分析结果：

```
K_star: 3
pairwise_auc:
  0v1: 0.9877
  1v2: 0.8047
  2v3: 0.6545
  3v4: 0.5507
  4v5: 0.5287
pairwise_jsd:
  0v1: 0.171338
  1v2: 0.057344
  2v3: 0.019524
  3v4: 0.009917
  4v5: 0.008846
bootstrap_ci:
  0v1: {auc: 0.9876, ci_lower: 0.9851, ci_upper: 0.9900, perm_p: 0.0001}
  1v2: {auc: 0.8047, ci_lower: 0.7934, ci_upper: 0.8162, perm_p: 0.0001}
  2v3: {auc: 0.6544, ci_lower: 0.6401, ci_upper: 0.6688, perm_p: 0.0001}
  3v4: {auc: 0.5500, ci_lower: 0.5340, ci_upper: 0.5657, perm_p: 0.0001}
  4v5: {auc: 0.5284, ci_lower: 0.5122, ci_upper: 0.5443, perm_p: 0.0010}
ordinal:
  MAE: 0.8518
  Accuracy: 0.4545
top_features:
  1. freq_entropy (9845)
  2. surp_std (7968)
  3. surp_mean (7568)
  4. surp_d1_skew (7180)
  5. surp_d1_mean (7124)
key_finding: "Pythia-1.4B on arXiv yields K*=3 (θ=0.60), identical to exp-024 (Qwen on arXiv). The 2v3 boundary is the last distinguishable pair with CI lower bound (0.6401) firmly above theta. Domain saturation depth is model-invariant for arXiv."
comparison_with_exp024: "exp-024 Qwen arXiv: K*=3, 1v2=0.858, 2v3=0.6427, 3v4=0.5437. exp-025 Pythia arXiv: K*=3, 1v2=0.8047, 2v3=0.6545, 3v4=0.5507. Same K*, slightly different AUC magnitudes (Pythia lower at 1v2 by ~0.05, slightly higher at 2v3/3v4). Conclusion: arXiv domain effect (K*=3) is robust across model architectures — this is a domain property, not a Qwen-specific artifact."
```

---
