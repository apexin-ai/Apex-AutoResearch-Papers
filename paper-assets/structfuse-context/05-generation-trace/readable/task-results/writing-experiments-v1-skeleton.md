# writing experiments v1 skeleton

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_experiments-v1-skeleton_20260515T102528_result.json`
- **Structured JSON:** [`d5dae6256edbe4320a0d.json`](../../sessions/d5/d5dae6256edbe4320a0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已重写 `experiments_v1.md`，按要求的四段结构：

- **§4.1 Setup** — 数据集/编码器/训练/评估/seed 概述，训练细节引用 §3.4 不重复
- **§4.2 Main Results** — Table 1 (两个 panel，Seed 42/43/44 + Mean + 95% CI，LaTeX tabular)，Table 2 (fixed-checkpoint robustness)，已填入已有数值（Qwen random s42/s43/s44, embedding s43, StarCoder random s42），其余 X.XX 占位；Claim 1/2 映射段落
- **§4.3 Analysis** — 5 个子节：checkpoint selection criterion (val\_loss vs R@1 divergence)、seed variance (s44 outlier)、training dynamics (learning curve placeholder)、BM25 comparison (plan\_018 placeholder)、negative difficulty (已填实际 margin 数据)
- **§4.4 Discussion** — effect size shrinkage解读、representation geometry hypothesis、limitations 列表、downstream evaluation placeholder

---
