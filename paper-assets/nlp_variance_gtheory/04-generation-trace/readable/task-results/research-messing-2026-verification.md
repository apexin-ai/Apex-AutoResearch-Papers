# research messing 2026 verification

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_messing_2026_verification_20260522T035655_result.json`
- **Structured JSON:** [`8fa42d68e430f2697af6.json`](../../sessions/8f/8fa42d68e430f2697af6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全文确认完毕。结果如下：

---

## 论文基本信息
- **标题：** Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking
- **作者：** Solomon Messing
- **arXiv ID：** 2604.11581
- **年份：** 2026（submitted 2026-04-13, revised 2026-05-13）
- **发表状态：** arXiv preprint，未见会议/期刊发表记录

## G-theory 使用确认
- **使用 G-theory：是**
- **具体方法：** Total Evaluation Error (TEE) 框架，整合了 generalizability theory（引用 Shavelson and Webb, 1991）、total survey error、text-as-data 文献。包含 G-study 方差分解和 D-study projections（Section 3.3）。
- **Facets 列表：** Items (i), Prompt variants (v), Temperature (h), Judge/model (m), Replications (r) — 共 5 个 facets，但论文中未使用 "five methodology facets" 这一表述

## 数字核实
- **"judge identity dominated at 43.8%"：准确** — Section 4.1 (Safety demonstration, AILuminate benchmark)，Judge panel 贡献 43.8% of Var(θ̂)
- **"prompt×judge interaction at 12.4%"：准确** — Section 4.1，prompt×judge 交互方差占 12.4%

## 完整 BibTeX 条目

```bibtex
@article{messing2026hidden,
  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
  author={Messing, Solomon},
  journal={arXiv preprint arXiv:2604.11581},
  year={2026},
  url={https://arxiv.org/abs/2604.11581}
}
```

**结论：论文真实存在，引用数字均准确。** 之前误报为幻觉是拼写搜索问题（搜了 "Mesting" 而非 "Messing"）。"five methodology facets" 的说法是对 5 个 facets 的合理概括，但非论文原文用语。

Sources:
- [arXiv:2604.11581 Abstract](https://arxiv.org/abs/2604.11581)
- [arXiv:2604.11581 HTML Full Text](https://arxiv.org/html/2604.11581)

---
