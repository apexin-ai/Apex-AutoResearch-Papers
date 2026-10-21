# research literature supplement

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_supplement_20260520T234638_result.json`
- **Structured JSON:** [`379a1a2c21ba9b9e4cdc.json`](../../sessions/37/379a1a2c21ba9b9e4cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。文件已更新并注册。变更摘要：

**新增 3 篇文献（Section 3）：**
- **Li et al. (EMNLP 2024)** — Contamination Detector，9,229 条 MMLU item-level web-overlap 标注。定位为 primary ground truth source，解释了 enrichment≈1.0 的原因（global vs differential contamination 区分）。
- **Dekoninck et al. (NeurIPS 2024)** — ConStat，performance-based 污染检测。与 DIF 互补：ConStat 检测 model-level performance anomaly，DIF 检测 item-level differential functioning。
- **Zhang et al. (NeurIPS 2024)** — GSM1K，10–13pp accuracy drop 的里程碑实证。定位为 motivating example。

**次要修正：**
- **Oren et al.** — 补充了 canonical ordering 与 DIF 的方法论近似性和区别（都是统计检验，但检测目标不同）。
- **Growing Pains arXiv ID** — 确认 2604.12843 无误，无需修改。
- **Tao, Wang et al. (arXiv 2510.09259)** — 新增 Self-Critique 条目，RL post-training 隐藏污染信号，作为次要条目列入 Section 3 末尾。

---
