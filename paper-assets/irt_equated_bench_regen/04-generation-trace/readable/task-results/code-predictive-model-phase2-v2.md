# code predictive model phase2 v2

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_predictive_model_phase2_v2_20260522T092120_result.json`
- **Structured JSON:** [`59c3962f6b70f49c5585.json`](../../sessions/59/59c3962f6b70f49c5585.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2 完成。结果摘要：

**23 个安全特征**（删除 18 个泄漏特征，重算 3 个 ref-only 特征），Subject-GroupKFold 5-fold CV。

| Model | Mean AUROC |
|-------|-----------|
| LR Baseline (difficulty_ref only) | 0.5808 ± 0.0353 |
| LR Full (23 features) | 0.6026 ± 0.0203 |
| LightGBM (23 features) | 0.5994 ± 0.0258 |

**SHAP top-3**: difficulty_ref (0.258), discrimination_ref (0.219), difficulty_vs_subject_ref (0.124)

**判定：Abandon recommendation** — 最佳 AUROC 0.5994 < 0.65。去除泄漏特征后，剩余 ref cohort + 文本特征对 DIF 分类的预测力接近随机水平。Full model 相对 baseline 仅提升 +0.02 AUROC，说明非 difficulty 特征几乎不提供额外信号。LR 的 recall 基本为 0（阈值 0.5 下几乎不预测正类），GBM 稍好但 F1 仅 0.18。

4 个文件已写入 `artifacts/predictive_model/` 并注册。

---
