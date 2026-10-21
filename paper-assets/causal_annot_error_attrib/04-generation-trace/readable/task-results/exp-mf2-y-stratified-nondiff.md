# exp mf2 y stratified nondiff

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mf2_y_stratified_nondiff_20260523T162148_result.json`
- **Structured JSON:** [`73c799ec1b8620e0169e.json`](../../sessions/73/73c799ec1b8620e0169e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF-2 完成。结果总结：

**12 configs × 3 Y-proxies = 36 tests (10,000 permutations each)**

| Y proxy | Rejections@0.05 | Median p | 解读 |
|---|---|---|---|
| **text_length** | **1/12** | 0.508 | 非差异性成立（仅 llama4_few-shot-3 边际拒绝 p=0.027）|
| topic | 11/12 | 0.002 | 差异性——预期结果：LLM 直接观测 topic 内容 |
| sentiment | 10/12 | 0.014 | 差异性——预期结果：sentiment 从文本词汇提取，与 stance 相关 |

**核心发现**：当 Y proxy 与文本内容独立（text_length）时，非差异性假设 P(A*|A,Y) = P(A*|A) 成立；当 Y proxy 可从文本内容推断（topic, sentiment）时，假设被拒绝。这与理论预期一致——LLM 不观测真实结果 Y，仅观测文本 X，所以误分类率不依赖于与内容无关的 Y 变量。

**产出文件**：
- `artifacts/nondiff_y_stratified_results.json` — 完整结果（已注册 `art_20260523_bcf3f9`）
- `artifacts/nondiff_y_stratified.py` — 本地脚本（已修复 None pred_label 问题）

---
