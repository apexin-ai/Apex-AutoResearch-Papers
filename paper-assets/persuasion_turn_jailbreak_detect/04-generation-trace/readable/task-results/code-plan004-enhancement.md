# code plan004 enhancement

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-enhancement_20260517T224427_result.json`
- **Structured JSON:** [`08222f7ffe573be54bb4.json`](../../sessions/08/08222f7ffe573be54bb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`adversarial_perturbation.py` 已从 378 行增强到 603 行，新增：

**增强 1 — TF-IDF Baseline**
- `train_tfidf_classifier()`: 在 train split 上训练 TF-IDF + LogisticRegression
- `eval_tfidf()`: 在原始/扰动数据上分别评估
- 通过 `--train_path` 参数激活

**增强 2 — 扰动质量指标**
- `compute_quality_metrics()`: 计算 BERTScore F1、sentence-transformers cosine similarity、Jaccard lexical overlap
- BERTScore < threshold 的 turn 所属 conversation 被标记为低质量并在评估中排除
- 参数: `--quality_check`（默认 True）、`--bertscore_threshold`（默认 0.6）

**增强 3 — 三层对比输出表**
- 格式: `K | Model | Original F1 | Perturbed F1 | Delta (drop) | Robustness`
- 三行: TF-IDF / Vanilla DeBERTa / Persuasion DeBERTa
- 每个 K=1,2,3,full 分别输出

M001 约束（`enable_thinking=False` + `strip_thinking` regex）保持不变。依赖（`bert-score`, `sentence-transformers`）在 docstring 中已注明。

---
