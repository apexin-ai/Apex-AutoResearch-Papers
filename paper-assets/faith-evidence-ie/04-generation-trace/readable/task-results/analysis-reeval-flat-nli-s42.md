# analysis reeval flat nli s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reeval_flat_nli_s42_20260516T080058_result.json`
- **Structured JSON:** [`63f99b493a14da549b32.json`](../../sessions/63/63f99b493a14da549b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果总结

### reeval_flat_nli_s42 核心指标

| 指标 | 值 |
|------|-----|
| F1 | 0.4535 |
| Ign-F1 | 0.4448 |
| Evi-F1 | 0.8039 |
| EDCR | 0.6458 |
| Precision | 0.4670 |
| Recall | 0.4408 |

### flat-NLI 两个 seed 一致性

| | s42 | s43 | Δ |
|--|-----|-----|---|
| F1 | 0.4535 | 0.4523 | +0.0012 |
| Ign-F1 | 0.4448 | 0.4435 | +0.0013 |
| Evi-F1 | 0.8039 | 0.8158 | -0.0119 |
| EDCR | 0.6458 | 0.6505 | -0.0047 |

两个 seed 高度一致，F1/Ign-F1 差异 < 0.2%。

### CED vs flat-NLI 对比趋势

| 指标 | flat-NLI avg | CED avg | Δ(CED - flat-NLI) |
|------|-------------|---------|-----|
| F1 | 0.4529 | 0.4569 | **+0.0040** |
| Ign-F1 | 0.4442 | 0.4467 | **+0.0025** |
| Evi-F1 | 0.8099 | 0.8112 | +0.0013 |
| EDCR | 0.6482 | 0.6459 | -0.0023 |

CED 在 F1/Ign-F1 上略优于 flat-NLI（~0.3-0.4%），Evi-F1 基本持平，EDCR 略低。差异非常小。

### Paired t-test 状态

**Not ready.** 没有 per-document score 文件——需要从 4 个 `predictions.json` 计算每个 doc 的 F1 才能做 paired t-test。此外 CED s43 reeval 缺失（当前只有 CED s42 + s44），如需完整 3-seed 对比需补跑。

---
