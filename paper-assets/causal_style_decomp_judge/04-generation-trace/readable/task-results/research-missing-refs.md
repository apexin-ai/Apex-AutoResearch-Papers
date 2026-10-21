# research missing refs

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_missing-refs_20260522T043517_result.json`
- **Structured JSON:** [`e582ba19250cdf210859.json`](../../sessions/e5/e582ba19250cdf210859.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕，以下是验证结果。

---

## Reference 1: "Girrbach et al. Likert or Not"

- **状态: 存疑 — 两篇论文混淆**

不存在一篇由 Girrbach 撰写、标题为 "Likert or Not" 的论文。这很可能是以下两篇论文的混淆：

**论文 A — 标题匹配 "Likert or Not"，但作者不含 Girrbach：**

```bibtex
@article{godfrey2025likert,
  title={Likert or Not: {LLM} Absolute Relevance Judgments on Fine-Grained Ordinal Scales},
  author={Godfrey, Charles and Nie, Ping and Ostapuk, Natalia and Ken, David and Gao, Shang and Inati, Souheil},
  journal={arXiv preprint arXiv:2505.19334},
  year={2025}
}
```
- 内容：pointwise scoring vs listwise ranking，ordinal scale 粒度对 LLM relevance judgment 的影响
- 偏 IR 方向，与 LLM-as-Judge style bias 关系较远

**论文 B — 作者含 Girrbach，讨论 Likert-scale rating 问题，但标题不是 "Likert or Not"：**

```bibtex
@article{girrbach2025reference,
  title={Reference-Free Rating of {LLM} Responses via Latent Information},
  author={Girrbach, Leander and Su, Chi-Ping and Saanum, Tankred and Socher, Richard and Schulz, Eric and Akata, Zeynep},
  journal={arXiv preprint arXiv:2509.24678},
  year={2025}
}
```
- 内容：LLM judge 用 Likert-scale 打分时 scores 不稳定、calibration 差、top-of-scale compression、frequent ties。提出 Latent Judges 用 internal signals 替代显式打分
- **与 style bias 项目高度相关，极可能是你想引的那篇**

**建议：确认你想引的是论文 B (Girrbach et al., 2025)，修正标题为 "Reference-Free Rating of LLM Responses via Latent Information"。**

---

## Reference 2: PRePair (Jeong et al. 2025)

- **状态: 存在**
- 完整标题: The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of LLM Evaluators
- 作者: Hawon Jeong, ChaeHun Park, Jimin Hong, Hojoon Lee, Jaegul Choo
- Venue: BlackboxNLP 2025 (EMNLP Workshop), Suzhou, China
- PRePair 是论文提出的方法（Pointwise Reasoning Enhanced Pairwise evaluation）

```bibtex
@inproceedings{jeong-etal-2025-comparative,
    title = "The Comparative Trap: Pairwise Comparisons Amplifies Biased Preferences of {LLM} Evaluators",
    author = "Jeong, Hawon and Park, ChaeHun and Hong, Jimin and Lee, Hojoon and Choo, Jaegul",
    booktitle = "Proceedings of the 8th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks for NLP",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.blackboxnlp-1.5/",
    doi = "10.18653/v1/2025.blackboxnlp-1.5",
    pages = "79--108"
}
```

---

## Reference 3: Acquiescence Bias / Central Tendency Bias 经典引用

- **状态: 存在，推荐两篇互补经典**

**推荐 A — Krosnick (1999)：survey response bias 的综述性权威引用**

覆盖 acquiescence bias、satisficing、response order effects、central tendency 等所有 rating scale bias，被引 5000+。

```bibtex
@article{krosnick1999survey,
  title={Survey Research},
  author={Krosnick, Jon A.},
  journal={Annual Review of Psychology},
  volume={50},
  number={1},
  pages={537--567},
  year={1999},
  doi={10.1146/annurev.psych.50.1.537},
  publisher={Annual Reviews}
}
```

**推荐 B — Paulhus (1991)：response bias measurement 的经典 chapter**

专门讨论 acquiescence、social desirability、extreme response style 的测量与控制，心理测量学标准引用。

```bibtex
@incollection{paulhus1991measurement,
  title={Measurement and Control of Response Bias},
  author={Paulhus, Delroy L.},
  booktitle={Measures of Personality and Social Psychological Attitudes},
  editor={Robinson, John P. and Shaver, Phillip R. and Wrightsman, Lawrence S.},
  pages={17--59},
  year={1991},
  publisher={Academic Press},
  address={San Diego, CA}
}
```

**建议：引 Krosnick (1999) 作为一站式引用最方便（一篇覆盖 acquiescence + central tendency + satisficing）。如果需要更专门讨论 response style 的分类学，补引 Paulhus (1991)。**

---
