# Citation Verification Report

**Date**: 2026-05-15
**Scope**: All citations in paper_framing.md, memory.md, and literature_map.yaml for project tax_error_inject_agent

---

## Verified ✅

### Core Citations

- **Rolnick et al. 2017** — "Deep Learning is Robust to Massive Label Noise", arXiv 1705.10694. Authors: Rolnick, Veit, Belongie, Shavit. All correct. Paper demonstrates >90% accuracy on MNIST even with 100:1 noise dilution. [Link](https://arxiv.org/abs/1705.10694)

- **PALADIN (arXiv 2509.25238)** — "PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases". Authors: Vuddanti, Shah, Chittiprolu, Song, Dev, Zhu, Chaudhary. arXiv ID confirmed. Published at ICLR 2026. RR 32.76% → 89.68% (+57pp) confirmed. Removing retrieval drops RR to ~61.4% (~28pp drop, consistent with paper_framing's "~30pp"). [Link](https://arxiv.org/abs/2509.25238)

- **EEF (arXiv 2504.13145)** — "Exploring Expert Failures Improves LLM Agent Tuning". Authors: Li-Cheng Lan, Andrew Bai, Minhao Cheng, Cho-Jui Hsieh, Tianyi Zhou. arXiv ID confirmed. First to surpass 0.81 on WebShop, >81 on SciWorld. [Link](https://arxiv.org/abs/2504.13145)

- **AgentDebug (arXiv 2509.25370)** — "Where LLM Agents Fail and How They can Learn From Failures". arXiv ID confirmed. 5-dimensional error taxonomy (memory/reflection/planning/action/system) for ALFWorld, GAIA, WebShop. [Link](https://arxiv.org/abs/2509.25370)

- **Ye et al. ICLR 2025** — "Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance". arXiv 2403.16952. Published at ICLR 2025 (poster). Authors: Jiasheng Ye, Peiju Liu, Tianxiang Sun, Jun Zhan, Yunhua Zhou, Xipeng Qiu. Correct. Note: paper is about data mixing optimization/scaling laws, not specifically "noise-ratio threshold theory" — but the concept of "critical proportion for catastrophic forgetting" is analogous. [Link](https://arxiv.org/abs/2403.16952)

- **Arpit et al. 2017** — "A Closer Look at Memorization in Deep Networks", ICML 2017. arXiv 1706.05394. Confirmed at PMLR v70. Authors match literature_map. [Link](https://arxiv.org/abs/1706.05394)

- **Liu et al. 2020** — "Early-Learning Regularization Prevents Memorization of Noisy Labels", NeurIPS 2020. Authors: Liu, Niles-Weed, Razavian, Fernandez-Granda. All correct. [Link](https://arxiv.org/abs/2007.00151)

- **Wang et al. 2024** — "Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents", arXiv 2402.11651. Authors: Wang, Li, Han, Zhang, Baldwin. All correct. [Link](https://arxiv.org/abs/2402.11651)

- **Song et al. 2024 (ETO)** — "Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents", ACL 2024. Authors: Song, Yin, Yue, Huang, Li, Lin. +8% WebShop, +9.5% ScienceWorld vs SFT confirmed. [Link](https://aclanthology.org/2024.acl-long.409/)

- **Dohmatob et al. 2025** — "Strong Model Collapse", ICLR 2025. Authors: Dohmatob, Feng, Subramonian, Kempe. Correct. [Link](https://arxiv.org/abs/2410.04840)

- **Seddik et al. 2024** — "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse", arXiv 2404.05090. Authors: Seddik, Chen, Hayou, Youssef, Debbah. Correct. [Link](https://arxiv.org/abs/2404.05090)

- **AgentHER 2025** — "AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling", arXiv 2603.21357. Paper exists (March 2026, by Liang Ding et al.). Correct. [Link](https://arxiv.org/abs/2603.21357)

- **Dong et al. 2024** — "How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition", ACL 2024. First authors: Guanting Dong, Hongyi Yuan. Correct. [Link](https://arxiv.org/abs/2310.05492)

- **Li et al. 2025 (ICML)** — "Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models". Authors: Yuan Li, Zhengzhong Liu, Eric Xing. ICML 2025 confirmed. [Link](https://arxiv.org/abs/2508.11953)

- **WKM 2024** — "Agent Planning with World Knowledge Model", NeurIPS 2024. Confirmed. [Link](https://arxiv.org/abs/2405.14205)

- **Beyond Clean Data 2024** — "Beyond Clean Data: Exploring the Effects of Label Noise on Object Detection Performance", ScienceDirect 2024. Confirmed. [Link](https://www.sciencedirect.com/science/article/abs/pii/S095070512401178X)

- **CoEx** — "CoEx: Co-evolving World-model and Exploration", EMNLP 2025 Findings. 93.28% on ALFWorld confirmed. Authors: Minsoo Kim, Seung-won Hwang. [Link](https://aclanthology.org/2025.findings-emnlp.1179/)

- **AgentPRM** — "Process Reward Models for LLM Agents: Practical Framework and Directions", arXiv 2502.10325. Author: Sanjiban Choudhury. 91.0% on ALFWorld confirmed (Best-of-N with N=16; base policy π₃ = 88.1%). [Link](https://arxiv.org/abs/2502.10325)

- **Reflexion** — ~97% on ALFWorld with multi-trial (12 trials), NeurIPS 2023. Confirmed. [Link](https://arxiv.org/abs/2303.11366)

### Papers that exist but have metadata errors (see Issues section)

- **Luo et al. 2023** — arXiv 2308.08747. Paper exists. [Link](https://arxiv.org/abs/2308.08747)
- **Zhou et al. 2023 (LIMA)** — NeurIPS 2023. Paper exists. [Link](https://arxiv.org/abs/2305.11206)
- **Longpre 2020** — EMNLP 2020 Findings. Paper exists. [Link](https://aclanthology.org/2020.findings-emnlp.394/)
- **"Early Stopping Against Label Noise" ICLR 2024** — Paper exists. [Link](https://openreview.net/forum?id=CMzF2aOfqp)
- **"Robust Curriculum Learning" ICLR 2021** — Paper exists. [Link](https://openreview.net/forum?id=lmTWnm3coJJ)

---

## Issues Found ⚠️

### 1. ❗ Longpre 2020 — WRONG TITLE, WRONG AUTHORS, WRONG VENUE (literature_map.yaml)

**Listed in literature_map:**
- Title: "To Augment or Not to Augment? A Comparative Study on Text Augmentation Techniques for Low-Resource NLP"
- Authors: "Longpre, Wang, De Melo"
- Venue: "ACL (Computational Linguistics)"

**Actual Longpre 2020 paper:**
- Title: **"How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?"**
- Authors: Shayne Longpre, Yu Wang, **Chris DuBois** (not De Melo)
- Venue: **Findings of EMNLP 2020** (not ACL, not Computational Linguistics)
- [Link](https://aclanthology.org/2020.findings-emnlp.394/)

**The listed title belongs to a completely different paper:**
- "To Augment or Not to Augment?" is by **Gözde Gül Şahin** (solo author), published in **Computational Linguistics 2022** (vol 48, issue 1).
- [Link](https://aclanthology.org/2022.cl-1.2/)

**Action required**: Fix title, authors, and venue in literature_map.yaml. The key_finding about "label-preservation and distribution-stationarity" violations needs to be verified against the actual Longpre 2020 paper.

### 2. ❗ Luo 2023 — WRONG AUTHOR LIST (literature_map.yaml)

**Listed**: "Luo, Xu, Zheng, Zhao, Yang, Bian, Zheng"

**Actual**: Yun Luo, Zhen Yang, Fandong Meng, Yafu Li, Jie Zhou, Yue Zhang

Only "Luo" and "Yang" overlap. The other 5 names (Xu, Zheng, Zhao, Bian, Zheng) are hallucinated.

### 3. ❗ Zhou 2023 LIMA — PARTIALLY HALLUCINATED AUTHOR LIST (literature_map.yaml)

**Listed**: "Zhou, Liu, Xu, Iyer, Sun, **Du, Lin, Geng**, Zhang, **Patel**, Yu, **Hinton**"

**Actual (15 authors)**: Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, Omer Levy

- **Hallucinated names**: Du, Lin, Geng, Patel, Hinton — none are authors
- **Missing authors**: Mao, Ma, Efrat, Yu (Lili), Ghosh, Lewis, Zettlemoyer, Levy

Geoffrey Hinton is NOT an author of LIMA.

### 4. ⚠️ "Li et al. 2024" ICLR — WRONG FIRST AUTHOR (literature_map.yaml)

**Listed**: id `li2024early_stopping`, authors "Li et al."

**Actual authors**: Suqin **Yuan**, Lei **Feng**, Tongliang **Liu**

No author named "Li" in this paper. Should be "Yuan et al. 2024".

### 5. ⚠️ "Curriculum Robust 2024" — WRONG YEAR (literature_map.yaml)

**Listed**: year 2024, venue "OpenReview"

**Actual**: Published at **ICLR 2021**. Authors: Tianyi Zhou, Shengjie Wang, Jeff Bilmes.

The year is off by 3 years (2021 listed as 2024).

### 6. ⚠️ PALADIN numbers in literature_map — MISLEADING

**Listed key_finding**: "+13.6% recovery rate, +10.2% task success"

**Clarification**: The +13.6% is vs CRITIC baseline (89.68% − 76.34% ≈ 13.3pp), not vs vanilla. The headline number used in paper_framing is **+57pp vs vanilla** (32.76% → 89.68%). The literature_map gives a much smaller number without specifying the baseline, which is misleading.

### 7. ⚠️ AgentPRM — AMBIGUOUS REFERENCE, NO arXiv ID

paper_framing.md says "AgentPRM 91.0% (2025)" without an arXiv ID. Two papers share this name:
- arXiv **2502.10325** (Choudhury, Feb 2025) — evaluates on ALFWorld, achieves 91.0% with Best-of-N
- arXiv **2511.08325** (Xi et al., Nov 2025) — evaluates on WebShop/BabyAI/TextCraft, does NOT evaluate on ALFWorld

The ALFWorld 91.0% comes from arXiv 2502.10325. The reference should include the arXiv ID.

---

## Not Found ❌

None — all cited papers were found to exist. No fabricated papers detected.

---

## Summary

| Category | Count |
|----------|-------|
| Fully verified ✅ | 20 |
| Exists but has metadata errors ⚠️ | 7 |
| Fabricated / not found ❌ | 0 |

### Priority fixes for literature_map.yaml:
1. **Longpre 2020**: Fix title → "How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?", authors → "Longpre, Wang, DuBois", venue → "Findings of EMNLP 2020"
2. **Luo 2023**: Fix authors → "Luo, Yang, Meng, Li, Zhou, Zhang"
3. **Zhou 2023 LIMA**: Fix authors → "Zhou, Liu, Xu, Iyer, Sun, Mao, Ma, Efrat, Yu, Yu, Zhang, Ghosh, Lewis, Zettlemoyer, Levy"
4. **li2024early_stopping**: Fix id/authors → "Yuan, Feng, Liu" (not "Li et al.")
5. **curriculum_robust2024**: Fix year → 2021, venue → "ICLR 2021"
6. **paladin2025**: Clarify key_finding baseline or use +57pp vs vanilla
7. **AgentPRM reference**: Add arXiv ID 2502.10325

### Note on Seddik et al. title
The previous version of this report flagged the title as fabricated. The literature_map currently has the correct title "How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse" — this is accurate.

### Note on Dohmatob et al. author list
The literature_map lists "Dohmatob, Feng, Subramonian, Kempe" which is the complete and correct author list.
