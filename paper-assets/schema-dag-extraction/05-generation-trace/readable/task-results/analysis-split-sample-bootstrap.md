# analysis split sample bootstrap

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_split_sample_bootstrap_20260522T045724_result.json`
- **Structured JSON:** [`7636a2e7f8823df9c38b.json`](../../sessions/76/7636a2e7f8823df9c38b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now the LaTeX appendix paragraph:

---

**结果摘要**

| 指标 | Standard bootstrap | Cluster bootstrap | Cluster-robust SE |
|---|---|---|---|
| R² 95% CI | [0.142, 0.419] | [0.145, 0.411] | — |
| CI width Δ | baseline | -5.1% | — |
| Slope SE | 0.0250 (OLS) | — | 0.0239 (0.96×) |
| Slope p | 1.25×10⁻¹² | — | 7.19×10⁻¹² |

**判断：CI robust，共享 instances 影响可忽略 (<20%)**

尽管 DEFF=5.4（ICC=0.21, 平均每 type 出现在 21.9 个 batch 中），cluster-robust SE 反而比 OLS SE 略小（0.96×）。原因：type 共享在 BCS 值域上是"平衡"的——高/低 BCS batch 都涉及共享 type，不会产生虚假相关。跨 6 个聚类阈值（0.1–0.9）的敏感性分析一致：SE inflation 0.96–0.97×，CI width 变化 -6% 到 +6%，slope 始终 p<10⁻¹¹。

**可插入 Appendix 的 LaTeX 段落：**

```latex
\paragraph{Bootstrap CI Robustness.}
Because batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n{=}164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors \citep{cameron2008bootstrap}. Across six overlap thresholds (Jaccard distance $\in\{0.1,\ldots,0.9\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is 0.96--0.97$\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\%$ to $+6\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\ $[0.15, 0.41]$). Despite a nominal design effect of 5.4 (residual ICC${=}0.21$ among type-sharing batch pairs), the balanced distribution of shared types across the BCS range ensures that instance overlap does not inflate the estimated BCS--accuracy association. We conclude that the reported CIs are robust to the non-independence induced by shared text instances.
```

---
