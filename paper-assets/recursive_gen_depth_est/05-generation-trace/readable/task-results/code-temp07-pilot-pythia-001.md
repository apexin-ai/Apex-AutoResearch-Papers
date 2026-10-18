# code temp07 pilot pythia 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_temp07_pilot_pythia_001_20260515T163617_result.json`
- **Structured JSON:** [`a9e2151f536cd6f6af31.json`](../../sessions/a9/a9e2151f536cd6f6af31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

## 结果总结

**temp07_pilot_pythia_001** — 已完成 ✅

| 指标 | τ=0.7 | τ=0.9 baseline |
|------|-------|----------------|
| d1v2 AUC (RF) | **0.8378** | 0.8327 |
| d1v2 AUC (LR) | **0.8031** | 0.7833 |
| 6-class RF acc | 57.3% | — |

**核心发现：d1v2 inversion 在 τ=0.7 within-strategy 评估中未出现。** τ=0.7 的 d1v2 AUC 与 τ=0.9 几乎一致（RF +0.005, LR +0.020），说明 temperature 均匀缩放 logit 不影响组内深度可分性。

Cross-strategy LOO 中观察到的 d1v2 inversion (GPT-2 XL: 0.129, OLMo: 0.253) 是**跨策略泛化**问题——temperature 策略的 d1 特征分布与 nucleus/topk50 的 d2 重叠，导致跨策略分类器系统性高估深度。这不是 τ=0.7 特有的，而是 temperature 解码策略的固有属性。

产出文件：`results/temp07_pilot/` (features.jsonl, pairwise_auc.json, results.json, confusion_matrix.png, classification_report.txt)

---
