# rebuttal w1 crossmodel cv v2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_rebuttal_w1-crossmodel-cv-v2_20260520T030947_result.json`
- **Structured JSON:** [`c18ae8eb8d2801329113.json`](../../sessions/c1/c18ae8eb8d2801329113.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**确认原代码确实是 sample-level 5-fold StratifiedKFold CV**（`cross_model_chains.py` 全局 balance 后随机分 fold）。

**已改为 LOGO 并重跑**，每 fold 持出一个 generator 的全部样本：

| 指标 | 原 5-fold CV | LOGO | 95% CI |
|------|-------------|------|--------|
| 3-class macro F1 | 0.809 | 0.789 | [0.777, 0.800] |
| Binary F1 | 0.764 | **0.830** | [0.818, 0.841] |

Binary F1 反而从 0.764 提升至 0.830——LOGO 迫使分类器学习 generator-invariant depth 特征，泛化更好。5 个 generator 的 binary F1 均 ≥ 0.81。

报告已写入 `artifacts/rebuttal_w1_crossmodel_cv.md`，结果 JSON 在服务器 `results/cross_model_logo_results.json`。论文中 abstract/§5.1/conclusion/limitations 的 0.764 需更新为 0.830。

---
