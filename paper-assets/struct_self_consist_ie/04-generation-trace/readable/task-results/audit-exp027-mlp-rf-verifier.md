# audit exp027 mlp rf verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_exp027-mlp-rf-verifier_20260519T220906_result.json`
- **Structured JSON:** [`cda535cdedf50135df3f.json`](../../sessions/cd/cda535cdedf50135df3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论：✅ 数据存在，论文数值匹配

### 数据源路径

| 文件 | 说明 |
|------|------|
| `/root/autodl-tmp/struct_self_consist_ie/output/exp_027_mlp_verifier/results.json` | **论文引用的主数据源**（SciERC, N=16, 3 seeds: 42/123/456, 5-fold CV） |
| `/root/autodl-tmp/struct_self_consist_ie/output/exp_027v2_mlp_verifier/results.json` | v2 版本（MLP 有 hyperparameter 调整，数值略不同） |
| `/root/autodl-tmp/struct_self_consist_ie/output/supervised_verifier_upgrade/results.json` | 3 数据集全量结果（SciERC/CoNLL/Few-NERD） |
| `/root/autodl-tmp/struct_self_consist_ie/output/r17_analyses/mlp_verifier_comparison.json` | 汇总对比（含 diagnosis） |

### 数值比对（appendix L437 vs `exp_027_mlp_verifier`）

| 指标 | 论文声称 | 数据实际值 | 匹配 |
|------|---------|-----------|------|
| Greedy F1 | 0.644 | 0.6441 | ✓ |
| LR Δ vs greedy | −0.4 pp | −0.35 pp (0.6406) | ✓ (四舍五入) |
| MLP Δ vs greedy | −1.6 pp | −1.63 pp (0.6278) | ✓ |
| RF Δ vs greedy | −3.1 pp | −3.08 pp (0.6133) | ✓ |
| AUROC (interaction vs base) | 0.634 vs 0.638 | MLP_15feat 0.6341 vs MLP_5feat 0.6381 | ✓ |

所有数值一致。experiment_plan 标记为 planned 应更新为 completed。

---
