# audit provenance trace 8values

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_provenance-trace-8values_20260523T111959_result.json`
- **Structured JSON:** [`9b007d65811df2d5fca1.json`](../../sessions/9b/9b007d65811df2d5fca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。8 个数值的溯源结果：

| # | 论文值 | 源文件 | 一致? |
|---|--------|--------|-------|
| 1 | VIF avg 3.0, 10/12<5 | `vif_partial_corr.json:vif.mean`=2.978 | Y |
| 2 | partial r 0.31/0.12 | `vif_partial_corr.json:partial_correlation.summary.*` | Y |
| 3 | MDE=0.14 | `power_cr2_cr3.json:power_analysis.MDE_80`=0.144 | Y |
| 3 | β_std=0.164 | `k5_rf_contrast.json:rf_ols.mmlu.keff_std_beta`=0.165 | **~N** (差0.001) |
| 4 | RF R²=0.73–0.81 | `k5_rf_contrast.json:comparison_table.k3_rf` | Y |
| 5 | β_std=-0.192, p≈0.06 | `wild_cluster_bootstrap_v2.json` + `wild_cluster_bootstrap.json` (arc×sycophancy) | Y |
| 6 | 58% (61/105) | `stochastic_dominance.json:global_12_conditions` | Y |
| 7 | r≈0.82 log space | `capability_matched_subsample.json:full_set_correlation.log`=0.82 | Y (精确) |
| 8 | mean sig 1.85/12 | `random_subsample_transition.json:overall.cl_keff_sig_mean`=1.849 | Y |

唯一不完全一致的是 #3 的 β_std：JSON 为 0.16518（→0.165），论文写 0.164，差一个末位。其余 7 个数值全部匹配。

结果已写入 `docs/paper/data/provenance_trace.txt`。

---
