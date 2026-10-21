# writing related work completeness

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_related-work-completeness_20260514T054916_result.json`
- **Structured JSON:** [`15b95cd3b0e104eb23f8.json`](../../sessions/15/15b95cd3b0e104eb23f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 1. Cite-Bib 一致性

**27 个 cite key，27 个 bib entry，完全匹配。**

- 缺失的 bib entry：**无**
- 孤立的 bib entry（未被引用）：**无**

---

## 2. 近期文献遗漏

以下论文在搜索中被发现具有较高相关性，但未出现在 related_work.tex 中：

| 论文 | Venue | Year | 与本工作的关系 |
|------|-------|------|----------------|
| **Fast-DetectGPT: Efficient Zero-Shot Detection via Conditional Probability Curvature** (Bao et al.) | ICLR | 2024 | 已引 DetectGPT 的直接后继，速度提升 340x、准确率相对提升 75%。作为 binary detection 段落的重要方法缺席 |
| **Strong Model Collapse** (Dohmatob, Feng, Subramonian, Kempe) | ICLR | 2025 | 与已引的 dohmatob2024model 同一作者，证明即使极小比例（1/1000）合成数据也导致 collapse，且更大模型会放大 collapse。直接强化本文动机 |
| **Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification** (Feng et al.) | ICLR | 2025 | 证明外部验证器可防止 collapse——depth estimation 本质上就是一种验证信号，与本文 curation 框架直接对接 |
| **DetectRL: Benchmarking LLM-Generated Text Detection in Real-World Scenarios** (Wu et al.) | NeurIPS D&B | 2024 | 展示 SOTA 检测器在真实场景下性能显著下降，为本文 depth estimation 的实用价值提供背景支撑 |
| **MGTBench: Benchmarking Machine-Generated Text Detection** (He et al.) | ACM CCS | 2024 | 首个系统性 MGT 检测基准，含 text attribution 任务（多类别归属），与 depth 分类有方法论交叉 |
| **Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts** (Tulchinskii et al.) | NeurIPS | 2023 | 用内在维度作为 zero-shot 检测特征，AI 文本的内在维度系统性低于人类文本约 1.5，可作为 depth 特征的潜在补充 |

**优先级建议**：Strong Model Collapse 和 Beyond Model Collapse 与本文动机最直接相关（model collapse + curation），建议优先补充。Fast-DetectGPT 作为 DetectGPT 的重要后继也应提及。

---

## 3. Bib 格式问题

| 条目 | 问题 |
|------|------|
| `shumailov2024collapse` | Nature 文章缺少 `volume={631}` 和 `pages={755--759}`，应补全 |
| `alain2017understanding` | 类型为 `@article`，journal 为 arXiv preprint，但该论文实际是 ICLR 2017 Workshop 论文。建议改为 `@inproceedings` 并注明 workshop，或保留 `@article` 但 year 与 arXiv ID (1610.01644, 2016年) 不完全对应 |
| `shi2025generalization` | `note={Spotlight}` 为非标准字段，部分 citation style 会将其直接输出到正文中，建议删除或移入注释 |
| Venue 命名 | NeurIPS 统一用 `Advances in NeurIPS`，其余用 `Proceedings of X` — 风格一致，可接受。但 `Advances in NeurIPS` 是非正式缩写（全称为 `Advances in Neural Information Processing Systems`），严格场合建议统一用全称或纯缩写 |
| Author 格式 | 全部 `{Last, First and ...}` 格式，一致 ✓ |
| Year 字段 | 全部完整 ✓ |

---
