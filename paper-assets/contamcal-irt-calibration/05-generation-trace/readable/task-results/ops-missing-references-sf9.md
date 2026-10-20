# ops missing references sf9

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_missing_references_sf9_20260517T182959_result.json`
- **Structured JSON:** [`46092b579293cd7d4024.json`](../../sessions/46/46092b579293cd7d4024.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部找到。以下是 5 篇论文的完整 bibliographic 信息：

---

## 1. Han et al. (EACL Findings 2026)

| 字段 | 内容 |
|------|------|
| **Title** | Quantifying Data Contamination in Psychometric Evaluations of LLMs |
| **Authors** | Jongwook Han, Woojung Song, Jonggeun Lee, Yohan Jo |
| **Venue** | Findings of the Association for Computational Linguistics: EACL 2026, pp. 6070–6088, Rabat, Morocco |
| **arXiv ID** | 2510.07175 |
| **Abstract (前2句)** | Recent studies apply psychometric questionnaires to LLMs to assess high-level psychological constructs such as values, personality, moral foundations, and dark traits. Although prior work has raised concerns about possible data contamination from psychometric inventories, there has been no systematic attempt to quantify the extent of this contamination. |
| **与本文关系** | 直接相关工作：量化 contamination 对 LLM 评测的影响，但聚焦心理测量量表而非 benchmark，ContamCal 将 IRT 校准方法推广到一般 benchmark 场景。 |

---

## 2. arXiv 2601.04301 (Schaeffer et al.)

| 字段 | 内容 |
|------|------|
| **Title** | Quantifying the Effect of Test Set Contamination on Generative Evaluations |
| **Authors** | Rylan Schaeffer, Joshua Kazdan, Baber Abbasi, Ken Ziyu Liu, Brando Miranda, Ahmed Ahmed, Fazl Barez, Abhay Puri, Stella Biderman, Niloofar Mireshghallah, Sanmi Koyejo |
| **Venue** | arXiv preprint, January 2026; 相关版本 "Causally Quantifying the Effect of Test Set Contamination on Generative Benchmarks" 收录于 NeurIPS 2025 |
| **arXiv ID** | 2601.04301 |
| **Abstract (前2句)** | Test set contamination has become a critical concern for accurately assessing frontier AI systems' capabilities as they are pretrained on web-scale data. While research has thoroughly investigated the impact of test set contamination on discriminative evaluations like MCQ, comparatively little has studied its impact on generative evaluations. |
| **与本文关系** | 量化 contamination 对模型性能的因果效应（通过 controlled pretraining），为 ContamCal 的 contamination-aware 校准提供 empirical grounding：即使单次重复也可显著影响分数。 |

---

## 3. Chen et al. (EMNLP 2025)

| 字段 | 内容 |
|------|------|
| **Title** | Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation |
| **Authors** | Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray |
| **Venue** | Proceedings of EMNLP 2025 (Main Conference) |
| **arXiv ID** | 2502.17521 |
| **Abstract (前2句)** | Data contamination has raised significant concerns in evaluating LLMs. This paper examines how LLM benchmarking has evolved from a static to a dynamic paradigm, conducting an in-depth analysis of existing static and dynamic benchmarks. |
| **与本文关系** | 全面综述 contamination 检测与缓解方法，ContamCal 引用作为领域背景综述，说明现有方法侧重检测/动态评测而缺乏 post-hoc 校准手段。 |

---

## 4. arXiv 2411.03923 (Singh et al.)

| 字段 | 内容 |
|------|------|
| **Title** | Evaluation Data Contamination in LLMs: How Do We Measure It and (When) Does It Matter? |
| **Authors** | Aaditya K. Singh, Muhammed Yusuf Kocyigit, Andrew Poulton, David Esiobu, Maria Lomeli, Gergely Szilvasy, Dieuwke Hupkes |
| **Venue** | arXiv preprint, November 2024 (Meta FAIR) |
| **arXiv ID** | 2411.03923 |
| **Abstract (前2句)** | Evaluation data contamination—the inadvertent mixing of evaluation benchmark samples into pre-training corpora—has become an important concern in evaluating LLMs. While intuitively understood, it is surprisingly difficult to define precisely which samples should be considered contaminated and how contamination impacts benchmark scores. |
| **与本文关系** | 提出 ConTAM 方法量化 contamination 程度与性能增益的关系，与 ContamCal 互补：ConTAM 侧重检测阈值选择，ContamCal 侧重给定 contamination signal 后如何校准分数。 |

---

## 5. Gelman, Hill & Yajima (2012)

| 字段 | 内容 |
|------|------|
| **Title** | Why We (Usually) Don't Have to Worry About Multiple Comparisons |
| **Authors** | Andrew Gelman, Jennifer Hill, Masanao Yajima |
| **Venue** | Journal of Research on Educational Effectiveness, Vol. 5, No. 2, pp. 189–211, 2012 |
| **arXiv ID** | 0907.2478 |
| **Abstract (前2句)** | Applied researchers often face settings that seem to require multiple comparisons adjustments. We argue that the problem of multiple comparisons can disappear entirely when viewed from a hierarchical Bayesian perspective—multilevel models perform partial pooling, shifting estimates toward each other. |
| **与本文关系** | ContamCal 的 IRT 框架天然是 hierarchical Bayesian model，引用此文为理论依据：层次模型通过 partial pooling 自动处理多重比较问题，无需额外校正。 |

---

**差异说明**：
- 论文 2 的 NeurIPS 2025 收录版标题为 "**Causally** Quantifying..." 且用 "Benchmarks" 而非 "Evaluations"，arXiv 2601.04301 是扩展版。引用时建议用 NeurIPS 版本。
- 论文 4 目前仅为 arXiv preprint，未见正式会议录用信息。

Sources:
- [Han et al. - ACL Anthology](https://aclanthology.org/2026.findings-eacl.319/)
- [Han et al. - arXiv](https://arxiv.org/abs/2510.07175)
- [Schaeffer et al. - arXiv](https://arxiv.org/abs/2601.04301)
- [Schaeffer et al. - NeurIPS OpenReview](https://openreview.net/forum?id=RsmjshBEDP)
- [Chen et al. - ACL Anthology](https://aclanthology.org/2025.emnlp-main.511/)
- [Singh et al. - arXiv](https://arxiv.org/abs/2411.03923)
- [Gelman et al. - Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/19345747.2011.618213)
- [Gelman et al. - arXiv](https://arxiv.org/abs/0907.2478)

---
