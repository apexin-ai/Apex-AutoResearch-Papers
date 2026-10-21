# research coral ordinal literature

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_coral_ordinal_literature_20260519T103232_result.json`
- **Structured JSON:** [`0d8415d44416bef00fdd.json`](../../sessions/0d/0d8415d44416bef00fdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。产出已注册为 `art_20260519_6f34d3`。

**调研结论摘要：**

- **CORAL 原论文**: Cao, Mirjalili, Raschka (Pattern Recognition Letters 2020, arXiv 1901.07884)，K-1 binary subtask + weight-sharing 保证 rank consistency
- **NLP 中的 ordinal classification**: Kasa et al. (ACL 2024 Findings) 直接比较了 ordinal vs nominal 文本分类，ordinal 方法在 MAE 上显著更优
- **Novelty**: 目前没有论文将 ordinal regression 用于 AI-generated text detection，我们的 recursive generation depth 是新颖 framing
- **竞品**: CORN 去掉 weight-sharing 约束但更复杂，THOR 是回归式方法不产生概率，对我们 K=4 小规模问题 CORAL 是最佳选择
- **推荐 Related Work 必引 4 篇**: CORAL, Kasa et al. 2024, Frank & Hall 2001, Gutiérrez et al. 2016 综述

---
