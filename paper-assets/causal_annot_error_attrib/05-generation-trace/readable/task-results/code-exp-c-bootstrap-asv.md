# code exp c bootstrap asv

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_c_bootstrap_asv_20260522T112843_result.json`
- **Structured JSON:** [`ff7982fdb4651abe7a9a.json`](../../sessions/ff/ff7982fdb4651abe7a9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Topology | δ* point | 95% CI | valid/total |
|---|---|---|---|
| Confounding | — | — (threshold never reached) | 0/1000 |
| Exposure | 0.937 | [0.602, 1.363] | 907/1000 |
| IV | 0.754 | [0.435, 1.290] | 902/1000 |

Confounding 的 τ_true=2.0 较大，10% bias 阈值（0.2）在整个 δ 扫描范围内都未被触及，说明该拓扑对标注误差鲁棒。Exposure 和 IV 的 CI 宽度分别为 0.76 和 0.86，约 ~10% 的 bootstrap 样本也未触及阈值（93/98 个 None）。

三个输出文件已生成：`artifacts/exp_c_bootstrap_asv.py`、`artifacts/exp_c_bootstrap_results.json`、`artifacts/exp_c_bootstrap_figure.pdf`。

---
