# ops feat importance pythia14b

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_feat_importance_pythia14b_20260521T071330_result.json`
- **Structured JSON:** [`e7e6d34d626c001ba47b.json`](../../sessions/e7/e7e6d34d626c001ba47b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果：

```
MODEL: Pythia-1.4B (wiki domain)
0v1_BASELINE_AUC: 0.9754
0v1_TOP3: surp_d1_std (0.1282), surp_mean (0.1224), freq_entropy (0.0852)
1v2_BASELINE_AUC: 0.5868
1v2_TOP3: freq_entropy (0.0558), surp_std (0.0136), self_bleu (0.0101)
2v3_BASELINE_AUC: 0.5455
```

输出文件：
- JSON: `results/feature_importance_pythia/importance_results.json`
- Barplot: `artifacts/feature_importance_pythia_1.4b.pdf`
- LaTeX table: `artifacts/feature_importance_pythia_1.4b.tex`

与 LLaMA-8B 对比：Pythia 的 0v1 AUC 更高（0.975 vs 0.922），但 1v2 boundary 更难区分（0.587 vs 0.610）。两者 1v2 的 top feature 都是 freq_entropy，但 Pythia 的 surp_d1_std 在 0v1 中是最重要特征（LLaMA-8B 同样），而 surp_mean 在 Pythia 中贡献更大（25.8%）。

---
