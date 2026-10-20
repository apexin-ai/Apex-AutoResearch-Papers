# Citation Expansion: 20 References for "When Does Error Injection Help LLM Agents?"

Generated: 2026-05-15
Status: 20 references total (16 existing verified + 4 newly added)

---

## Cluster 1: Error Injection for Agents (6 refs)

### 1. PALADIN (Vuddanti et al., 2025) — EXISTING, VERIFIED
- **BibTeX key**: `vuddanti2025paladin`
- **Title**: PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases
- **Authors**: Sri Vatsa Vuddanti, Aarav Shah, Satwik Kumar Chittiprolu, Tony Song, Sunishchal Dev, Kevin Zhu, Maheep Chaudhary
- **Year**: 2025
- **Venue**: arXiv 2509.25238
- **Relation**: Primary comparison target. Taxonomy-guided error injection + retrieval yields +57pp on ToolBench; we test the training component on ALFWorld and find no transfer.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, authors)

### 2. ETO (Song et al., ACL 2024) — EXISTING, VERIFIED
- **BibTeX key**: `song2024eto`
- **Title**: Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents
- **Authors**: Yifan Song, Da Yin, Xiang Yue, Jie Huang, Sujian Li, Bill Yuchen Lin
- **Year**: 2024
- **Venue**: ACL 2024 Main Conference (arXiv 2403.02502)
- **Relation**: DPO on failure-success trajectory pairs for agent training. Key contrast: ETO uses contrastive learning, we use direct SFT mixing.
- **Verified**: Yes (WebSearch confirmed venue, authors, arXiv ID)

### 3. EEF (Lan et al., 2025) — EXISTING, VERIFIED
- **BibTeX key**: `lan2025eef`
- **Title**: Exploring Expert Failures Improves LLM Agent Tuning
- **Authors**: Li-Cheng Lan, Andrew Bai, Minhao Cheng, Ruochen Wang, Cho-Jui Hsieh, Tianyi Zhou
- **Year**: 2025
- **Venue**: arXiv 2504.13145
- **Relation**: Extracts positive signal from failed expert trajectories (WebShop SOTA 62%). Contrasts with our approach: EEF extracts good from bad, we inject bad into good.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, authors)

### 4. AgentDebug (Zhu et al., 2025) — EXISTING, VERIFIED
- **BibTeX key**: `zhu2025agentdebug`
- **Title**: Where LLM Agents Fail and How They can Learn From Failures
- **Authors**: Kunlun Zhu, Zijia Liu, Bingxuan Li, Muxin Tian, Yingxuan Yang, Jiaxun Zhang, et al.
- **Year**: 2025
- **Venue**: arXiv 2509.25370
- **Relation**: 5-dimension error taxonomy for ALFWorld/GAIA/WebShop + debugging framework. Complementary taxonomy design; they focus on inference-time correction, we on training-time injection.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, GitHub repo)

### 5. AgentHER (2026) — NEW, VERIFIED
- **BibTeX key**: `agenther2026`
- **Title**: AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling
- **Authors**: (see arXiv 2603.21357 for full list)
- **Year**: 2026
- **Venue**: arXiv 2603.21357
- **Relation**: Relabels failed trajectories by finding alternative goals they satisfy (HER for agents). +7-12pp over success-only SFT on WebArena/ToolBench. Another failure-utilization strategy orthogonal to error injection.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, method)

### 6. Wang et al. (2024) — EXISTING (was in writing_plan), VERIFIED
- **BibTeX key**: `wang2024learning`
- **Title**: Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents
- **Authors**: Renxi Wang, Haonan Li, Xudong Han, Yixuan Zhang, Timothy Baldwin
- **Year**: 2024
- **Venue**: arXiv 2402.11651
- **Relation**: Argues failed trajectories contain valuable signal; proposes quality control strategies for integrating negative examples into SFT. Direct methodological predecessor to our error injection approach.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, authors)

---

## Cluster 2: Training Instability & Seed Sensitivity (3 refs)

### 7. McCoy et al. (2020) — EXISTING, VERIFIED
- **BibTeX key**: `mccoy2020berts`
- **Title**: BERTs of a feather do not generalize together: Large variability in generalization across models with similar test set performance
- **Authors**: R. Thomas McCoy, Junghyun Min, Tal Linzen
- **Year**: 2020
- **Venue**: BlackboxNLP 2020 (arXiv 1911.02969)
- **Relation**: 100 BERT fine-tuning runs show 0-66% variance on generalization despite similar dev accuracy. Supports our finding that seed variance is a fundamental issue, not an artifact.
- **Verified**: Yes (WebSearch confirmed arXiv ID, venue, authors)

### 8. Mosbach et al. (2021) — EXISTING, VERIFIED
- **BibTeX key**: `mosbach2021stability`
- **Title**: On the Stability of Fine-tuning BERT: Misconceptions, Explanations, and Strong Baselines
- **Authors**: Marius Mosbach, Maksym Andriushchenko, Dietrich Klakow
- **Year**: 2021
- **Venue**: ICLR 2021 (arXiv 2006.04884)
- **Relation**: Fine-tuning instability caused by optimization difficulties (vanishing gradients), not catastrophic forgetting. Our variance gradient (more injection → more instability) extends this to augmented agent training.
- **Verified**: Yes (WebSearch confirmed — note: ICLR 2021, not EMNLP as initially noted in some places)

### 9. D'Amour et al. (2022) — EXISTING, VERIFIED
- **BibTeX key**: `damour2022underspecification`
- **Title**: Underspecification Presents Challenges for Credibility in Modern Machine Learning
- **Authors**: Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, et al. (36 authors)
- **Year**: 2022
- **Venue**: JMLR Vol. 23 (arXiv 2011.03395)
- **Relation**: Models with identical training performance can behave very differently in deployment. Our TaxEI seeds 42/123 match vanilla but seed 0 collapses — a concrete instance of underspecification in agent training.
- **Verified**: Yes (WebSearch confirmed — JMLR 2022, not NeurIPS)

---

## Cluster 3: Data Mixing, Noise & Curriculum (4 refs)

### 10. Rolnick et al. (2017) — EXISTING, VERIFIED
- **BibTeX key**: `rolnick2017robust`
- **Title**: Deep Learning is Robust to Massive Label Noise
- **Authors**: David Rolnick, Andreas Veit, Serge Belongie, Nir Shavit
- **Year**: 2017
- **Venue**: arXiv 1705.10694
- **Relation**: Vision DNNs tolerate 100:1 noise-to-clean ratio. Contrasts with our finding: embodied planning collapses at ~25% injection. Task structure determines noise tolerance.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, authors)

### 11. Ye et al. (ICLR 2025) — EXISTING, VERIFIED
- **BibTeX key**: `ye2025mixing`
- **Title**: Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance
- **Authors**: Jiasheng Ye, Peiju Liu, Tianxiang Sun, Jun Zhan, Yunhua Zhou, Xipeng Qiu
- **Year**: 2025
- **Venue**: ICLR 2025 (arXiv 2403.16952)
- **Relation**: Establishes that data mixture proportions follow predictable laws with critical thresholds. Supports our dose-response finding that injection ratio has a non-linear threshold effect.
- **Verified**: Yes (WebSearch confirmed ICLR 2025, arXiv ID, authors)

### 12. Bengio et al. (2009) — EXISTING, VERIFIED
- **BibTeX key**: `bengio2009curriculum`
- **Title**: Curriculum Learning
- **Authors**: Yoshua Bengio, J\'{e}r\^{o}me Louradour, Ronan Collobert, Jason Weston
- **Year**: 2009
- **Venue**: ICML 2009
- **Relation**: Training order matters: easy-to-hard curriculum improves generalization. Error injection violates curriculum ordering by introducing hard/impossible examples early, potentially explaining the instability we observe.
- **Verified**: Yes (WebSearch confirmed ICML 2009, authors)

### 13. Madry et al. (2018) — EXISTING, VERIFIED
- **BibTeX key**: `madry2018towards`
- **Title**: Towards Deep Learning Models Resistant to Adversarial Attacks
- **Authors**: Aleksander Madry, Aleksandar Makelov, Ludwig Schmidt, Dimitris Tsipras, Adrian Vladu
- **Year**: 2018
- **Venue**: ICLR 2018 (arXiv 1706.06083)
- **Relation**: PGD adversarial training improves robustness but reduces clean accuracy. Analogous to our observation: error injection trades stability for potential robustness, but in embodied planning neither side of the tradeoff materializes.
- **Verified**: Yes (WebSearch confirmed ICLR 2018, arXiv ID, authors)

---

## Cluster 4: ALFWorld Methods (5 refs)

### 14. ALFWorld (Shridhar et al., 2021) — EXISTING, VERIFIED
- **BibTeX key**: `shridhar2021alfworld`
- **Title**: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning
- **Authors**: Mohit Shridhar, Xingdi Yuan, Marc-Alexandre C\^{o}t\'{e}, Yonatan Bisk, Adam Trischler, Matthew Hausknecht
- **Year**: 2021
- **Venue**: ICLR 2021 (arXiv 2010.03768)
- **Relation**: Our evaluation environment. 6 task types, 47 unseen test tasks, text-based embodied planning.
- **Verified**: Yes (WebSearch confirmed ICLR 2021, arXiv ID, authors)

### 15. ReAct (Yao et al., 2023) — EXISTING, VERIFIED
- **BibTeX key**: `yao2023react`
- **Title**: ReAct: Synergizing Reasoning and Acting in Language Models
- **Authors**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- **Year**: 2023
- **Venue**: ICLR 2023 (arXiv 2210.03629)
- **Relation**: Foundational prompting framework for ALFWorld agents. Our SFT agents implicitly learn ReAct-style reasoning from expert trajectories.
- **Verified**: Yes (WebSearch confirmed ICLR 2023, arXiv ID, authors)

### 16. Reflexion (Shinn et al., 2023) — EXISTING, VERIFIED
- **BibTeX key**: `shinn2023reflexion`
- **Title**: Reflexion: Language Agents with Verbal Reinforcement Learning
- **Authors**: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Year**: 2023
- **Venue**: NeurIPS 2023 (arXiv 2303.11366)
- **Relation**: Inference-time self-reflection achieves ~97% on ALFWorld via multi-trial verbal feedback. Key contrast: inference-time reflection succeeds where training-time injection fails.
- **Verified**: Yes (WebSearch confirmed NeurIPS 2023, arXiv ID, authors)

### 17. CoEx (Kim & Hwang, EMNLP 2025 Findings) — NEW, VERIFIED
- **BibTeX key**: `kim2025coex`
- **Title**: CoEx -- Co-evolving World-model and Exploration
- **Authors**: Minsoo Kim, Seung-won Hwang
- **Year**: 2025
- **Venue**: Findings of EMNLP 2025 (arXiv 2507.22281)
- **Relation**: SOTA on ALFWorld (93.28%) via co-evolving world model and exploration. Contextualizes our vanilla 65.3% relative to SOTA approaches.
- **Verified**: Yes (WebSearch confirmed Findings of EMNLP 2025, arXiv ID, authors)

### 18. AgentPRM (Choudhury, 2025) — NEW, VERIFIED
- **BibTeX key**: `choudhury2025agentprm`
- **Title**: Process Reward Models for LLM Agents: Practical Framework and Directions
- **Authors**: Sanjiban Choudhury
- **Year**: 2025
- **Venue**: arXiv 2502.10325
- **Relation**: Process reward model for ALFWorld; 3B model outperforms GPT-4o. Shows RL-based approaches succeed on ALFWorld where our SFT injection fails — further evidence that error injection's failure is method-specific, not environment-specific.
- **Verified**: Yes (WebSearch confirmed arXiv ID, title, author, ALFWorld evaluation)

---

## Cluster 5: Training Dynamics (3 refs)

### 19. Arpit et al. (2017) — EXISTING, VERIFIED
- **BibTeX key**: `arpit2017memorization`
- **Title**: A Closer Look at Memorization in Deep Networks
- **Authors**: Devansh Arpit, Stanis{\l}aw Jastrz\k{e}bski, Nicolas Ballas, David Krueger, Emmanuel Bengio, Maxinder S. Kanwal, Tegan Maharaj, Asja Fischer, Aaron Courville, Yoshua Bengio, Simon Lacoste-Julien
- **Year**: 2017
- **Venue**: ICML 2017 (arXiv 1706.05394)
- **Relation**: DNNs learn simple patterns first, then memorize noise. Supports our training-eval paradox: injected models achieve lower training loss (memorization) but worse eval performance.
- **Verified**: Yes (WebSearch confirmed ICML 2017, arXiv ID, authors)

### 20. LIMA (Zhou et al., 2023) — EXISTING, VERIFIED
- **BibTeX key**: `zhou2023lima`
- **Title**: LIMA: Less Is More for Alignment
- **Authors**: Chunting Zhou, Pengfei Liu, Puxin Xu, Srini Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis, Luke Zettlemoyer, Omer Levy
- **Year**: 2023
- **Venue**: NeurIPS 2023 (arXiv 2305.11206)
- **Relation**: Superficial alignment hypothesis — 1K curated examples suffice for instruction following. Implies error-injected samples may teach surface formatting rather than deep error reasoning.
- **Verified**: Yes (WebSearch confirmed NeurIPS 2023, arXiv ID)

### (Longpre et al., 2020 — removed from count as ref #21 would exceed 20, but included below for appendix use)

### Longpre et al. (2020) — EXISTING, VERIFIED (optional/appendix)
- **BibTeX key**: `longpre2020augmentation`
- **Title**: How Effective is Task-Agnostic Data Augmentation for Pretrained Transformers?
- **Authors**: Shayne Longpre, Yu Wang, Christopher DuBois
- **Year**: 2020
- **Venue**: Findings of EMNLP 2020
- **Relation**: Data augmentation techniques that help non-pretrained models fail for pretrained transformers. Parallel to our finding that error injection fails for pretrained LLM agents.
- **Verified**: Yes (WebSearch confirmed Findings of EMNLP 2020, authors)

---

## Summary

| # | Status | Cluster | Key |
|---|--------|---------|-----|
| 1 | Existing ✓ | Error injection | vuddanti2025paladin |
| 2 | Existing ✓ | Error injection | song2024eto |
| 3 | Existing ✓ | Error injection | lan2025eef |
| 4 | Existing ✓ | Error injection | zhu2025agentdebug |
| 5 | **NEW** ✓ | Error injection | agenther2026 |
| 6 | Existing ✓ | Error injection | wang2024learning |
| 7 | Existing ✓ | Instability | mccoy2020berts |
| 8 | Existing ✓ | Instability | mosbach2021stability |
| 9 | Existing ✓ | Instability | damour2022underspecification |
| 10 | Existing ✓ | Data/noise | rolnick2017robust |
| 11 | Existing ✓ | Data/noise | ye2025mixing |
| 12 | Existing ✓ | Data/noise | bengio2009curriculum |
| 13 | Existing ✓ | Data/noise | madry2018towards |
| 14 | Existing ✓ | ALFWorld | shridhar2021alfworld |
| 15 | Existing ✓ | ALFWorld | yao2023react |
| 16 | Existing ✓ | ALFWorld | shinn2023reflexion |
| 17 | **NEW** ✓ | ALFWorld | kim2025coex |
| 18 | **NEW** ✓ | ALFWorld | choudhury2025agentprm |
| 19 | Existing ✓ | Training dynamics | arpit2017memorization |
| 20 | Existing ✓ | Training dynamics | zhou2023lima |
| +1 | Existing ✓ | Training dynamics | longpre2020augmentation (optional) |

**Total**: 20 core references (all WebSearch-verified) + 1 optional = 21 available

## Corrections to Existing References

1. **Mosbach et al. (2021)**: Venue is **ICLR 2021**, not EMNLP.
2. **D'Amour et al. (2022)**: Venue is **JMLR Vol. 23**, not NeurIPS.
3. **McCoy et al. (2020)**: Venue is **BlackboxNLP 2020** (EMNLP workshop), arXiv 1911.02969.
4. **Rolnick et al. (2017)**: No formal venue found beyond arXiv 1705.10694.
5. **CoEx**: Authors are Kim & Hwang (2 authors), not "Zhang et al." as noted in writing_plan.yaml.
6. **AgentPRM (arXiv 2502.10325)**: Single author (Choudhury), not to be confused with the separate AgentPRM paper (arXiv 2511.08325) by Xiong et al. which appeared later at WWW 2026.
